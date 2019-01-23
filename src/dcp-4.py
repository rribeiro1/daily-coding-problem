import unittest


# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.


def find_missing_positive_number(array_numbers):
    array_numbers.sort()
    previous = 0
    for i in array_numbers:
        if i > 0:
            if (i - previous == 1) or (previous == i):
                previous = i
            else:
                result = i - 1
                return result
    return previous + 1


class TestSolution(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_missing_positive_number([3, 4, -1, 1]), 2)

    def test2(self):
        self.assertEqual(find_missing_positive_number([1, 2, 0]), 3)

    def test3(self):
        self.assertEqual(find_missing_positive_number([1, 1, -1, -1, 0, 2, 3]), 4)

    def testWithNegativeNumbers(self):
        self.assertEqual(find_missing_positive_number([-1, -1, -2, -2, -3]), 1)

    def testWithZeros(self):
        self.assertEqual(find_missing_positive_number([0, 0, 0]), 1)
