
import unittest
import Complete

print("Testing:" + Complete.__doc__)
        

class Test_Complete(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self):
        self.test_client = Complete(
            name
        )
        
    def test_io_gefqwregqw(self):
        """
        test the gefqwregqw method which accepts the following arguments:
        
        ---
        Params:
        namefeqqef : efqfeqtype

        ---
        Returns:
        - efgrqqe
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

        test_result = self.test_client.gefqwregqw(*correct_input)
        self.assertEqual(test_result,correct_output[0])
        
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type(efgrqqe)) 

        test_result = self.test_client.gefqwregqw(*edge_case_input)
        self.assertEqual(test_result,edge_case_output[0])
        
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type(efgrqqe))

        test_result = self.test_client.gefqwregqw(*invalid_types_input)
        self.assertEqual(test_result,invalid_types_output[0]) 
        
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type(efgrqqe))

        test_result = self.test_client.gefqwregqw(*invalid_values_input)
        self.assertEqual(test_result,invalid_values_output[0]) 
        
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type(efgrqqe))
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        