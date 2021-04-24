class Operations:
    """
  A class that calculates the operations needed to reach from a specific number to another,
  doing only two operations: multiplication with 2 or subtraction with 1.
  """

    def __init__(self, n1: int, n2: int):
        """
    :param n1: A random integer number to begin with
    :param n2: A random integer number to end with.

    operations: A placeholder to save the number of operations to perform.
    results: A list to save the results of the operations and look for the n2
    next_step: A temporary list to save the next branch of operations
    """
        self.n1 = n1
        self.n2 = n2
        self.operations = 0

    def reached(self, num):
        """
    Checks if we reach the number we have as target
    :return: -1 if we reached the target, else 0
    """
        if self.n1 == num:
            return -1
        else:
            return 0

    def step(self, num: int):
        """
    :param num: An integer number
    :return: A list with the results of the operations on num
    """
        addition = num + 1
        division = num / 2

        # if end number is even and bigger than start the divide by 2
        if num % 2 == 0 and self.n1 < num:
            return division
        # if end number is even and bigger than start then add 1
        elif num % 2 != 0 and self.n1 < num:
            return addition
        # all other cases return the addition
        else:
            return addition

    def calculate_operations(self):
        """
        Here we calculate the number of operations needed to reach the target number.
        :return: The number of operations
        """
        num = self.n2
        while self.reached(num) == 0:
            self.operations += 1
            result = self.step(num)
            num = result

        return self.operations
