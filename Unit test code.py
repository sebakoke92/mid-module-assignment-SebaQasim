    # unit test case
import unittest

class TestStringMethod (unittest.TestCase):
    # test function to test equality of two value 
    def test_positive(self):
        output_list =graph
        expected list =[
            [0,7,12,8],
            [INF,0,5,7],
            [INF,INF,0,2],
            [INF,INF,INF,0],
        ]

        # error message in case if test case got failed
        message = " First value and second value are not equal  !"
        #assertEqual() to check equality of first & second value 
        self.assertEqual(expected_list, output_list)

if __name__=== "__main__":
     unittest.main()

