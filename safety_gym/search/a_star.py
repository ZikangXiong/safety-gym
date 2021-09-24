from queue import PriorityQueue

import constants as c
from typing import List, Dict
import numpy as np

class Agent:
    """
    Agent of player
    """

    def __init__(self, state, configs: Dict):
        self.states = []
        self.actions = ["up", "down", "left", "right"]
        self.state = state
        self.configs = configs

        # initial state reward
        self.state_values = {}
        for i in range(state.board_rows):
            for j in range(state.board_cols):
                self.state_values[(i, j)] = 0  # set initial value to 0

    @staticmethod
    def reconstruct_path(path, start, goal):
        new_path = []
        new_path.insert(0, goal)
        curr = path[goal]
        while path[curr] is not None:
            new_path.insert(0, curr)
            curr = path[curr]
        new_path.insert(0, start)
        return new_path

    def get_average_cost(self, x, y):
        cost = 0
        for i in range(self.configs["robot_size"]):
            for j in range(self.configs["robot_size"]):
                cost = cost + self.state.cost[y + j - 1][x + i - 1]
        cost = cost / (self.configs["robot_size"] * self.configs["robot_size"])
        return cost

    def a_star_search(self, start_state, goal_state):
        q = PriorityQueue()
        q.put(start_state, False)
        path = {start_state: None}
        path_cost = {start_state: 0.0}

        while not q.empty():
            current = q.get()

            current_array = np.array([current.row, current.col])
            goal_state_array = np.array([goal_state.row, goal_state.col])
            goal_size = self.configs["goal_size"]

            #If we use the following lines, we aren't able to reach the goal. Keeping
            #   them commented in case we want to use them in the future
            #if (current_array <= goal_state_array + goal_size).all() \
                    #        and (current_array >= goal_state_array - goal_size).all():
            if (current_array == goal_state_array).all():
                break
            else:
                for _dir in self.actions:
                    next_state = self.state.next_position(_dir, current, self.configs["step_size"])
                    next_state_cost = self.get_average_cost(next_state.row, next_state.col)
                    new_cost = path_cost[current] + next_state_cost

                    if (next_state not in path_cost and next_state_cost == 0) or (
                            next_state in path_cost and new_cost < path_cost[next_state]):
                        path_cost[next_state] = new_cost
                        new_priority = new_cost + (self.state.heuristic(next_state, goal_state))
                        q.put(next_state, new_priority)
                        path[next_state] = current

        return self.reconstruct_path(path, start_state, goal_state), path_cost

