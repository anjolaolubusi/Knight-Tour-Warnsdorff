import numpy as np

class ChessBlock:

    def __init__(self, my_x, my_y):
        self.state = "*" #The state variable will show if a block has been moved on by a knight
        self.block_x = my_x #The x position of the chessblock
        self.block_y = my_y #The y position of the chessblock
        self.KnightTourNeighbours = [] # A list of all the chessblocks that are one knight movement away from our chessblock

    def __repr__(self):
        return self.state

    def SetState(self, new_state: str): #Simply changes the state of the chessblock
        self.state = new_state

    def PrintState(self): # Simply prints the state
        print("State = ", self.state)

    def GetState(self): # Returns the state of the chessblock
        return self.state

    def GetPos(self): # Returns the numpy array of the position
        return np.array([self.block_x, self.block_y])

    def AddChessBlockToKnightTourNeighboursList(self, block): #Adds a chessblock object to the KnightTourNeighbours list
        self.KnightTourNeighbours.append(block)

    def ClearKnightTourNeighboursList(self): # Empties the KnightTourNeighbours list
        self.KnightTourNeighbours = []
