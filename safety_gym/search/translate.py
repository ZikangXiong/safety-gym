import numpy as np
import search.constants as c
from search.location import Location
from search.state import State
from search.a_star import Agent
class Translation:
    
    def __init__(self, maze, start=Location(c.START_POS_X, c.START_POS_Y), 
            goal=Location(c.GOAL_POS_X, c.GOAL_POS_Y)):
        arr_type = np.dtype('float,float')
        self.maze = np.array(maze, arr_type)

        dim = int(c.BOARD_SIZE/c.BOARD_STEP) + 1

        board = np.zeros(shape=(dim, dim))
        offset = c.BOARD_SIZE / 2
        factor = 10
        for block in maze:
            x = round(block[0], 1) * factor
            y = round(block[1], 1) * factor

            col = int(abs(x + offset*factor) / offset)
            row = int(abs(y - offset*factor) / offset)

            board[row][col] = c.INFINITY

        self.start = start
        self.goal = goal
        self.state = State(board.flatten(), self.start, c.BOARD_SIZE, c.BOARD_SIZE)
        self.ag = Agent(self.state)

    def start_search(self):
        # returns a path and a path_cost array
        return self.ag.a_star_search(self.start, self.goal)






