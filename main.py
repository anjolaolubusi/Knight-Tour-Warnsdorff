import pygame,sys
from pygame.locals import *
import pygame_gui
from my_tour import Warnsdorff

pygame.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyTour: Getting Input")
fpsClock.tick(60)

while True:
    global real_x
    global real_y
    global my_grid
    screen.fill((255,255,255))
    pygame.display.update()
    real_x=int(input("Input Width of Chessboard: "))
    real_y=int(input("Input Height of Chessboard: "))
   
    test_y = int(input("Input the X position: "))
    test_x = int(input("Input the Y position: "))

    if(test_y - 1 < 0):
        test_y = 0
    else:
        test_y = test_y - 1

    if(test_x - 1 < 0):
        test_x = 0
    else:
        test_x = test_x - 1
 
    my_grid = Warnsdorff(real_x, real_y) 
    my_grid.knight_x = test_x
    my_grid.knight_y = test_y
    pygame.quit()
    break

print("RX: ", real_x, " RY: ", real_y)
my_grid.KnightTour()

