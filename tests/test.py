import unittest
from fractions import Fraction

# Imports sum() from the my_sum package
from my_sum import sum

# Defines a new test case class called TestSum, which inherits from unittest.TestCase
class TestSum(unittest.TestCase):
    # Defines a test method, .test_list_int(), to test a list of integers
    def test_list_int(self):
        '''
        Test that the function can return a sum of a list of integers.
        '''

        # Declare a variable data with a list of numbers (1, 2, 3, 4, 5)
        data = [1,2,3,4,5]
        # Assign the result of my_sum.sum(data) to a result variable
        result = sum(data)
        # Assert that the value of result equals 15 by using the .assertEqual() method on the unittest.TestCase class
        self.assertEqual(result, 15)

    
    # Make a failing test
    def test_list_fraction(self):
        '''
        Test that the function can return a sum of a list of fractions.
        '''
        data = [Fraction(1,4),Fraction(1,4),Fraction(1,3)]
        result = sum(data)
        self.assertEqual(result, 1.)

    
    # Handle error when a wrong input is provided to the function
    def test_bad_input(self):
        '''
        Raise an error for wrong input type.
        '''
        # This test case will now only pass if sum(data) raises a TypeError.
        data = 'apple'
        with self.assertRaises(TypeError):
            # The test steps are below.
            result = sum(data)

if __name__ == '__main__':
    unittest.main()