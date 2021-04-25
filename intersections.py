# importing numpy packages
import numpy as np

# sets the random seed of the NumPy pseudo-random number generator
np.random.seed(100)

# Returning random integers from low (inclusive) to high (exclusive) in l1,l2 and l3.
l1 = np.random.randint(1, 99, 100)
l3 = np.random.randint(1, 99, 100)
l2 = np.random.randint(1, 99, 100)

#calculating the intersection by using default methods from python's set Object: intersection
intersections = set(l1).intersection(l2).intersection(l3)

# printing the result in intersection 
print(intersections)
