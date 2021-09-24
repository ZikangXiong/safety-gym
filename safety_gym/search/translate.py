import numpy as np
import constants as c
from location import Location
from state import State
from a_star import Agent

from typing import List, Dict
from planning_config import planning_config
from maze import Maze

class Translation:

    def __init__(self, maze=None): 
        if maze is not None:
            arr_type = np.dtype('float,float')
            self.maze = np.array(maze, arr_type)

            dim = int(c.BOARD_SIZE/c.BOARD_STEP) + 1

            board = np.zeros(shape=(dim, dim))
            offset = c.BOARD_SIZE / 2
            for block in maze:
                x = round(block[0], 1) * c.ROUND_FACTOR
                y = round(block[1], 1) * c.ROUND_FACTOR

                col = int(abs(x + offset*c.ROUND_FACTOR) / offset)
                row = int(abs(y - offset*c.ROUND_FACTOR) / offset)

                board[row][col] = c.INFINITY

    def start_search(self, task_name):
        # returns a path 

        _config = planning_config[task_name]
        temp = np.array(_config["robot_initial_pos"])
        start = Location(*temp)
        temp = np.array(_config["goal"])
        goal = Location(*temp)
        maze = Maze(task_name)

        state = State(maze.maze_np.flatten(), start, *maze.maze_np.shape)
        agent = Agent(state, _config)
        path, _ = agent.a_star_search(start, goal)

        path = [np.array([loc.row, loc.col]) for loc in path]
        return path
