from board import Board
from piece import Piece
from move import Move
from copy import deepcopy
import random
board=Board(8)



def minimax(board,depth,alpha,beta,maximum):
    boardcopy=deepcopy(board)#copy board to avoid changing game board object
    if depth==0 or board.gameOver():#base case
        return board.score(),0
    if maximum:
        bestmove=[]
        val=float('-inf')
        for move in boardcopy.getvalidmoves("w"):#get all valid moves for white
            boardcopy=deepcopy(board)
            move[0].execute(boardcopy,move[1])
            value,prevailingmove=minimax(boardcopy,depth-1,True,True,False)#recurse for next set of moves
            if val ==value:#if values are the same, pick a random one so game isn't deterministic
                i=random.randint(0,1)
                if i == 0:
                    bestmove=move[0]
            if val<value:#if value greater, return the value
                val=value
                alpha=value
                bestmove=move[0]
            if alpha >= beta:
                break
        return val,bestmove
    else:
        bestmove=[]
        val=float('inf')
        for move in boardcopy.getvalidmoves("b"):#get all valid moves for black
            boardcopy=deepcopy(board)
            move[0].execute(boardcopy,move[1])
            value,prevailingmove=minimax(boardcopy,depth-1,True,True,True)
            if val ==value:#if values are the same, pick a random one so game isn't deterministic
                i=random.randint(0,1)
                if i == 0:
                    bestmove=move[0]
            if val>value:#if value greater, return the value
                val=value
                beta=value
                bestmove=move[0]
            if beta<=alpha:
                break
                
        return val,bestmove
                
new = Board(8)#initialise new board
new.populate()
new.display()

depth=0
ease=int(input("Select difficulty:\n1.Easy\n2.Medium\n3.Hard\nEnter the number of your choice:  "))#select difficulty
if ease == 1:
    depth=2
elif ease == 2:
    depth=5
elif ease == 3:
    depth =7
else:
    print("restart program and enter valid number")


game=True
while game and depth:#game loop
    correct=False
    while correct==False:#loop in case of invalid input
        x1=int(input("X1: "))
        y1=int(input("y1: "))
        x2=int(input("X2: "))
        y2=int(input("Y1: "))
        move=Move(x1,y1,x2,y2)
        move.translateCoOrds()
        valid,skips,string =move.validate("w",new)
        if valid:
            correct=True
        else:
            print(string)#print reason why not valid input
    if valid:
        move.execute(new,skips)#execute player move
        new.display()
        print(new.score())
    end=new.gameOver()#if game over end loop
    if end=="b":
        print("Black wins!")
        break
    elif end=="w":
        print("White wins!")
        break
            
    else:
        print(string)
    val,move=minimax(new,depth,float('-inf'),float('inf'),False)#AI search for best move
    valid,skips,string=move.validate("b",new)#validate move and get skips
    if valid:#if valid execute
        move.execute(new,skips)
    else:
        print(string)
    new.display()#display board after AI move
    print(new.score())
    end=new.gameOver()#if game over break out of loop
    if end=="b":
        print("Black wins!")
        break
    elif end=="w":
        print("White wins!")
        break
        

#I made the below code out of interest, to run two minimax AIs against each other
"""for i in range(0,100):
    
    val,move=minimax(new,5,float('-inf'),float('inf'),False)
    if type(move)==type([]):
        break
    valid,skips,string=move.validate("b",new,False)
    if valid:
        move.execute(new,skips)
        print(new.score())
    else:
        print(string)
    new.display()
    val,move=minimax(new,5,float('-inf'),float('inf'),True)
    if type(move)==type([]):
        break
    valid,skips,string=move.validate("w",new,False)
    if valid:
        move.execute(new,skips)
        print(new.score())
    else:
        print(string)
    new.display()"""














    
