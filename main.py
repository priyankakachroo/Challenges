import matplotlib.pyplot as plt

from Operations import *

a = Operations(500, 100000)
print(a.gcd)
calc = a.calculate_operations()
print(f"Number of calculations to go from {a.n1} to {a.n2} are {calc}")


# test_list = [x for x in range(1, 1000)]
# calcs = []
#
# for each in test_list:
#     a = Operations(1, each)
#     calcs.append(a.calculate_operations())

# plt.plot(test_list, calcs)
# plt.grid()
# plt.show()

# print(max(calcs))
