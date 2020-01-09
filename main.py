import pygame,sys,math
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

start_x = 0 #Starting x-coordinate
start_y = 0 #Starting y-coordinate
chess_width = 0 #Width of the chessboard
chess_height = 0 #Height of the chessboard

string = "" #Empty string used to hold the input
textsurface = myfont.render('Enter Width: ', False, (0, 0, 0)) #Text to show on screen

def GetWidth(): #Gets the width of the chessboard
    global textsurface,string,running,chess_width
    pygame.display.flip() #Updates the screen
    screen.fill(WHITE) #Paints the screen white
    test = myfont.render(string, False, (0, 0, 0)) #Text to show the input
    screen.blit(test,(400 + (textsurface.get_width() // 2),300 - (textsurface.get_height() // 2)) ) #Shows "Enter Width: " on screen
    screen.blit(textsurface,(400  - (textsurface.get_width() // 2), 300 - (textsurface.get_height() // 2)) ) #Shows input on screen
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(len(event.unicode) > 0):
                if (ord(event.unicode) < 58 and ord(event.unicode) > 47): #Makes sure that the input is numerical
                    string += pygame.key.name(event.key) #Updates input string
                    pygame.display.update()
                elif pygame.key.name(event.key) == "backspace": #Removes one character from the input string
                    string = string[:len(string) - 1]
                    pygame.display.update()
                elif pygame.key.name(event.key) == "return":
                    chess_width = int(string)
                    string = ""
                    screen.fill((255,255,255))
                    running = False
            else:
                pass
        if event.type==QUIT:
                pygame.quit()
                sys.exit()

def GetHeight(): #Gets the height of the chessboard
    global string,WHITE,running,chess_height 
    pygame.display.flip()
    screen.fill((255,255,255))
    textsurface = myfont.render('Enter Height: ', False, (0, 0, 0))
    test = myfont.render(string, False, (0, 0, 0))
    screen.blit(test,(400 + (textsurface.get_width() // 2),300 - (textsurface.get_height() // 2)) ) 
    screen.blit(textsurface,(400  - (textsurface.get_width() // 2), 300 - (textsurface.get_height() // 2)) )
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
        if event.type==QUIT:
                pygame.quit()
                sys.exit()

#Terrible loops to get all the input data we need
running = True
while running: 
    GetWidth()
running = True
while running:
    GetHeight()

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
    #global OriginPoint
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
    
    ChessCursor = np.array((BLOCK_WIDTH, BLOCK_HEIGHT))

my_grid = Warnsdorff(chess_width, chess_height, start_x, start_y, BLOCK_WIDTH, BLOCK_HEIGHT) #Object that contains the knight tour and the grid
my_grid.KnightTour() #Starts the KnightTour

OriginPoint = np.array((BLOCK_WIDTH, BLOCK_HEIGHT)) #The starting point of our grid
ChessCursor = OriginPoint #The cursor used to draw the grid
screen_width = int((chess_width + 2) * BLOCK_WIDTH) #The width of the new window
screen_height = int((chess_height + 2) * BLOCK_HEIGHT) #The height of the new window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE) #Resizes the window to our speficiations
pygame.display.set_caption("PyTour: Getting Starting Position") #Sets the title of the window
screen.fill((255, 255, 255))#Makes the background white
DrawChessBoard() 

def GetStartPos(): 
    global running,start_x,start_y,textsurface,string,screen
    myfont = pygame.font.SysFont('Times New Roman', int(14*math.log(math.sqrt((chess_width ** 2) + (chess_height ** 2)), 10) ))
    pygame.display.flip()
    textsurface = myfont.render('Click on the starting chessblock', False, (0,0,0))
    screen.blit(textsurface, (screen_width // 2 - textsurface.get_width() // 2, BLOCK_HEIGHT // 2 - 10))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(BLOCK_WIDTH <= pos[0] <= (chess_width + 1)*BLOCK_WIDTH and BLOCK_HEIGHT <= pos[1] <= (chess_height + 1)*BLOCK_HEIGHT):
                start_x = int(pos[0]/BLOCK_WIDTH) - 1
                start_y = int(pos[1]/BLOCK_HEIGHT) - 1
                pygame.draw.rect(screen , WHITE, ((0,0), (screen_width // 2 + textsurface.get_width() // 2, BLOCK_HEIGHT)))
                pygame.display.flip()
                running = False
        if event.type==QUIT:
                pygame.quit()
                sys.exit()

running = True
while running:
    fpsClock.tick(60)
    pygame.display.update()
    GetStartPos()

my_grid = Warnsdorff(chess_width, chess_height, start_x, start_y, BLOCK_WIDTH, BLOCK_HEIGHT) #Object that contains the knight tour and the grid
my_grid.KnightTour() #Starts the KnightTour
pygame.display.set_caption("PyTour: Animating KnightTour") #Sets the title of the window

step = 0
finished = False
def AnimateKnightTour():
    global step, my_grid,finished,start_x, start_y,BLOCK_WIDTH,BLOCK_HEIGHT,chess_width,chess_height,screen
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and finished == True:
            pos = pygame.mouse.get_pos()
            if(BLOCK_WIDTH <= pos[0] <= (chess_width + 1)*BLOCK_WIDTH and BLOCK_HEIGHT <= pos[1] <= (chess_height + 1)*BLOCK_HEIGHT):
                start_x = int(pos[0]/BLOCK_WIDTH) - 1
                start_y = int(pos[1]/BLOCK_HEIGHT) - 1
            screen.fill(WHITE)
            DrawChessBoard()
            my_grid = Warnsdorff(chess_width, chess_height, start_x, start_y, BLOCK_WIDTH, BLOCK_HEIGHT) #Object that contains the knight tour and the grid
            my_grid.KnightTour()
            finished = False
            AnimateKnightTour()

    if step < len(my_grid.ListOfSteps) - 1 and finished == False:
        pygame.draw.line(screen, RED, my_grid.ListOfSteps[step], my_grid.ListOfSteps[step + 1], 2)
        step += 1

    if step == len(my_grid.ListOfSteps) - 1:
        step = 0
        finished = True
        myfont = pygame.font.SysFont('Times New Roman', int(14*math.log(math.sqrt((chess_width ** 2) + (chess_height ** 2)), 10) ))
        pygame.display.flip()
        textsurface = myfont.render('Click on the starting chessblock', False, (0,0,0))
        screen.blit(textsurface, (screen_width // 2 - textsurface.get_width() // 2, BLOCK_HEIGHT // 2 - 10))




while True:
    fpsClock.tick(10)
    pygame.display.update()
    AnimateKnightTour()
