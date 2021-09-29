class Piece():
    def __init__(self,player,king):
        self.player=player
        self.king=king
        if player == "b":#set player characters and characters for display
            self.char="⬤"
        elif player =="w":
            self.char = "◯"
        else:
            self.char = "broken"

    def getPlayer(self): #get player 
        return self.player
    def getKing(self):#return king status
        return self.king
    def getChar(self):#get character for display
        return self.char
    def crown(self):#converts player to king
        self.king =True
