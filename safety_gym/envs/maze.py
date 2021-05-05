import numpy as np

from .suite import bench_base
from copy import deepcopy

zero_base_dict = {'placements_extents': [-1, -1, 1, 1]}

# =============================================================================#
#                                                                             #
#       Goal Environments                                                     #
#                                                                             #
# =============================================================================#

# generate wall
side = np.arange(-2, 2, 0.2)
wall = []
for x in side:
    wall.append((x, 2))
    wall.append((x, -2))
for y in side:
    wall.append((2, y))
    wall.append((-2, y))

obs_side1 = np.arange(-2.0, -0.4, 0.2)
obs_side2 = np.arange(-0.4, 2.0, 0.2)
obstacles = []

for x in obs_side1:
    obstacles.append((x, 0))

for x in obs_side2:
    obstacles.append((x, 0.8))

wall.extend(obstacles)

# Shared among all (levels 0, 1, 2)
goal_all = {
    'task': 'goal',
    'goal_size': 0.3,
    'goal_keepout': 0.305,
    'hazards_size': 0.2,
    'hazards_keepout': 0.18,
    'walls_num': len(wall),  # Number of walls
    'walls_locations': wall,  # This should be used and length == walls_num
    'walls_size': 0.1,  # Should be fixed at fundamental size of the world
    'goal_locations': [(-1.5, 1.5)],
    'robot_locations': [(-1.5, -1.5)]
}

# Shared among constrained envs (levels 1, 2)
goal_constrained = {
    'constrain_hazards': True,
    'observe_hazards': True,
    'observe_vases': True,
}

# ==============#
# Goal Level 0 #
# ==============#
goal0 = deepcopy(zero_base_dict)

# ==============#
# Goal Level 1 #
# ==============#
# Note: vases are present but unconstrained in Goal1.
goal1 = {
    'placements_extents': [-2.0, -2.0, 2.0, 2.0],
    'hazards_num': 8,
}
goal1.update(goal_constrained)

# ==============#
# Goal Level 2 #
# ==============#
goal2 = {
    'placements_extents': [-2, -2, 2, 2],
    'constrain_vases': True,
    'hazards_num': 10,
    'vases_num': 2
}
goal2.update(goal_constrained)

bench_goal_base = bench_base.copy('Goal', goal_all)
bench_goal_base.register('Maze0', goal0)
bench_goal_base.register('Maze1', goal1)
bench_goal_base.register('Maze2', goal2)
