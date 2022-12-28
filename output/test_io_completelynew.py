
import unittest
from completelynew import CompletelyNew

print("Testing:" + CompletelyNew.__doc__)
        

class Test_CompletelyNew(unittest.TestCase):        
    """This is a completely new object by the way"""
        
    def setUp(self):
        self.test_client = CompletelyNew(
            new_field
            ,another
            ,smae_one
        )
        
    def test_io_this_funct(self):
        """
        test the this_funct method which accepts the following arguments:
        
        ---
        Parameters:
        name : type

        ---
        Returns:
        - str
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.this_funct(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.this_funct(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.this_funct(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        