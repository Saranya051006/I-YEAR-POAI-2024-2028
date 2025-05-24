PLAYER_X = 1
PLAYER_O = -1
EMPTY = 0

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return 0

def is_moves_left(board):
    return any(EMPTY in row for row in board)

def minimax(board, is_maximizing):
    score = evaluate(board)
    if score != 0:
        return score
    if not is_moves_left(board):
        return 0

    best = -float('inf') if is_maximizing else float('inf')
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X if is_maximizing else PLAYER_O
                val = minimax(board, not is_maximizing)
                board[row][col] = EMPTY
                best = max(best, val) if is_maximizing else min(best, val)
    return best

def find_best_move(board):
    best_val = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                move_val = minimax(board, False)
                board[row][col] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    best_move = (row, col)
    return best_move

def print_board(board):
    symbols = {PLAYER_X: "X", PLAYER_O: "O", EMPTY: "."}
    for row in board:
        print(" ".join(symbols[cell] for cell in row))

# Example game
board = [
    [PLAYER_X, PLAYER_O, PLAYER_X],
    [PLAYER_O, PLAYER_X, EMPTY],
    [EMPTY, PLAYER_O, PLAYER_X]
]

print("Current Board:")
print_board(board)

move = find_best_move(board)
print(f"\nBest Move: {move}")
board[move[0]][move[1]] = PLAYER_X

print("\nBoard after best move:")
print_board(board)
