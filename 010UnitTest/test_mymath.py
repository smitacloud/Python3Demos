import mymath
import unittest
 
class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
 
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)
 
    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)
 
    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')
 
 
if __name__ == '__main__':
    unittest.main()


'''
First we import our mymath module and Python’s unittest module. Then we subclass TestCase and add three tests, which translates into three methods. The first function tests the addition of two integers; the second function tests the addition of two floating point numbers; and the last function concatenates two strings together. Finally we call unittest’s main method at the end.

You will note that each method begins with the letters “test”. This is actually important! It tells the test runner which methods are tests that it should run. Each test should have at least one assert which will verify that the result is as we expected. The unittest module supports many different types of asserts. You can test for exceptions, for Boolean conditions, and for many other conditions.
'''
