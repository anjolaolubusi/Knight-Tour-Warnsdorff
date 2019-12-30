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

screen = pygame.display.set_mode((800, 600)) #Sets the default screen size (Subject to change)
pygame.display.set_caption("PyTour: Getting Input") #Sets the title of the window
fpsClock.tick(60) #Sets FPS to be 60
screen.fill((255,255,255)) #Fills the screen to be white
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30)

start_x = 0
start_y = 0
chess_width = 0
chess_height = 0

string = ""
textsurface = myfont.render('Enter Width: ', False, (0, 0, 0))

def GetWidth():
    global textsurface,string,running,chess_width
    pygame.display.flip()
    screen.fill(WHITE)
    screen.blit(textsurface,(0,0))
    test = myfont.render(string, False, (0, 0, 0))
    screen.blit(test,(200,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(len(event.unicode) > 0):
                if (ord(event.unicode) < 58 and ord(event.unicode) > 47):
                    string += pygame.key.name(event.key)
                    pygame.display.update()
                elif pygame.key.name(event.key) == "backspace":
                    string = string[:len(string) - 1]
                    pygame.display.update()
                elif pygame.key.name(event.key) == "return":
                    chess_width = int(string)
                    string = ""
                    screen.fill((255,255,255))
                    running = False
            else:
                pass

def GetHeight(): 
    global textsurface,string,WHITE,running,chess_height 
    pygame.display.flip()
    screen.fill((255,255,255))
    textsurface = myfont.render('Enter Height: ', False, (0, 0, 0))
    screen.blit(textsurface,(0,0))
    test = myfont.render(string, False, (0, 0, 0))
    screen.blit(test,(200,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(len(event.unicode) > 0):
                if (ord(event.unicode) < 58 and ord(event.unicode) > 47):
                    string += pygame.key.name(event.key)
                    pygame.display.update()
                elif pygame.key.name(event.key) == "backspace":
                    string = string[:len(string) - 1]
                    pygame.display.update()
                elif pygame.key.name(event.key) == "return":
                    chess_height = int(string)
                    string = ""
                    screen.fill(WHITE)
                    running = False
            else:
                pass

def GetX():
    global textsurface,string,running,WHITE,start_x
    pygame.display.flip()
    screen.fill((255,255,255))
    textsurface = myfont.render('Enter X: ', False, (0, 0, 0))
    screen.blit(textsurface,(0,0))
    test = myfont.render(string, False, (0, 0, 0))
    screen.blit(test,(200,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(len(event.unicode) > 0):
                if (ord(event.unicode) < 58 and ord(event.unicode) > 47):
                    string += pygame.key.name(event.key)
                    pygame.display.update()
                elif pygame.key.name(event.key) == "backspace":
                    string = string[:len(string) - 1]
                    pygame.display.update()
                elif pygame.key.name(event.key) == "return":
                    start_x = int(string)
                    string = ""
                    running = False

def GetY():
    global textsurface,string,WHITE,running,start_y
    pygame.display.flip()
    screen.fill((255,255,255))
    textsurface = myfont.render('Enter Y: ', False, (0, 0, 0))
    screen.blit(textsurface,(0,0))
    test = myfont.render(string, False, (0, 0, 0))
    screen.blit(test,(200,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(len(event.unicode) > 0):
                if (ord(event.unicode) < 58 and ord(event.unicode) > 47):
                    string += pygame.key.name(event.key)
                    pygame.display.update()
                elif pygame.key.name(event.key) == "backspace":
                    string = string[:len(string) - 1]
                    pygame.display.update()
                elif pygame.key.name(event.key) == "return":
                    start_y = int(string)
                    string = ""
                    running = False

running = True
while running: 
    GetWidth()
running = True
while running:
    GetHeight()
running = True
while running:
    GetX()
running = True
while running:
    GetY()


#Makes sure that the intial position of the knight can not go below (0,0)
if(start_y - 1 < 0):
    start_y = 0
else:
    start_y = start_y - 1

if(start_y > chess_width):
    GetY()

if(start_x > chess_height):
    GetX()

if(start_x - 1 < 0):
    start_x = 0
else:
    start_x = start_x - 1

my_grid = Warnsdorff(chess_width, chess_height, start_x, start_y, BLOCK_WIDTH, BLOCK_HEIGHT) #Object that contains the knight tour and the grid

OriginPoint = np.array((BLOCK_WIDTH, BLOCK_HEIGHT)) #The starting point of our grid
ChessCursor = OriginPoint #The cursor used to draw the grid
screen_width = int((chess_width + 2) * BLOCK_WIDTH) #The width of the new window
screen_height = int((chess_height + 2) * BLOCK_HEIGHT) #The height of the new window
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
    for i in range(chess_height):
        for j in range(chess_width):
            drawRectangle(j, i)
            ChessCursor[0] = ChessCursor[0] + BLOCK_WIDTH
        ChessCursor[0] = BLOCK_WIDTH
        ChessCursor[1] = ChessCursor[1] + BLOCK_HEIGHT

    ChessCursor = OriginPoint
    for i in range(chess_width + 1):
        pygame.draw.line(screen, BLACK, ChessCursor, (ChessCursor[0], OriginPoint[1] + (chess_height)*BLOCK_HEIGHT))
        ChessCursor[0] = ChessCursor[0] + BLOCK_WIDTH
    
    OriginPoint = np.array((BLOCK_WIDTH, BLOCK_HEIGHT))
    ChessCursor = OriginPoint
    for j in range(chess_height + 1):
        pygame.draw.line(screen, BLACK, ChessCursor, (OriginPoint[0] + (chess_width)*BLOCK_WIDTH, ChessCursor[1]))
        ChessCursor[1] += BLOCK_HEIGHT

my_grid.KnightTour() #Starts the KnightTour
DrawChessBoard() 

step = 0
#Loop so that we can see the knight tour
while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        
        if step < len(my_grid.ListOfSteps) - 1:
            pygame.draw.line(screen, RED, my_grid.ListOfSteps[step], my_grid.ListOfSteps[step + 1], 2)
            step += 1
        #pygame.draw.lines(screen, RED, True, my_grid.ListOfSteps, 2)
        fpsClock.tick(10)
        pygame.display.update()

