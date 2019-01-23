import unittest


# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].


def product_array(array_integers):
    total = 1
    result = []
    j = 0
    for i in array_integers:
        if i == 0:
            result = [0] * len(array_integers)
            return result
        total = total * i
    for i in array_integers:
        result.append(int(total / i))
        j = j + 1
    return result


class TestSolution(unittest.TestCase):

    def test1(self):
        self.assertEqual([120, 60, 40, 30, 24], product_array([1, 2, 3, 4, 5]))

    def test2(self):
        self.assertEqual([2, 3, 6], product_array([3, 2, 1]))

    def testWithZeros(self):
        self.assertEqual([0, 0, 0, 0], product_array([1, 2, 3, 0]))
