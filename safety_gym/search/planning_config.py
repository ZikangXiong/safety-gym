planning_config = {
    "safety-gym-maze-1": {
        "robot_initial_pos": [17, 4],
        "robot_size": 1,
        "walls": [(0, [0, 0], [20, 0], 1),
                  (0, [0, 0], [0, 20], 1),
                  (0, [0, 20], [20, 20], 1),
                  (0, [20, 0], [20, 20], 1),
                  (0, [0, 10], [7, 10], 1),
                  (0, [7, 5], [20, 5], 1)],
        "obs_pos": None,
        "obs_size": 0,
        "goal": [4, 15],
        # FIXME: this needs to be set to greater than 0
        "goal_size": 1,
        "board_size": [21, 21],
        "step_size": 1
    }
}
