import numpy as np
from my_tour import Warnsdorff
from my_grid import Grid

real_x = -1
real_y = -1

def GetXY():
    global real_x
    global real_y

    real_x=int(input("Input Width of Chessboard: "))
    real_y=int(input("Input Height of Chessboard: "))

GetXY()
my_grid = Warnsdorff(real_x, real_y)
my_grid.AskForKnightPosition()
my_grid.KnightTour()

