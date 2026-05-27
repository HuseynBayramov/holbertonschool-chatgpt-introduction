#!/usr/bin/python3

def print_board(board):
    """Lövhəni səliqəli şəkildə terminalda çap edir."""
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---" * 3)

def check_winner(board):
    """Qalib olub-olmadığını yoxlayır."""
    # Sətirləri yoxla
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Sütunları yoxla
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Diaqonalları yoxla
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """Lövhənin tamamilə dolub-dolmadığını (heç-heçəni) yoxlayır."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # İstifadəçi daxiletmələrinin (Input Validation) tam yoxlanılması
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid coordinates! Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter numbers only (0, 1, or 2).")
            continue

        # Xanaya gediş edilməsi
        if board[row][col] == " ":
            board[row][col] = player
            
            # Gedişdən dərhal sonra qələbəni yoxlayırıq (oyunçu dəyişmədən əvvəl)
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
                
            # Lövhənin dolmasını yoxlayırıq (heç-heçə)
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Növbəti oyunçuya keçid
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()#!/usr/bin/python3

def print_board(board):
    """Lövhəni səliqəli şəkildə terminalda çap edir."""
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---" * 3)

def check_winner(board):
    """Qalib olub-olmadığını yoxlayır."""
    # Sətirləri yoxla
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Sütunları yoxla
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Diaqonalları yoxla
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """Lövhənin tamamilə dolub-dolmadığını (heç-heçəni) yoxlayır."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # İstifadəçi daxiletmələrinin (Input Validation) tam yoxlanılması
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid coordinates! Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter numbers only (0, 1, or 2).")
            continue

        # Xanaya gediş edilməsi
        if board[row][col] == " ":
            board[row][col] = player
            
            # Gedişdən dərhal sonra qələbəni yoxlayırıq (oyunçu dəyişmədən əvvəl)
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
                
            # Lövhənin dolmasını yoxlayırıq (heç-heçə)
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Növbəti oyunçuya keçid
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
