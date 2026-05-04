import copy
class ChessPiece:
    def __init__(self,name,position,color):
        self.name=name
        self.position=position
        self.color=color
    
    def display(self):
        return f"{self.color} {self.name} is at {self.position}"
    def clone(self):
        return copy.deepcopy(self)
        # return ChessPiece(self.name,self.position,self.color)  #also use that method 
        
    
class ChessBoard:
    def __init__(self):
        self.pieces=[]
    def addpiece(self,piece:ChessPiece):
        self.pieces.append(piece)
    def displayboard(self):
        print("\nBoard State")
        for piece in self.pieces:
            print(f"{piece.display()}")  
    def clone_board(self):
        return copy.deepcopy(self)
       
            
piece1=ChessPiece("king","c3","Black")
piece2=ChessPiece("Queen","d3","Black")
piece3=ChessPiece("Pawn","a2","white")
piece4=ChessPiece("Horse","e3","white")

chess_board=ChessBoard()
chess_board.addpiece(piece1)
chess_board.addpiece(piece2)
chess_board.addpiece(piece3)
chess_board.addpiece(piece4)

chess_board.displayboard()

print("------------------------------")

 
# instead of manually we can literally clone the object 
new_chess_board=chess_board.clone_board()
# new_chess_board.displayboard()

piece5=ChessPiece("Bishop","e6","black")
new_chess_board.addpiece(piece5)
new_chess_board.displayboard()
   
   