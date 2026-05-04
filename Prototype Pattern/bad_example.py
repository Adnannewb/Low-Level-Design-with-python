class ChessPiece:
    def __init__(self,name,position,color):
        self.name=name
        self.position=position
        self.color=color
    
    def display(self):
        return f"{self.color} {self.name} is at {self.position}"
    
class ChessBoard:
    def __init__(self):
        self.pieces=[]
    def addpiece(self,piece:ChessPiece):
        self.pieces.append(piece)
    def displayboard(self):
        print("\nBoard State")
        for piece in self.pieces:
            print(f"{piece.display()}")     
            
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

#manually creating new board and adding new pieces and postions.
#this is quite time consuming and errorful . 
new_chess_board=ChessBoard()
new_chess_board.addpiece(piece1)
new_chess_board.addpiece(piece2)
new_chess_board.addpiece(piece3)
new_chess_board.addpiece(piece4)

new_chess_board.displayboard()

   
   