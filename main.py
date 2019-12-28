import pygame,sys
from pygame.locals import *
import pygame_gui
from my_tour import Warnsdorff
import numpy as np

pygame.init() #Initalises pygame
fpsClock = pygame.time.Clock() #Sets the frames per second

WHITE=(255,255,255) #RGB Value for White
BLACK = (0,0,0) #RGB Value for Black
RED = (255, 0, 0) # RGB Value for Red
BLOCK_WIDTH = 30 #Default value for the width of the block
BLOCK_HEIGHT = 30 #Default value for the height of the block

screen = pygame.display.set_mode((1280, 720)) #Sets the default screen size (Subject to change)
pygame.display.set_caption("PyTour: Getting Input") #Sets the title of the window
fpsClock.tick(60) #Sets FPS to be 60
screen.fill((255,255,255)) #Fills the screen to be white

real_x=int(input("Input Width of Chessboard: ")) #Gets the width of the chessboard
real_y=int(input("Input Height of Chessboard: ")) #Gets the height of the chessboard
test_y = int(input("Input the X position: ")) #Gets the inital x position of the knight
test_x = int(input("Input the Y position: ")) #Gets the inital y position of the knight

#Makes sure that the intial position of the knight can not go below (0,0)
if(test_y - 1 < 0):
    test_y = 0
else:
    test_y = test_y - 1

if(test_x - 1 < 0):
    test_x = 0
else:
    test_x = test_x - 1
 
my_grid = Warnsdorff(real_x, real_y) #Object that contains the knight tour and the grid
my_grid.knight_x = test_x #Sets the inital x position
my_grid.knight_y = test_y #Sets the inital y position

OriginPoint = np.array((BLOCK_WIDTH, BLOCK_HEIGHT)) #The starting point of our grid
ChessCursor = OriginPoint #The cursor used to draw the grid
screen_width = int((real_x + 2) * BLOCK_WIDTH) #The width of the new window
screen_height = int((real_y + 2) * BLOCK_HEIGHT) #The height of the new window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE) #Resizes the window to our speficiations
screen.fill((255, 255, 255))#Makes the background white

#Draws Colored Square
def drawRectangle(x : int, y: int):
    global ChessCursor
    global BLOCK_WIDTH
    global BLOCK_HEIGHT
    if( (x + y) % 2 == 0):
        square = pygame.Rect((ChessCursor[0], ChessCursor[1]), (BLOCK_WIDTH, BLOCK_HEIGHT))
        pygame.draw.rect(screen, WHITE, square)
    else:
        square = pygame.Rect((ChessCursor), (BLOCK_WIDTH, BLOCK_HEIGHT))
        pygame.draw.rect(screen, BLACK, square)

#Draws the Chessboard
def DrawChessBoard():
    global ChessCursor
    global OriginPoint
    global BLOCK_WIDTH
    global BLOCK_HEIGHT
    global screen, RED
    OriginPoint = np.array((BLOCK_WIDTH, BLOCK_HEIGHT))
    for i in range(real_y):
        for j in range(real_x):
            drawRectangle(j, i)
            ChessCursor[0] = ChessCursor[0] + BLOCK_WIDTH
        ChessCursor[0] = BLOCK_WIDTH
        ChessCursor[1] = ChessCursor[1] + BLOCK_HEIGHT

    ChessCursor = OriginPoint
    for i in range(real_x + 1):
        pygame.draw.line(screen, BLACK, ChessCursor, (ChessCursor[0], OriginPoint[1] + (real_y)*BLOCK_HEIGHT))
        ChessCursor[0] = ChessCursor[0] + BLOCK_WIDTH
    
    OriginPoint = np.array((BLOCK_WIDTH, BLOCK_HEIGHT))
    ChessCursor = OriginPoint
    for j in range(real_y + 1):
        pygame.draw.line(screen, BLACK, ChessCursor, (OriginPoint[0] + (real_x)*BLOCK_WIDTH, ChessCursor[1]))
        ChessCursor[1] += BLOCK_HEIGHT

def DrawKnightTour():
    global my_grid
    global real_x
    global real_y
    global OriginPoint
    max_count = real_x * real_y
    count = 1
    dump = np.zeros((real_x, real_y))
    for i in range(real_x):
        for j in range(real_y):
            dump[i][j] = int(my_grid.grid.core_grid[i][j].GetState())
    while(count < max_count):
        pos1 = np.where(dump == count)
        POS1 = (int(BLOCK_WIDTH + (BLOCK_WIDTH/2) + (BLOCK_WIDTH)*pos1[0]), int(BLOCK_HEIGHT + (BLOCK_HEIGHT/2) + (BLOCK_HEIGHT)*pos1[1]))
        count += 1
        pos2 = np.where(dump == count)
        POS2 = (int(BLOCK_WIDTH + (BLOCK_WIDTH/2) + (BLOCK_WIDTH)*pos2[0]), int(BLOCK_HEIGHT + (BLOCK_HEIGHT/2) + (BLOCK_HEIGHT)*pos2[1]))
        pygame.draw.lines(screen, RED, True, [POS1, POS2], 1)

my_grid.KnightTour() #Starts the KnightTour
DrawChessBoard() 
DrawKnightTour()

#Loop so that we can see the knight tour
while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

