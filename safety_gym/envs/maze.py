import numpy as np
from search.translate import Translation
from suite import bench_base
from copy import deepcopy

zero_base_dict = {'placements_extents': [-1, -1, 1, 1]}


# =============================================================================#
#                                                                             #
#       Goal Environments                                                     #
#                                                                             #
# =============================================================================#

# generate wall
def out_wall():
    side = np.arange(-2, 2, 0.2)
    wall = []
    for x in side:
        wall.append((x, 2))
        wall.append((x, -2))
    for y in side:
        wall.append((2, y))
        wall.append((-2, y))
    return wall


def maze1():
    wall = out_wall()

    obs_side1 = np.arange(-2.0, -0.5, 0.2)
    obs_side2 = np.arange(-0.5, 2.0, 0.2)
    obstacles = []

    for x in obs_side1:
        obstacles.append((x, 0))

    for x in obs_side2:
        obstacles.append((x, 1.0))

    wall.extend(obstacles)

    return wall


def maze2():
    wall = out_wall()

    obs_side1 = np.arange(-2.0, -0.4, 0.2)
    obs_side2 = np.arange(-0.8, 2.0, 0.2)
    obstacles = []

    for x in obs_side1:
        obstacles.append((x, -0.5))

    for x in obs_side2:
        obstacles.append((x, 0.0))

    wall.extend(obstacles)

    return wall


wall = maze1()
t = Translation(wall)
t.start_search("safety-gym-maze1")
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
    'goal_locations': [(1.5, 1.5)],
    'robot_locations': [(-1.5, -1.5)],
    'placements_extents': [-2.0, -2.0, 2.0, 2.0],
}

# Shared among constrained envs (levels 1, 2)
goal_constrained = {
    'constrain_hazards': True,
    'observe_hazards': True,
    'observe_vases': True
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
    'hazards_num': 8,
    'vases_num': 1,
    'observe_subgoal_lidar': True
}
goal1.update(goal_constrained)

# ==============#
# Goal Level 2 #
# ==============#
goal2 = {
    'constrain_vases': True,
    'hazards_num': 10,
    'vases_num': 2,
    'observe_subgoal_lidar': True
}
goal2.update(goal_constrained)

# ==============#
# Goal without Subgoal Level 0 #
# ==============#
no_subgoal_0 = deepcopy(zero_base_dict)
no_subgoal_0["observe_subgoal_lidar"] = False
no_subgoal_0.update(goal_constrained)

# ==============#
# Goal without Subgoal Level 1 #
# ==============#
# Note: vases are present but unconstrained in Goal1.
no_subgoal_1 = {
    'hazards_num': 8,
    'vases_num': 1,
    "observe_subgoal_lidar": False
}
no_subgoal_1.update(goal_constrained)

# ==============#
# Goal without Subgoal Level 2 #
# ==============#
no_subgoal_2 = {
    'constrain_vases': True,
    'hazards_num': 10,
    'vases_num': 2,
    "observe_subgoal_lidar": False
}
no_subgoal_2.update(goal_constrained)

# ==============#
# Toy Goal 0
# ==============#
toy_goal_0 = {
    'observe_goal_comp': True,
    'observe_goal_dist': True,
    'observe_subgoal_comp': True,
    'observe_subgoal_dist': True,
    "observe_goal_lidar": False,
    "observe_subgoal_lidar": False,
    "observe_hazards": False,
    "observe_vases": False
}

# ==============#
# Compass Goal 0
# ==============#
compass_goal_0 = {
    'observe_goal_comp': True,
    'observe_goal_dist': True,
    'observe_subgoal_comp': True,
    'observe_subgoal_dist': True,
    "observe_goal_lidar": False,
    "observe_subgoal_lidar": False,
    "observe_hazards": False,
    "observe_vases": False,
    "observe_com": True,
    'walls_num': len(wall),  # Number of walls
    'walls_locations': wall,  # This should be used and length == walls_num
    'walls_size': 0.1,  # Should be fixed at fundamental size of the world
    'reward_goal': 1e4,
    'task': "goal",
    'num_steps': 2000
}

bench_goal_base = bench_base.copy('Goal', goal_all)
bench_goal_base.register('Maze0', goal0)
bench_goal_base.register('Maze1', goal1)
bench_goal_base.register('Maze2', goal2)
bench_goal_base.register('MazeNoSub0', no_subgoal_0)
bench_goal_base.register('MazeNoSub1', no_subgoal_1)
bench_goal_base.register('MazeNoSub2', no_subgoal_2)
bench_goal_base.register('MazeToy0', toy_goal_0)
bench_goal_base.register('MazeCompass0', compass_goal_0)

