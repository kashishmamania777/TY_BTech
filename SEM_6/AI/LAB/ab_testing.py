import copy

# Constants
EMPTY = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'
DRAW = 'D'

def opponent(player):
    return PLAYER_O if player == PLAYER_X else PLAYER_X

class SmallBoard:
    def __init__(self):
        self.cells = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.winner = None

    def make_move(self, row, col, player):
        if self.cells[row][col] != EMPTY or self.winner is not None:
            return False
        self.cells[row][col] = player
        self.check_winner()
        return True

    def check_winner(self):
        lines = []
        # Rows, columns, diagonals
        lines.extend(self.cells)
        lines.extend([[self.cells[r][c] for r in range(3)] for c in range(3)])
        lines.append([self.cells[i][i] for i in range(3)])
        lines.append([self.cells[i][2 - i] for i in range(3)])
        for line in lines:
            if line[0] != EMPTY and all(cell == line[0] for cell in line):
                self.winner = line[0]
                return
        if all(self.cells[r][c] != EMPTY for r in range(3) for c in range(3)):
            self.winner = DRAW

    def is_full(self):
        return all(self.cells[r][c] != EMPTY for r in range(3) for c in range(3))

    def get_legal_moves(self):
        if self.winner is not None:
            return []
        return [(r, c) for r in range(3) for c in range(3) if self.cells[r][c] == EMPTY]

class UltimateTicTacToe:
    def __init__(self):
        self.boards = [[SmallBoard() for _ in range(3)] for _ in range(3)]
        self.board_winners = [[None for _ in range(3)] for _ in range(3)]
        self.global_winner = None

    def copy(self):
        new_game = UltimateTicTacToe()
        new_game.boards = [[copy.deepcopy(self.boards[r][c]) for c in range(3)] for r in range(3)]
        new_game.board_winners = [row[:] for row in self.board_winners]
        new_game.global_winner = self.global_winner
        return new_game

    def make_move(self, board_row, board_col, cell_row, cell_col, player):
        board = self.boards[board_row][board_col]
        if not board.make_move(cell_row, cell_col, player):
            return False
        self.board_winners[board_row][board_col] = board.winner
        self.check_global_winner()
        return True

    def check_global_winner(self):
        lines = []
        lines.extend(self.board_winners)
        lines.extend([[self.board_winners[r][c] for r in range(3)] for c in range(3)])
        lines.append([self.board_winners[i][i] for i in range(3)])
        lines.append([self.board_winners[i][2 - i] for i in range(3)])
        for line in lines:
            if line[0] is not None and line[0] != DRAW and all(cell == line[0] for cell in line):
                self.global_winner = line[0]
                return
        if all(self.board_winners[r][c] is not None for r in range(3) for c in range(3)):
            self.global_winner = DRAW

    def get_legal_moves(self, next_board):
        # next_board: (row, col) or None
        moves = []
        if self.global_winner is not None:
            return moves
        if next_board is not None:
            r, c = next_board
            if self.boards[r][c].winner is None:
                for cell in self.boards[r][c].get_legal_moves():
                    moves.append((r, c, cell[0], cell[1]))
                if moves:
                    return moves
        # If forced board is won/full, can play anywhere legal
        for br in range(3):
            for bc in range(3):
                if self.boards[br][bc].winner is None:
                    for cell in self.boards[br][bc].get_legal_moves():
                        moves.append((br, bc, cell[0], cell[1]))
        return moves

def evaluate(game, player):
    # Simple evaluation: +1000 for win, -1000 for loss, +10 for each small board won, -10 for each lost
    if game.global_winner == player:
        return 1000
    if game.global_winner == opponent(player):
        return -1000
    score = 0
    for r in range(3):
        for c in range(3):
            winner = game.board_winners[r][c]
            if winner == player:
                score += 10
            elif winner == opponent(player):
                score -= 10
    return score

def minimax(game, depth, alpha, beta, maximizing_player, player, next_board):
    if depth == 0 or game.global_winner is not None:
        return evaluate(game, player), None
    moves = game.get_legal_moves(next_board)
    if not moves:
        return evaluate(game, player), None
    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            new_game = game.copy()
            new_game.make_move(*move, player)
            next_br, next_bc = move[2], move[3]
            if new_game.boards[next_br][next_bc].winner is not None:
                next_forced = None
            else:
                next_forced = (next_br, next_bc)
            eval, _ = minimax(new_game, depth-1, alpha, beta, False, player, next_forced)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            new_game = game.copy()
            new_game.make_move(*move, opponent(player))
            next_br, next_bc = move[2], move[3]
            if new_game.boards[next_br][next_bc].winner is not None:
                next_forced = None
            else:
                next_forced = (next_br, next_bc)
            eval, _ = minimax(new_game, depth-1, alpha, beta, True, player, next_forced)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

import copy
import random

# --- (All your previous code here: SmallBoard, UltimateTicTacToe, etc.) ---

# ... (Paste all your code above up to the minimax function) ...

def random_opponent_move(game, next_board):
    moves = game.get_legal_moves(next_board)
    if not moves:
        return None
    return random.choice(moves)

def print_board(game):
    """Pretty print the current state of the ultimate board."""
    def cell_str(cell):
        return cell if cell != EMPTY else ' '
    for br in range(3):
        for r in range(3):
            row = []
            for bc in range(3):
                row.extend([cell_str(game.boards[br][bc].cells[r][c]) for c in range(3)])
                if bc < 2:
                    row.append('|')
            print(' '.join(row))
        if br < 2:
            print('-' * 17)

if __name__ == "__main__":
    game = UltimateTicTacToe()
    player = PLAYER_X
    next_board = None  # No constraint for first move
    depth = 3  # AI search depth

    turn = 0
    while game.global_winner is None:
        print(f"\nTurn {turn+1}:")
        print_board(game)
        if player == PLAYER_X:
            # AI's turn
            score, move = minimax(game, depth, float('-inf'), float('inf'), True, PLAYER_X, next_board)
            print(f"AI ({PLAYER_X}) chooses: {move} (score: {score})")
        else:
            # Random opponent's turn
            move = random_opponent_move(game, next_board)
            print(f"Opponent ({PLAYER_O}) chooses: {move}")
        if move is None:
            print("No moves left!")
            break
        game.make_move(*move, player)
        # Determine next forced board
        next_br, next_bc = move[2], move[3]
        if game.boards[next_br][next_bc].winner is not None:
            next_board = None
        else:
            next_board = (next_br, next_bc)
        # Switch player
        player = opponent(player)
        turn += 1

    print("\nFinal board:")
    print_board(game)
    print("\nGame Over!")
    if game.global_winner == DRAW:
        print("It's a draw!")
    else:
        print(f"Winner: {game.global_winner}")


# Example usage:
if __name__ == "__main__":
    game = UltimateTicTacToe()
    player = PLAYER_X
    next_board = None  # No constraint for first move
    depth = 3  # Increase for stronger AI, decrease for faster response

    score, move = minimax(game, depth, float('-inf'), float('inf'), True, player, next_board)
    print("Best move for", player, "is:", move, "with score", score)
