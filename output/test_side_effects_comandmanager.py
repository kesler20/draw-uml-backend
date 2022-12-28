
import unittest
from comandmanager import ComandManager

print("Testing:" + ComandManager.__doc__)
        

class Test_ComandManager(unittest.TestCase):        
    """Object Description
    
    testing the side effects of the ComandManager class
    
    Example of how those tests are run
    ---
    given a method ``append_row`` which takes the following arguments
    ```txt
    row: List[List], table_name: str
    ```
    you can cause the side effect (call the method being tested) and then check the endpoints
    ```python
    # array of arguments which are expected by the method which causes the side effect under test
    side_effect_input = [[121],base_table_name]
    # array containing the expected correct result of the side effect
    side_effect_output = [pd.DataFrame([*base_df_values, 121],columns=base_df_cols)]

    # cause a side effect to test
    test_result = self.test_client.append_row(*side_effect_input)

    # test that the side effect is expected
    test_result = self.test_client.get_table(base_table_name)
    self.assertTrue(test_result.equals(side_effect_output[0]))    
    ```
    """
    
        
    def setUp(self):
        self.test_client = ComandManager(
            testing_it
            ,another_property
        )
        
    def test_side_effects_execute(self):
        """
        test the execute method which accepts the following arguments:
        
        ---
        Parameters:
        name : type

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.execute(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.execute()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_get_data(self):
        """
        test the get_data method which accepts the following arguments:
        
        ---
        Parameters:
        p : str, vv : int

        ---
        Returns:
        - list
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_data(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_data()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects___run(self):
        """
        test the __run method which accepts the following arguments:
        
        ---
        Parameters:
        name : type

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.__run(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.__run()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        