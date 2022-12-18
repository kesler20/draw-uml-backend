
import unittest
from managercoordinator import ManagerCoordinator

print("Testing:" + ManagerCoordinator.__doc__)
        

class Test_ManagerCoordinator(unittest.TestCase):        
    '''The manager coordinator manages all the object within the programme'''
        
    def setUp(self):
        self.test_client = ManagerCoordinator(
            emit
        )
        
    def test_side_effects_run(self):
        """
        test the run method which accepts the following arguments:
        
        ---
        Params:
        message : str

        ---
        Returns:
        - str
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.run(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.run()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        