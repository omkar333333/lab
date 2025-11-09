import math
def print_board(board):
    for i in range(3):
        row = board[3*i : 3*i+3]
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print()
def check_winner(board):
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a,b,c in lines:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "D"
    return None

def alphabeta(board, depth, alpha, beta, maximizing):
    winner = check_winner(board)

    if winner == "X":
        return 1, None
    if winner == "O":
        return -1, None
    if winner == "D":
        return 0, None
    if depth == 0:
        return 0, None

    if maximizing:
        best_value = -math.inf
        best_move = None

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                value, _ = alphabeta(board, depth-1, alpha, beta, False)
                board[i] = " "
                if value > best_value:
                    best_value = value
                    best_move = i
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    break
        return best_value, best_move

    else:
        best_value = math.inf
        best_move = None

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                value, _ = alphabeta(board, depth-1, alpha, beta, True)
                board[i] = " "
                if value < best_value:
                    best_value = value
                    best_move = i
                beta = min(beta, best_value)
                if alpha >= beta:
                    break
        return best_value, best_move
def play():
    board = [" "] * 9
    print("Tic-Tac-Toe!")
    print("You are O. AI is X.\n")
    print_board(board)

    while True:
        print("AI thinking...")
        _, move = alphabeta(board, depth=9, alpha=-math.inf, beta=math.inf, maximizing=True)
        board[move] = "X"
        print("\nAI moves:")
        print_board(board)

        if check_winner(board) is not None:
            break
        while True:
            try:
                user = int(input("Choose your spot (0-8): "))
                if user in range(9) and board[user] == " ":
                    board[user] = "O"
                    break
                else:
                    print("Invalid move, try again!")
            except ValueError:
                print("Please enter a number!")

        print("\nYour move:")
        print_board(board)

        if check_winner(board) is not None:
            break

    result = check_winner(board)
    if result == "X":
        print("AI wins!")
    elif result == "O":
        print("You win!")
    else:
        print("It's a draw!")
play()
