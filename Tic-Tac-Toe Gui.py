import os    
import time    
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   

Win = 1    
Draw = -1    
Running = 0    
Stop = 1    

Game = Running    
Mark = 'X'    

def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    

def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False     
    
def check_win(board, player):
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)):
        return True
    else:
        return False

def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]
    while True:
        print_board(board)
        print("Player", current_player)
        move = int(input("Enter a number from 1-9: "))
        if board[move-1] != " ":
            print("That move is already taken. Try again.")
            continue
        board[move-1] = current_player
        if check_win(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break
        if " " not in board:
            print_board(board)
            print("Tie game!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

if __name__ == "__main__":
    main()
