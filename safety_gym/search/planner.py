from typing import List
import numpy as np
from translate import Translation


class Plan:
    def __init__(self, plan_list: List[np.ndarray]):
        self.plan_list = plan_list

    def __repr__(self):
        return str(self.plan_list)

    def __len__(self):
        return len(self.plan_list)

    def __getitem__(self, indx: int) -> np.ndarray:
        return self.plan_list[indx]


class Planner:
    def __init__(self, algorithm="a_star"):
        self.algo = algorithm

    def plan(self, task: str) -> Plan:
        if self.algo == "a_star":
            t = Translation()
            plan_list = t.start_search("safety-gym-maze-1")
            return Plan(plan_list)
