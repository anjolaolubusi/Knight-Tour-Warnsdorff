import numpy as np
from my_chessblock import ChessBlock
from my_grid import Grid
import math

class Warnsdorff:

    def __init__(self, x, y):
        self.grid = Grid(x, y) #The chessboard object
        self.grid_width = x #Width of the chessboard
        self.grid_height = y #Height of the chessboard
        self.grid_center_pos = np.array([self.grid_width/2, self.grid_height/2]) #Numpy array of the center of the chessboard
        self.knight_x = 0 #The x positon of the Knight
        self.knight_y = 0 #The y positon of the Knight
        self.count = 0 #This number will show which step the knight is

    def FindAllKinghtTourNeighbours(self): #This method will calculate all the Knight Tour neighbours
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                for temp_i in range(self.grid_width):
                    for temp_j in range(self.grid_height):
                        dump_point1 = np.array([i, j])
                        dump_point2 = np.array([temp_i, temp_j])
                        if(np.linalg.norm(dump_point1 - dump_point2) == math.sqrt(5) and self.grid.core_grid[i][j].GetState() == "*" and self.grid.core_grid[temp_i][temp_j].GetState() == "*"):
                            self.grid.core_grid[i][j].AddChessBlockToKnightTourNeighboursList(self.grid.core_grid[temp_i][temp_j])
                        del dump_point1, dump_point2

    def ClearAllKinghtTourNeighbours(self): #Clears the KnightTourNeighbours list
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                if(self.grid.core_grid[i][j].GetState() == "*"):
                    self.grid.core_grid[i][j].ClearKnightTourNeighboursList()

    def KnightTour(self): #The Knight Tour method.
        self.FindAllKinghtTourNeighbours()
        LKTN  = [] #Temporary list that represents the lengths of each Knight Tour Neighbours
        for i in range(len(self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours)):
            LKTN.append(len(self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours[i].KnightTourNeighbours))
        min_index = self.MinimumIndex(LKTN) #Temporary minimum index variable
        if(min_index != -1):
            self.count = self.count + 1
            self.grid.core_grid[self.knight_x][self.knight_y].SetState(str(self.count)) #Changes the state of the chessblock to show step number
            kx = self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours[min_index].block_x #The new knight x position
            ky = self.grid.core_grid[self.knight_x][self.knight_y].KnightTourNeighbours[min_index].block_y #The new knight y position
            self.knight_x = kx
            self.knight_y = ky
            self.ClearAllKinghtTourNeighbours()

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
                self.KnightTour()
            else:
                self.grid.PrintGrid()
        else:
            self.grid.core_grid[self.knight_x][self.knight_y].SetState(str(self.count))
            self.grid.PrintGrid()

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
