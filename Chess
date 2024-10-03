from Class import *


def main():
    pass


def create_board():
    myboard = ChessBoard()
    # white side
    for x in range(0, 8):
        for y in range(0, 2):
            if y !=0:
                if x == 0 or x ==8:
                    myboard.change((x, y), Rook((x,y), 0))
                elif x == 1 or x ==7:
                    myboard.change((x, y), Knight((x, y), 0))
                elif x ==2 or x == 6:
                    myboard.change((x, y), Bishop((x, y), 0))
                elif x == 3:
                    myboard.change((x, y), Queen((x, y), 0))
                elif x == 4:
                    myboard.change((x, y), King((x, y), 0))

create_board()

def convert(np_array):
    mytuple = tuple(np_array.tolist())
    return mytuple

