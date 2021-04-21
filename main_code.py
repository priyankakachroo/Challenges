###
# 
# 
# How the hell branches work?
# 
# # Create a class object that store sthe remaining value and the step we are in
class node:
  def __init__(self, values: list):
    self.start = values[0]
    self.end = values[1]

# Returns minimum number of operations
def min_operations(x, y):
  steps = 0
  while x != y:
    if x < y:
      x = x * 2
    else:
      x = x -1
    steps += 1
  return steps


print(min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
