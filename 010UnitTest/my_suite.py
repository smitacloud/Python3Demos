import unittest
 
from test_mymath import TestAdd
 
 
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAdd))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
 
my_suite()

'''
Creating your own suite is a slightly convoluted process. First you need to create an instance of TestSuite and an instance of TestResult. The TestResult class just holds the results of the tests. Next we call addTest on our suite object. This is where it gets a bit weird. If you just pass in TestAdd, then it has to be an instance of TestAdd and TestAdd must also implement a runTest method. Since we didn’t do that, we use unittest’s makeSuite function to turn our TestCase class into a suite.

The last step is to actually run the suite, which means that we need a runner if we want nice output. Thus, we create an instance of TextTestRunner and have it run our suite.
'''
