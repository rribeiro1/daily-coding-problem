import unittest

# This problem was asked by Jane Street.
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
#
# Implement car and cdr.


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def left(a, b):
        return a
    return pair(left)


def cdr(pair):
    def right(a, b):
        return b
    return pair(right)


class TestSolution(unittest.TestCase):

    def test1(self):
        self.assertEqual(3, car(cons(3, 4)))

    def test2(self):
        self.assertEqual(4, cdr(cons(3, 4)))
