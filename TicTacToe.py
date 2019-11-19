# Creating a TicTacToe application via Python

#player1 = input("Do you want to be X or O?")
#print(player1)
import random

#board_state = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
test_state = [' ',' ','X',' ','X','X','X',' ','X']

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
        return False

def full_board_check(board):
    for pos in (0, len(board) - 1):
        if board[pos] == ' ':
            return False
    return True

def player_choice(board):
    player_move = input("What position would you like to play next?")
    if space_check(board,player_move):
        return player_move
    else:
        player_choice(board)
    



#print(win_check(test_state,'X'))
#print(player_input())
#place_marker(board_state,'X',7)
display_board(test_state)