def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")
    print("\n")

def check_winner(board, player):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

def is_board_full(board):
    return ' ' not in board

def minimax(board, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    board = [' '] * 9
    print("Tic-Tac-Toe AI (You: X, AI: O)")
    print("Positions: 1-9 (left to right, top to bottom)")
    
    while True:
        print_board(board)
        
        move = input("Your move (1-9): ").strip()
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input! Enter 1-9.")
            continue
        
        pos = int(move) - 1
        if board[pos] != ' ':
            print("Position taken! Try again.")
            continue
        
        board[pos] = 'X'
        
        if check_winner(board, 'X'):
            print_board(board)
            print("You win! Impressive!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        ai_pos = ai_move(board)
        board[ai_pos] = 'O'
        print(f"AI plays position {ai_pos + 1}")
        
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
  
