import numpy as np
from my_chessblock import ChessBlock
from my_grid import Grid
import math

class Warnsdorff:

    def __init__(self, width, height, x, y, BLOCK_WIDTH, BLOCK_HEIGHT):
        self.grid = Grid(width, height) #The chessboard object
        self.grid_width = width #Width of the chessboard
        self.grid_height = height #Height of the chessboard
        self.grid_center_pos = np.array([self.grid_width/2, self.grid_height/2]) #Numpy array of the center of the chessboard
        self.knight_x = x #The x positon of the Knight
        self.knight_y = y #The y positon of the Knight
        self.count = 0 #This number will show which step the knight is
        self.FindAllKinghtTourNeighbours() #Finds all the neighbours for each chessblock on the board
        self.ListOfSteps = [] #List that contains the points of the knight tour
        self.BLOCK_WIDTH = BLOCK_WIDTH #Width of Block
        self.BLOCK_HEIGHT = BLOCK_HEIGHT #Height of Block

    def FindAllKinghtTourNeighbours(self): #This method will calculate all the Knight Tour neighbours
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                temp_x = i
                temp_y = j
                if(temp_x + 1 < self.grid_width and temp_y + 2 < self.grid_height):
                    self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_x + 1][temp_y + 2])
                if(temp_x + 1 < self.grid_width and temp_y - 2 > -1):
                    self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_x + 1][temp_y - 2])
                if(temp_x - 1 > -1 and temp_y + 2 < self.grid_height):
                    self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_x - 1][temp_y + 2])
                if(temp_x - 1 > -1 and temp_y - 2 > -1):
                    self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_x - 1][temp_y - 2]) 
                if(temp_x + 2 < self.grid_width and temp_y + 1 < self.grid_height):
                    self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_x + 2][temp_y + 1])
                if(temp_x + 2 < self.grid_width and temp_y - 1 > -1):
                    self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_x + 2][temp_y - 1])
                if(temp_x - 2 > -1 and temp_y + 1 < self.grid_height):
                    self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_x - 2][temp_y + 1])
                if(temp_x - 2 > -1 and temp_y - 1 > -1):
                    self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_x - 2][temp_y - 1])

    def UpdateKinghtTourNeighbourList(self): #Clears the KnightTourNeighbours list
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                for block in self.grid.core_grid[i][j].GKTN():
                    if(block.GetState() != "*" and block.GetState() != "K"):
                        self.grid.core_grid[i][j].GKTN().remove(block)

    def KnightTour(self): #The Knight Tour method.
        for loop_counter in range(self.grid_width * self.grid_height):
            LKTN  = [] #Temporary list that represents the lengths of each Knight Tour Neighbours
            for i in range(len(self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours)):
                LKTN.append(len(self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours[i].KnightTourNeighbours))
            min_index = self.MinimumIndex(LKTN) #Temporary minimum index variable
            if(min_index != -1):
                self.count = self.count + 1
                self.grid.core_grid[self.knight_x][self.knight_y].SetState(str(self.count)) #Changes the state of the chessblock to show step number
                kx = self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours[min_index].block_x #The new knight x position
                ky = self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours[min_index].block_y #The new knight y position
                POS1 = (int(self.BLOCK_WIDTH + (self.BLOCK_WIDTH/2) + (self.BLOCK_WIDTH)*self.knight_x), int(self.BLOCK_HEIGHT + (self.BLOCK_HEIGHT/2) + (self.BLOCK_HEIGHT)*self.knight_y))    #Current position as a tuple
                POS2 = (int(self.BLOCK_WIDTH + (self.BLOCK_WIDTH/2) + (self.BLOCK_WIDTH)*kx), int(self.BLOCK_HEIGHT + (self.BLOCK_HEIGHT/2) + (self.BLOCK_HEIGHT)*ky))  #The next position as a tuple
                self.ListOfSteps.append(POS1)   #Adds the current position to ListOfSteps
                self.ListOfSteps.append(POS2)   #Adds the next positon to ListOfSteps
                self.knight_x = kx  #Updates the x-coordinate of the knight
                self.knight_y = ky  #Updates the y-coordinate of the knight
                self.UpdateKinghtTourNeighbourList() #Updates the chessboard so that the current chessblock won't be counted

                dump_first = "*"
                check1 = True #Boolean variable that shows if all the chessblocks have been visited 
                for fake_x in range(self.grid_width):
                    for fake_y in range(self.grid_height):
                        if dump_first != self.grid.core_grid[fake_x][fake_y].GetState():
                            check1 = False
                            break;

            #Checks to see if all the chessblocks have been visited
                if(check1 == False):
                    del LKTN, min_index, kx, ky, dump_first, check1
                else:
                    if (self.count == self.grid_width * self.grid_height):
                        self.HCT = True
                    print("HCT: ", self.HCT)
                    self.grid.PrintGrid()
                    self.ListOfSteps = list(dict.fromkeys(self.ListOfSteps))
                    break;
            else:
                self.count = self.count + 1
                self.grid.core_grid[self.knight_x][self.knight_y].SetState(str(self.count))
                self.ListOfSteps = list(dict.fromkeys(self.ListOfSteps))    #Cleans out the list so that there are no duplicates
                break;
    
    def SetKnight(self, kx, ky): #Sets the knight's position
        self.knight_x = kx
        self.knight_y = ky

    def MinimumIndex(self, the_length_list): #Finds the minimum index of an array. Has a method for when all elements of the array have the same value
        if(len(the_length_list) > 0):
            dump_first = the_length_list[0]
            check1 = True

            for item in the_length_list:
                if dump_first != item:
                    check1 = False
                    break;

            if(check1 == False):
                del dump_first, check1
                return the_length_list.index(min(the_length_list))           
            else:
                dump_list = []
                for i in range(len(self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours)):
                    dump_list.append(np.linalg.norm(self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours[i].GetPos() - self.grid_center_pos))
                return dump_list.index(min(dump_list))
                del dump_list
        else:
            return -1
