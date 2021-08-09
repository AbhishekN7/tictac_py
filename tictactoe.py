import random
import time

#game board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

#if game is still going
game_still_going=True

#Who won or Tie?
winner=None

#Who's turn is it
current_player="X"



def disp_board():
    print(board[0]+" | " + board[1]+" | "+ board[2])
    print(board[3]+" | " + board[4]+" | "+ board[5])
    print(board[6]+" | " + board[7]+" | "+ board[8])


def play_game():
    
    #display the initial board
    disp_board()
    
    while game_still_going:
        #handle a single turn of a player
        handle_turn(current_player)
        
        #check if the game has ended
        check_if_game_over()
        
        #Flip to the other player
        flip_player()
        
    #The game has ended
    if winner=="X" or winner=="O":
        print(winner+" Won")
    elif winner==None:
        print("Tie")
        

#handle a single turn    
def handle_turn(player):
    position= input("Choose a position from 1-9: ")
    position=int(position)-1
    
    board[position]="X"
    disp_board()
    
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
def check_for_winner():
    #set up global variables
    global winner
    #check rows
    row_winner= check_rows()
    #check columns
    column_winner= check_columns()
    #check diagnals
    diagonal_winner= check_diagonals()
    
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        #There was no winner
        winner = None
    return

def check_rows():
    #setup global variables
    global game_still_going
    row_1 = board[0] == board[1] == board[2] !="-"
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"
    
    if row_1 or row_2 or row_3:
        game_still_going=False
    
    
    #Return winner x or o
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] !="-"
    column_2 = board[1] == board[4] == board[7] !="-"
    column_3 = board[2] == board[5] == board[8] !="-"
    
    if column_1 or column_2 or column_3:
        game_still_going=False
    
    
    #Return winner x or o
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

    

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] !="-"
    diagonal_2 = board[2] == board[4] == board[6] !="-"
    
    if diagonal_1 or diagonal_2: 
        game_still_going=False
    
    
    #Return winner x or o
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return



def check_if_tie():
    return

def flip_player():
    return

play_game()

    
    
    
    
    
    
    
    
    
    
    


