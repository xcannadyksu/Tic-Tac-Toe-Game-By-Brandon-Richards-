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
    
def CheckWin():    
    global Game  
  if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win  
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win   
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win   
   elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running   



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
