import unittest

from dynamicProgramming import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_ComputeFibonacci(self):

        fifthFiboIndex = 4
        fifthFiboValue = 3

        returnedFiboValue = fibonacci(fifthFiboIndex)
        self.assertEqual(returnedFiboValue, fifthFiboValue)
