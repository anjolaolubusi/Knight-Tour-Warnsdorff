import numpy as np
from my_tour import Warnsdorff

real_x = -1
real_y = -1

def GetXY():
    global real_x
    global real_y

    real_x=int(input("Input x: "))
    real_y=int(input("Input y: "))

GetXY()
my_grid = Warnsdorff(real_x, real_y)
my_grid.KnightTour()
