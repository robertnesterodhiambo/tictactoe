# board
board =  ["_","_","_",
          "_","_","_",
          "_","_","_"]
def display_board():
    print(" | " + board[0] + " | ", board[1] + " | ", board[2] + " | ")
    print(" | " + board[3] + " | ", board[4] + " | ", board[5] + " | ")
    print(" | " + board[6] + " | ", board[7] + " | ", board[8] + " | ")

#handle turns

def handle_turn():
    # starts by getting postition
    position = input("choose a position from 1 - 9 ")

def play_game():
    # display initial board
    display_board()
    handle_turn()


play_game()

#display board
# play game
# handle turns 
# check win
 # check rows
 # chcek columns
 # check diagonal
# chcek tie
#flip player 