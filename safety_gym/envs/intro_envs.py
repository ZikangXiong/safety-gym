from .suite import bench_base

from .maze import out_wall

zero_base_dict = {'placements_extents': [-1, -1, 1, 1]}

wall = out_wall()
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
    'goal_locations': [(1.5, 0.0)],
    'robot_locations': [(-1.5, 0.0)],
    'placements_extents': [-2.0, -2.0, 2.0, 2.0],
}

# No hazard example
intro1 = {
    'observe_subgoal_lidar': True,
    'sparse_reward': True,
    "observe_com": True,
    'num_steps': 200
}

bench_goal_base = bench_base.copy('Intro', goal_all)

# Introduction environment 1
bench_goal_base.register('1', intro1)
