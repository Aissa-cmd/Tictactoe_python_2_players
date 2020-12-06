# _______  ___    ______    _______   _____     ______    _______   _____     _____
#    |      |    |             |     |     |   |             |     |     |   |
#    |      |    |             |     |-----|   |             |     |     |   |----
#    |     _|_   |______       |     |     |   |______       |     |_____|   |_____

# ---------------------------------- 2 Players -------------------------------------

# --------------global variables------------------
# the board
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

# the player either "X" or "O"
current_player = "X"

# the winner
winner = None

# game still going if it's True to keep playing or if it's False to stop playing
game_still_going = True


# -------------dispalying the board----------------
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#--------------Ask the user for a position to put "X" or "O"-----------------
def hundle_turn(player):
    print(f"This is {player}'s turn.")
    position = input("Choose a position from 1-9: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid value. Choose a position from 1-9: ")
    position = int(position) - 1
    while board[position] != "-":
        position = input("You can't go there. Choose a position from 1-9: ")
        position = int(position) - 1
    board[position] = player
    display_board()


#----------------Check if there is a winner to stop playing or if there isn't to keep playing----------------
# check if there is a winner in rows
def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    

# chck if there is a winner in columns
def check_column():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


#check if there is a winner in diagonals
def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]


# check if there is a winner in the game
def check_for_winner():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    

# check if all the position in the board are full an non of the players won
def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


# check if game is over either one of the players won or there is a tie
def check_is_game_over():
    check_for_winner()
    check_for_tie()

#-----------------To flip between players turn on turn for "X" and another for "O"----------------
def flip_turn():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"



#------------------The function that generate the game-----------------
def play_game():
    display_board()
    while game_still_going:
        hundle_turn(current_player)
        check_is_game_over()
        flip_turn()
    if winner == "X" or winner == "O":
        print("Player " + winner + " won.")
        print()
        play_again()
        print()
    elif winner == None:
        print("Tie.")
        print()
        play_again()
        print()


# this function asks the player if he wants to play again
def play_again():
    global board
    global current_player
    global winner
    global game_still_going
    print("Do you want to play again (Yes/No)")
    answer = input(">>> ").upper()
    if answer == "YES":
        board = [
                "-", "-", "-",
                "-", "-", "-",
                 "-", "-", "-"
                ]
        current_player = "X"
        winner = None
        game_still_going = True
        play_game()
    elif answer == "NO":
        return


play_game()
