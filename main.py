#
#: board
# display board
#play the game
#handle turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player a to b


game_on = True
winner = None
playerName ="A"
#creating a board
board =["-", "-", "-", 
        "-", "-", "-", 
        "-", "-", "-", ]

#display the board
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

def turn_player(playerName):
    print(playerName+"'s turn")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("invalid input by user, please try again")
            position = input("Choose a position from 1-9: ")
        position = int(position)-1
        
        if board[position] == "-":
            valid = True
        else:
            print("This is already filled up")
    board[position] = playerName
    display_board()

def is_game_over():
    is_win()
    is_tie()

def is_win():
    global winner
    #check by row
    row = check_row()
    #check by column
    column = check_column()
    #check by diagonals
    diagonals = check_diagonals()

    if row:
        #win
        winner =row
    elif column:
        #win
        winner =column
    elif diagonals:
        #win
        winner =diagonals
    else:
        #tie
        winner = None

    return

def is_tie(): 
    global game_on
    if "-" not in board:
        game_on = False
    return

def check_row():
    global game_on
    rows1 = board[0] == board[1] == board[2] != "-"
    rows2 = board[3] == board[4] == board[5] != "-"
    rows3 = board[6] == board[7] == board[8] != "-"
    if rows1 or rows2 or rows3:
        game_on = False
    #Return the winner
    if rows1:
        return board[0]
    elif rows2:
        return board[3]
    elif rows3:
        return board[6]
    return

def check_column():
    global game_on
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        game_on = False
    #Return the winner
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diagonals():
    global game_on
    diagonals1 = board[0] == board[4] == board[8] != "-"
    #diagonals2 = board[1] == board[4] == board[7] != "-"
    diagonals3 = board[2] == board[4] == board[6] != "-"
    if diagonals1 or  diagonals3:
        game_on = False
    #Return the winner
    if diagonals1:
        return board[0]
   # elif diagonals2:
    #     return board[1]
    elif diagonals3:
        return board[6]
    return

def flip_player():
    #accessing global variable
    global playerName

    #if current player is x change to 0
    if playerName == "A":
        playerName = "B"
    #if current player is 0 change to X
    elif playerName=="B":
        playerName ="A"
    return 

def play_game():
    
    #display the board
    display_board()
    while game_on:

        #handle turn
        turn_player(playerName)
        is_game_over()
        #turn to another player
        flip_player()
    #game ended
    if winner=="X" or winner=="O":
        print(winner+" has won")
    elif winner==None:
        print("game tie")


play_game()