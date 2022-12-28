
import unittest
from completelynew import CompletelyNew

print("Testing:" + CompletelyNew.__doc__)
        

class Test_CompletelyNew(unittest.TestCase):        
    """This is a completely new object by the way
    
    testing the side effects of the CompletelyNew class
    
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
        self.test_client = CompletelyNew(
            new_field
            ,another
            ,smae_one
        )
        
    def test_side_effects_this_funct(self):
        """
        test the this_funct method which accepts the following arguments:
        
        ---
        Parameters:
        name : type

        ---
        Returns:
        - str
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.this_funct(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.this_funct()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        