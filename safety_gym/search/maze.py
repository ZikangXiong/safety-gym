import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from planning_config import planning_config


class Maze:
    def __init__(self, task_name: str):
        self.maze_config = planning_config[task_name]
        self.maze_np = np.zeros(self.maze_config["board_size"])
        self._build()

    def plot(self):
        sns.heatmap(self.maze_np, linewidth=0.0)
        plt.show()
        plt.savefig('graph.png')

    def _build(self):
        self._build_walls()
        self._build_obstacles()

    def _build_walls(self):
        walls = self.maze_config["walls"]
        if walls is None:
            return
        for w in walls:
            x1 = w[1][0]
            y1 = w[1][1]
            x2 = w[2][0]
            y2 = w[2][1]
            thickness = w[3]

            is_horizontal = y1 == y2
            if is_horizontal:
                for i in range(thickness):
                    xval = min(x1, x2)
                    for x in range(abs(x1 - x2)):
                        self.maze_np[y1 + i - 1][xval + x - 1] = 1
            else:
                for i in range(thickness):
                    yval = min(y1, y2)
                    for y in range(abs(y1 - y2)):
                        self.maze_np[yval + y - 1][x1 + i - 1] = 1

    def _build_obstacles(self):
        if self.maze_config["obs_pos"] is None:
            return
        for o in self.maze_config["obs_pos"]:
            x, y = o
            for i in range(x, x + self.maze_config["obs_size"]):
                for j in range(y, y + self.maze_config["obs_size"]):
                    self.maze_np[j - 1][i - 1] = 1
