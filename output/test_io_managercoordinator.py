
import unittest
from managercoordinator import ManagerCoordinator

print("Testing:" + ManagerCoordinator.__doc__)
        

class Test_ManagerCoordinator(unittest.TestCase):        
    '''The manager coordinator manages all the object within the programme'''
        
    def setUp(self):
        self.test_client = ManagerCoordinator(
            emit
        )
        
    def test_io_run(self):
        """
        test the run method which accepts the following arguments:
        
        ---
        Params:
        message : str

        ---
        Returns:
        - str
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments representing
        # a potential edge case where the method might be used
        edge_case_input = []
        # array containing the expected result of the function call
        edge_case_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.run(*correct_input)
        self.assertEqual(test_result,correct_output[0])
        
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type(str)) 

        test_result = self.test_client.run(*edge_case_input)
        self.assertEqual(test_result,edge_case_output[0])
        
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type(str))

        test_result = self.test_client.run(*invalid_types_input)
        self.assertEqual(test_result,invalid_types_output[0]) 
        
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type(str))

        test_result = self.test_client.run(*invalid_values_input)
        self.assertEqual(test_result,invalid_values_output[0]) 
        
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type(str))
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        