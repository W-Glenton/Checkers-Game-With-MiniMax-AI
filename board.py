from piece import Piece
from move import Move
class Board():

    def __init__ (self, dimension):
        initstate =[]
        for i in range(0,dimension):
            initstate.append([])
            for j in range(0,dimension):
                if (i%2==0 and j%2 == 0)or(i%2==1 and j%2 == 1) :#determine black squares and white squares
                    initstate[i].append("⬛")
                else:
                    initstate[i].append("  ")
        self.state=initstate
        self.dimension = dimension
    def getState(self):#return 2d array representing the board at current state of play
        return self.state
    
    def display(self): #print the board in ascii/unicode characters

        for i in range(0,len(self.state)):
            tempstring=str(self.dimension - i)#string for horizontal display
            for j in self.state[i]:
                if j != "  " and j!="⬛":
                    tempstring=tempstring+j.getChar()
                else:
                    tempstring=tempstring + j
            print (tempstring+"")
        print("  1 2 3 4 5 6 7 8")#print x axis chars

    def populate(self):#set board to regular state for beginning a game
        for i in range(0,self.dimension):
            for j in range(0,self.dimension):
                if i < 3 and self.state[i][j]=="  ":#set black pieces
                    self.state[i][j]=Piece("b", False)
                if i>4 and self.state[i][j]=="  ":#set white pieces
                    self.state[i][j]=Piece("w", False)
    def piecesLeft(self,player):#how many pieces of a given player remain?
        string="string"
        count=0
        debugcount=0
        for i in self.state:
            for j in i:
                debugcount+=1
                if j!="  " and j!= "⬛":
                    if j.getPlayer == player:
                        count=count+1
        print(count)
        return count
    def score(self):#score evaluation
        bcount=0#initialise score counts
        wcount=0
        for i in self.state:#iterate through whole board state
            for j in i:
                if type(j)!=type(" "):#if not a string (i.e. if given square is a piece)
                    if j.getPlayer()=="w":#if piece is white
                        if j.getKing():#if piece is a king
                            wcount=wcount+1.5
                        else:
                            wcount=wcount+1
                    elif j.getPlayer()=="b":#if piece is black
                        if j.getKing():#if piece is a black king
                            bcount=bcount+1.5
                        else:
                            bcount=bcount+1
        count = wcount-bcount
        return count
    def gameOver(self):#returns true if one player has no pieces left
        bcount=0
        wcount=0
        for i in range(0,self.dimension):
            for j in range(0,self.dimension):
                if self.state[i][j]!="  " and self.state[i][j]!="⬛":
                    if self.state[i][j].getPlayer()=="w":
                        wcount=wcount+1
                    else:
                        bcount=bcount+1
        if wcount==0:
            return "b"
        elif bcount==0:
            return "w"
        else:
            return 0
    def getvalidmoves(self,player):#finds every possible valid move for a give player
        moves=[]
        for i in range(0,self.dimension):#search for players pieces
            for j in range(0,self.dimension):
                if self.state[i][j]!="  " and self.state[i][j]!="⬛":
                    if self.state[i][j].getPlayer()==player:
                        for k in range(0,self.dimension):#generate a move starting at the pieces position
                            for l in range(0,self.dimension):
                                move=Move(i,j,k,l)
                                valid,skips,string=move.validate(player,self)#check move is valid
                                if valid:
                                    moves.append([move,skips])#add valid moves to valid moves array
        return moves



            
#"⬜""◯""⬤""
