import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for winner
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if all([board[i] == player for i in combo]):
            return True
    return False

# Check for draw
def is_draw(board):
    return ' ' not in board

# Get available moves
def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):  # AI is 'O'
        return 10 - depth
    if check_winner(board, 'X'):  # Human is 'X'
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(best_score, score)
        return best_score

# AI Move using Minimax
def ai_move():
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

# Human move
def human_move():
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Invalid move. Try again.")
        human_move()

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human's move
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI's move
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
