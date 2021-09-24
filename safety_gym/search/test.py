'''from maze import Maze

m = Maze("safety-gym-maze-1")
print("doing this")
m.plot()
print("did it")
'''

from planner import Planner
p = Planner()
x = p.plan("safety-gym-maze-1")
#print(x)
