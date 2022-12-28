
import unittest
from comandmanager import ComandManager

print("Testing:" + ComandManager.__doc__)
        

class Test_ComandManager(unittest.TestCase):        
    """Object Description"""
        
    def setUp(self):
        self.test_client = ComandManager(
            testing_it
            ,another_property
        )
        
    def test_io_execute(self):
        """
        test the execute method which accepts the following arguments:
        
        ---
        Parameters:
        name : type

        ---
        Returns:
        - None
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

        test_result = self.test_client.execute(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.execute(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.execute(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_data(self):
        """
        test the get_data method which accepts the following arguments:
        
        ---
        Parameters:
        p : str, vv : int

        ---
        Returns:
        - list
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

        test_result = self.test_client.get_data(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_data(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_data(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io___run(self):
        """
        test the __run method which accepts the following arguments:
        
        ---
        Parameters:
        p : str, vv : int

        ---
        Returns:
        - None
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

        test_result = self.test_client.__run(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.__run(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.__run(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        