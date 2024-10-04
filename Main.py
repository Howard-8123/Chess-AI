from chess import *


def main():
    pass


def create_board():
    myboard = ChessBoard()
    # white side
    for x in range(0, 8):
        for y in range(0, 2):
            if y !=0:
                if x == 0 or x ==7:
                    piece = Rook((x,y), 0)
                elif x == 1 or x ==6:
                    piece = Knight((x,y), 0)
                elif x ==2 or x == 5:
                    piece = Bishop((x,y), 0)
                elif x == 3:
                    piece = Queen((x,y), 0)
                elif x == 4:
                    piece = King((x,y), 0)
            else:
                piece = Pawn((x, y), 0)
            myboard.change((x, y), piece)
        # Black side
        for y in range(6, 8):
            if y == 6:
                piece = Pawn((x, y), 1)
            else:
                if x == 0 or x ==7:
                    piece = Rook((x,y), 1)
                elif x == 1 or x ==6:
                    piece = Knight((x,y), 1)
                elif x ==2 or x == 5:
                    piece = Bishop((x,y), 1)
                elif x == 3:
                    piece = Queen((x,y), 1)
                elif x == 4:
                    piece = King((x,y), 1)
            myboard.change((x, y), piece)
    print(myboard.getboard())
    for piece in myboard.board:
        pos = myboard.board.index(piece)
        print(pos)
        myboard.change(pos, piece.__class__.__name__)

    print(myboard.getboard())


    print(myboard.all_legal(0))


create_board()
