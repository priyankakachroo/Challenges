import numpy as np

np.random.seed(42)

l1 = np.random.randint(1, 99, 100)
l3 = np.random.randint(1, 99, 100)
l2 = np.random.randint(1, 99, 100)

intersections = set(l1).intersection(l2).intersection(l3)

print(intersections)
