# Creating a TicTacToe application via Python
# Task: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/04-Milestone%20Project%20-%201/02-Milestone%20Project%201%20-%20Walkthrough%20Steps%20Workbook.ipynb

#player1 = input("Do you want to be X or O?")
#print(player1)
import random

#board_state = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#test_state = [' ',' ','X',' ','X','X','X',' ','X']

def display_board(board):
    print("   |   |   ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + "  ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + "  ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + "  ")
    print("   |   |   ")    

def player_input():
    player_option=input("Would you like to be X or O?")
    # Think about using while loops to continually ask until you get a correct answer
    #while player_choice != 'X' or player_choice != 'O':
    #    player_input()
    return player_option

def place_marker(board,marker,position):
    board[position] = marker
    return board

def win_check(board,mark):
    # Check if the horizontals are a win
    if board[0] == mark and board [1] == mark and board[2] == mark:
        return True
    elif board[3] == mark and board [4] == mark and board[5] == mark:
        return True
    elif board[6] == mark and board [7] == mark and board[7] == mark:
        return True
    # Check if the verticals are a win
    elif board[6] == mark and board [3] == mark and board[0] == mark:
        return True
    elif board[7] == mark and board [4] == mark and board[1] == mark:
        return True
    elif board[8] == mark and board [5] == mark and board[2] == mark:
        return True
    # Check if the diagonals are a win
    elif board[6] == mark and board [4] == mark and board[2] == mark:
        return True
    elif board[8] == mark and board [4] == mark and board[0] == mark:
        return True
    else:
        return False

def choose_first():
    first_player = random.randint(0,1)
    if first_player == 0:
        return 'Player 1 has the first move.'
    else:
        return 'Player 2 has the first move.'

def space_check(board,position):
    if board[position] == ' ':
        return True
    else:
        print('That space is taken!')
        return False

def full_board_check(board):
    for pos in (0, len(board) - 1):
        if board[pos] == ' ':
            return False
    return True

def player_choice(board):
    player_move = int(input("What position would you like to play next?"))
    player_move -= 1
    if space_check(board,player_move):
        return player_move
    else:
        player_choice(board)
    
def replay():
    answer = input("Do you want to play again?(Yes/No)")
    if answer.lower() == 'yes':
        return True
    else:
        return False
    
# Set up the game to determine who goes first and what marker each player is using. 
print('Welcome to Tic Tac Toe!')
player_one = player_input()
if player_one == 'X':
    player_two = 'O'
else:
    player_two ='X'
print('Player One selected ' + player_one + '. Player Two will be ' + player_two + '.')
first_player = choose_first()
print('We\'ve randomly chosen and ' + first_player)
input('Let\'s Begin!(Press Enter)')
board_state = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(board_state)


# The main game function
game_on = True
while game_on:
    # First player's turn
    move = player_choice(board_state)
    place_marker(board_state,player_one,move)
    display_board(board_state)
    if(full_board_check(board_state)):
        print("The board is full.")
        game_on = False
        break
    if(win_check(board_state,player_one)):
        print("Congratulations, Player One wins!")
        game_on = False
        break

    # Second player's turn
    move = player_choice(board_state)
    place_marker(board_state,player_two,move)
    display_board(board_state)
    if(full_board_check(board_state)):
        print("The board is full.")
        game_on = False
        break
    if(win_check(board_state,player_one)):
        print("Congratulations, Player Two wins!")
        game_on = False
        break
    #game_on = False


#print(win_check(test_state,'X'))
#print(player_input())x
#place_marker(board_state,'X',7)
#display_board(test_state)