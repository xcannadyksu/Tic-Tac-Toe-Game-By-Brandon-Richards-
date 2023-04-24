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
   
  def winning_condition(user):
    for i in range(0, len(bord)):
        if (
            (bord[0] == user and bord[1] == user and bord[2] == user)
            or (bord[0] == user and bord[3] == user and bord[6] == user)
            or (bord[2] == user and bord[5] == user and bord[8] == user)
            or (bord[6] == user and bord[7] == user and bord[8] == user)
            or (bord[3] == user and bord[4] == user and bord[5] == user)
            or (bord[1] == user and bord[4] == user and bord[7] == user)
            or (bord[0] == user and bord[4] == user and bord[8] == user)
            or (bord[2] == user and bord[4] == user and bord[6] == user)  
    
print("Tic-Tac-Toe Game")    
print("Player 1 [X] --- Player 2 [O]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3)    
while(Game == Running):    
    os.system('cls')    
    DrawBoard()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(CheckPosition(choice)):    
        board[choice] = Mark    
        player+=1    
        CheckWin()    
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won") 
