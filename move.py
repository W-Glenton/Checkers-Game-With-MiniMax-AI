from piece import Piece
#from board import Board
class Move:
    def __init__ (self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def getCoOrds(self):#return coords (only used in debugging)
        return self.x1,self.y1,self.x2,self.y2

    def skipsearch(self,state,player,factor,currentpos,endpos):#a depth first search for valid routes that involve taking opposing player piece
        found = False
        if (0>currentpos[0]or 7<currentpos[0])or(0>currentpos[1]or 7<currentpos[1]):
            return False,[],"no valid path"
        if currentpos==endpos:
            return True, []," "
        else:
            leftshift = [currentpos[0]+(2*factor),currentpos[1]-2]
            rightshift= [currentpos[0]+(2*factor),currentpos[1]+2]
            #print(currentpos)
            if min(currentpos[0]+(1*factor), currentpos[1]-1)>-1 and max(currentpos[0]+(1*factor), currentpos[1]-1)<8:#traverse left
                if type(state[currentpos[0]+(1*factor)][currentpos[1]-1])!=type("  "):
                    if state[currentpos[0]+(1*factor)][currentpos[1]-1].getPlayer()!=player:
                        path,skips,string =self.skipsearch(state,player,factor,leftshift,endpos)#recurse for multi leg moves
                        if path:
                            skips.append([currentpos[0]+(1*factor),currentpos[1]-1])
                            return True, skips, "  "
            if min(currentpos[0]+(1*factor), currentpos[1]+1)>-1 and max(currentpos[0]+(1*factor), currentpos[1]+1)<8:#traverse right
                if type(state[currentpos[0]+(1*factor)][currentpos[1]+1])!=type("  "):
                    if state[currentpos[0]+(1*factor)][currentpos[1]+1].getPlayer()!=player:
                        path,skips,string=self.skipsearch(state,player,factor,rightshift,endpos)#recurse for multi leg moves
                        if path:
                            skips.append([[currentpos[0]+(1*factor),currentpos[1]+1]])
                            return True, skips, "  "
                
        return False,[],"no valid path"

    
    def pathSearch(self,state,player):#determines if the move requires taking opposing pieces
        currentpos=[self.x1,self.y1]
        endpos=[self.x2,self.y2]
        reached=False
        if player == "b":#factor regulates the direction up or down the board the piece can move
            factor=1
        else:
            factor=-1
        if state[self.x1][self.y1].getKing():#if the player is a king, the factor depends on the direction of the move itself
            if currentpos[0]<endpos[0]:
                factor=1
            else:
                factor=-1
        #print(self.y2,self.y1+(1*factor), self.x2,self.x1+1,self.x2 , self.x1-1)
        if (endpos[0]==currentpos[0]+(1*factor))and(endpos[1]==currentpos[1]+1 or endpos[1] == currentpos[1]-1):
            return True,[]," "
        else:
            #print(state,player,factor,currentpos,endpos)
            reached,skips,string= self.skipsearch(state,player,factor,currentpos,endpos)#enter search for moves that involve skipping a piece
            return reached,skips,string
    
    def validate(self, player, board):
        state=board.getState()
        valid=True
        x1=self.x1
        y1=self.y1
        x2=self.x2
        y2=self.y2

        if min(x1,x2,y1,y2)<0 or max(x1,x2,y1,y2)>8:#ensure entered coords are within the boards dimensions
            return False,[],"must be within the dimensions of the board"
        if state[x1][y1]=="  " or state[x1][y1]=="⬛": #start must not be empty, must be a playable square

            return False,[],"start point must not be empty, or be a white square"
        elif state[x2][y2]!="  ": #end point must be empty

            return False,[],"Destination must be an empty square"
        elif state[x1][y1].getPlayer()!=player:#player cannot move other players piece

            return False,[], "can't move other player's piece!"

        else:#if above tests are passed, search for path
            valid,skips,err = self.pathSearch(state,player)

            return valid,skips,err
    
  
    


    
    def execute(self, board,skips):#executes a move when given a board state
        state=board.getState()
        #print(state)
        for skip in skips:#remove skipped pieces from the board
            #print (skip)
            if type(skip[0])==type([1,2]):
                skip=skip[0]
                if type(state[skip[0]][skip[1]])!=type(" "):
                    if state[skip[0]][skip[1]].getKing():#if piece takes a king, the piece is crowned instantly
                        state[self.x1][self.y1].crown()
                    state[skip[0]][skip[1]] = "  "
            else:
                if type(state[skip[0]][skip[1]])!=type(" "):
                    if state[skip[0]][skip[1]].getKing():
                        state[self.x1][self.y1].crown()
                    state[skip[0]][skip[1]] = "  "
                
        state[self.x2][self.y2] = state[self.x1][self.y1]#move player to destination
        state[self.x1][self.y1]="  "#clear starting square
        #print(state)
        if self.x2==0 and state[self.x2][self.y2].getPlayer()=="w":#if piece reaches king baseline, crown it
            state[self.x2][self.y2].crown()
        if self.x2==7 and state[self.x2][self.y2].getPlayer()=="b":
            state[self.x2][self.y2].crown()
        return state
    def translateCoOrds(self):#turns input coords into correct format to index board state
        x1=self.x1
        x2=self.x2
        y1=self.y1
        y2=self.y2
        self.y1=x1-1
        self.y2=x2-1
        self.x1=(y1*-1)+8
        self.x2=(y2*-1)+8
        
