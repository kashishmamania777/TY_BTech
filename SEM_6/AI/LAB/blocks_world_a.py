import heapq

class BlocksWorld:
    def __init__(self, initial_state, goal_state):
        """
        Initialize the Blocks World problem.
        Each state is represented as a list of stacks (lists of blocks).
        """
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_goal(self, state):
        """
        Check if the current state exactly matches the goal state.
        Here we assume the order of stacks and blocks is important.
        """
        return state == self.goal_state

    def get_valid_moves(self, state):
        """
        Generate all valid moves from the current state.
        A move is represented as a tuple (block, destination) where destination
        is either another block (if moving onto it) or "Table" (to move the block to a new stack).
        """
        moves = []
        # Identify all blocks that can be moved (the top block of every stack)
        movable_blocks = [stack[-1] for stack in state if stack]
        for block in movable_blocks:
            # Moving to the table always forms a new stack.
            moves.append((block, "Table"))
            # Moving to any other movable block (which is on top of some stack)
            for target in movable_blocks:
                if target != block:
                    moves.append((block, target))
        return moves

    def apply_move(self, state, move):
        """
        Apply a move (block, destination) to the state and return the new state.
        """
        block, destination = move
        # Create a deep copy of the state.
        new_state = [list(stack) for stack in state]
        source_stack_idx = None
        # Locate the source stack from which 'block' is to be moved.
        for i, stack in enumerate(new_state):
            if stack and stack[-1] == block:
                source_stack_idx = i
                break

        if source_stack_idx is None:
            return None  # Block not found or not at the top

        # Remove the block from its original location.
        new_state[source_stack_idx].pop()
        if not new_state[source_stack_idx]:
            new_state.pop(source_stack_idx)

        # Place the block according to the move.
        if destination == "Table":
            new_state.append([block])
        else:
            dest_stack_idx = None
            for i, stack in enumerate(new_state):
                if stack and stack[-1] == destination:
                    dest_stack_idx = i
                    break
            if dest_stack_idx is None:
                return None
            new_state[dest_stack_idx].append(block)

        return new_state

    def state_to_tuple(self, state):
        """
        Convert the state into a hashable tuple of tuples.
        """
        return tuple(tuple(stack) for stack in state)

    def heuristic(self, state):
        """
        A simple heuristic: count the number of blocks that are not in their goal position.
        The goal position of each block is defined by its location (stack index and position).
        """
        h = 0
        state_pos = {}
        goal_pos = {}
        for i, stack in enumerate(state):
            for j, block in enumerate(stack):
                state_pos[block] = (i, j)
        for i, stack in enumerate(self.goal_state):
            for j, block in enumerate(stack):
                goal_pos[block] = (i, j)
        for block in goal_pos:
            if block not in state_pos or state_pos[block] != goal_pos[block]:
                h += 1
        return h

    def astar_search(self):
        """
        Perform A* search to find a sequence of moves from the initial state to the goal state.
        Each queue entry is a tuple (f, g, state, path) where 'f' is the total cost (g + h),
        'g' is the cost so far, and 'path' is the list of moves taken.
        """
        start = self.initial_state
        start_h = self.heuristic(start)
        queue = []
        heapq.heappush(queue, (start_h, 0, start, []))
        visited = set()
        visited.add(self.state_to_tuple(start))

        while queue:
            f, g, state, path = heapq.heappop(queue)
            if self.is_goal(state):
                return path
            for move in self.get_valid_moves(state):
                new_state = self.apply_move(state, move)
                if new_state is not None:
                    state_key = self.state_to_tuple(new_state)
                    if state_key not in visited:
                        visited.add(state_key)
                        new_path = path + [move]
                        new_g = g + 1  # each move costs 1
                        new_f = new_g + self.heuristic(new_state)
                        heapq.heappush(queue, (new_f, new_g, new_state, new_path))
        return None

def display_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Solution found with", len(solution), "move(s):")
        for i, move in enumerate(solution, 1):
            block, destination = move
            dest_str = "the table" if destination == "Table" else f"block {destination}"
            print(f"Step {i}: Move block {block} to {dest_str}")

def interactive_mode():
    """
    Interactive mode to run the Blocks World A* search.
    The user enters the initial and goal states as strings.
    Example format: A,B;C,D (two stacks: ['A', 'B'] and ['C', 'D'])
    """
    print("Blocks World A* Search")
    init_str = input("Enter initial state: ")
    goal_str = input("Enter goal state: ")

    def parse_state(s):
        state = []
        for stack_str in s.split(';'):
            if stack_str:
                state.append(stack_str.split(','))
        return state

    initial_state = parse_state(init_str)
    goal_state = parse_state(goal_str)
    problem = BlocksWorld(initial_state, goal_state)
    solution = problem.astar_search()
    display_solution(solution)

if __name__ == "__main__":
    interactive_mode()
