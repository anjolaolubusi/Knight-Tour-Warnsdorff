from my_chessblock import ChessBlock
import numpy as np

class Grid:
    def __init__(self, my_x : float, my_y: float):
        self.core_grid = np.empty((my_x, my_y), dtype=ChessBlock) #Numpy Array that represents the chessblock
        self.grid_width = my_x #Width of the chessboard
        self.grid_height = my_y #Height of the chessboard

        dump_list = [] #Empty list used as a temporary grid
        for i in range(my_x):
            column = [] #Columns of the temporary grid
            for j in range(my_y):
                StandardBlock = ChessBlock(i, j) #Creates a chessblock
                column.append(StandardBlock) #Adds the block to the column
            dump_list.append(column) #Adds the column to grid
        self.core_grid = np.array(dump_list, copy=True) #Creates proper chessgrid
        #del column, dump_list

    def PrintGrid(self): #Prints the chessboard
        print("Grid: ")
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                print(self.core_grid[i][j], "\t", end=" ")
            print("")
