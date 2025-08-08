class BlocksWorld:
    def __init__(self, initial_state, goal_state):
        """
        Initialize a Blocks World problem.
        Each state is represented as a list of stacks (lists of blocks).
        """
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def is_goal(self, state):
        """Check if the current state matches the goal state."""
        # Convert to a canonical representation for comparison
        canonical_state = sorted([tuple(stack) for stack in state if stack])
        canonical_goal = sorted([tuple(stack) for stack in self.goal_state if stack])
        
        return canonical_state == canonical_goal
    
    def get_valid_moves(self, state):
        """
        Get all valid moves from the current state.
        A move is represented as (block, destination) where destination
        is either another block or "Table".
        """
        moves = []
        
        # Get all blocks that are at the top of stacks (can be moved)
        movable_blocks = []
        for stack in state:
            if stack:  # If stack is not empty
                movable_blocks.append(stack[-1])
        
        # For each movable block, find all valid destinations
        for block in movable_blocks:
            # Can move to table
            moves.append((block, "Table"))
            
            # Can move to top of other stacks
            for target in movable_blocks:
                if target != block:
                    moves.append((block, target))
        
        return moves
    
    def apply_move(self, state, move):
        """
        Apply a move to the state and return the new state.
        Move is (block, destination).
        """
        block, destination = move
        new_state = [stack[:] for stack in state]  # Deep copy
        
        # Find the stack containing the block
        source_stack_idx = None
        for i, stack in enumerate(new_state):
            if stack and stack[-1] == block:
                source_stack_idx = i
                break
        
        if source_stack_idx is None:
            return None  # Block not found or not at top of any stack
        
        # Remove the block from its source stack
        new_state[source_stack_idx].pop()
        
        # If the source stack is now empty, remove it
        if not new_state[source_stack_idx]:
            new_state.pop(source_stack_idx)
        
        # Place the block at its destination
        if destination == "Table":
            # Create a new stack with just the block
            new_state.append([block])
        else:
            # Find the stack with the destination block on top
            dest_stack_idx = None
            for i, stack in enumerate(new_state):
                if stack and stack[-1] == destination:
                    dest_stack_idx = i
                    break
            
            if dest_stack_idx is None:
                return None  # Destination block not found or not at top
            
            # Add the block to the destination stack
            new_state[dest_stack_idx].append(block)
        
        return new_state
    
    def depth_limited_search(self, limit):
        """
        Perform depth-limited search to find a solution.
        Returns a list of moves if a solution is found, None otherwise.
        """
        def state_to_tuple(s):
            """Convert a state to a hashable tuple for visited set."""
            return tuple(tuple(stack) for stack in s if stack)
        
        visited = set()
        
        def dls_recursive(state, depth, path):
            # Check if we've reached the goal
            if self.is_goal(state):
                return path
            
            # Check if we've reached the depth limit
            if depth >= limit:
                return None
            
            # Convert state to tuple for checking visited
            state_tuple = state_to_tuple(state)
            if state_tuple in visited:
                return None
            
            visited.add(state_tuple)
            
            # Try all valid moves
            for move in self.get_valid_moves(state):
                new_state = self.apply_move(state, move)
                if new_state:  # If the move is valid
                    result = dls_recursive(new_state, depth + 1, path + [move])
                    if result:
                        return result
            
            return None
        
        return dls_recursive(self.initial_state, 0, [])

def parse_state_input(state_str):
    """Parse a string representation of a state."""
    state = []
    for stack_str in state_str.split(';'):
        if stack_str:
            stack = stack_str.split(',')
            state.append(stack)
    return state

def display_solution(solution):
    """Display the solution steps."""
    if not solution:
        print("No solution found.")
        return
    
    print(f"Solution found with {len(solution)} moves:")
    for i, move in enumerate(solution, 1):
        block, destination = move
        print(f"Step {i}: Move block {block} to {'the table' if destination == 'Table' else 'block ' + destination}")

def display_state(state):
    """Display a state in a readable format."""
    print("Current state:")
    for i, stack in enumerate(state, 1):
        print(f"Stack {i}: {stack}")
    print()

def interactive_mode():
    """Run the program in interactive mode."""
    print("=== Blocks World Depth-Limited Search ===")
    print("Enter the initial state and goal state in the format: A,B;C,D")
    print("where each letter is a block and semicolons separate stacks.")
    print("Example: A,B;C represents two stacks [A,B] and [C]")
    
    # Get initial state
    initial_str = input("\nEnter initial state: ")
    initial_state = parse_state_input(initial_str)
    
    # Get goal state
    goal_str = input("Enter goal state: ")
    goal_state = parse_state_input(goal_str)
    
    # Get depth limit
    try:
        depth_limit = int(input("Enter depth limit (default 10): ") or "10")
    except ValueError:
        depth_limit = 10
        print("Invalid input. Using default depth limit of 10.")
    
    # Create the problem and solve
    problem = BlocksWorld(initial_state, goal_state)
    
    print("\nInitial state:")
    display_state(initial_state)
    print("Goal state:")
    display_state(goal_state)
    
    print(f"\nSearching for solution with depth limit {depth_limit}...")
    solution = problem.depth_limited_search(depth_limit)
    
    # Display the solution
    print("\nResults:")
    if solution:
        display_solution(solution)
    else:
        print(f"No solution found within depth limit {depth_limit}.")
        print("Try increasing the depth limit or check if the problem is solvable.")

def example_mode():
    """Run a predefined example."""
    # Sussman anomaly
    initial_state = [["A"], ["B", "C"]]
    goal_state = [["B", "A", "C"]]
    
    print("=== Running Blocks World DLS with Sussman Anomaly Example ===")
    print("\nInitial state:")
    display_state(initial_state)
    print("Goal state:")
    display_state(goal_state)
    
    problem = BlocksWorld(initial_state, goal_state)
    depth_limit = 10
    
    print(f"\nSearching for solution with depth limit {depth_limit}...")
    solution = problem.depth_limited_search(depth_limit)
    
    # Display the solution
    print("\nResults:")
    if solution:
        display_solution(solution)
    else:
        print(f"No solution found within depth limit {depth_limit}.")

def command_line_mode(args):
    """Run the program with command line arguments."""
    if len(args) != 4 or args[1] != 'dls':
        print("Usage: python blocks_world_dls.py dls <initial_state> <goal_state>")
        print("Example: python blocks_world_dls.py dls 'A,B;C' 'A;B;C'")
        return
    
    initial_str = args[2]
    goal_str = args[3]
    
    initial_state = parse_state_input(initial_str)
    goal_state = parse_state_input(goal_str)
    
    problem = BlocksWorld(initial_state, goal_state)
    depth_limit = 10
    
    print("\nInitial state:")
    display_state(initial_state)
    print("Goal state:")
    display_state(goal_state)
    
    print(f"\nSearching for solution with depth limit {depth_limit}...")
    solution = problem.depth_limited_search(depth_limit)
    
    # Display the solution
    print("\nResults:")
    if solution:
        display_solution(solution)
    else:
        print(f"No solution found within depth limit {depth_limit}.")

def main():
    import sys
    
    if len(sys.argv) == 1:
        # No command line arguments, run interactive mode
        interactive_mode()
    elif len(sys.argv) == 2 and sys.argv[1] == 'example':
        # Run example mode
        example_mode()
    else:
        # Run with command line arguments
        command_line_mode(sys.argv)

if __name__ == "__main__":
    main()
