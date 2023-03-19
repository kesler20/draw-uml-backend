
import unittest
from computer import Computer

print("Testing:" + Computer.__doc__)
        

class Test_Computer(unittest.TestCase):        
    """Object Description
    
    testing the side effects of the Computer class
    
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
        self.test_client = Computer(
            foll
            ,memory
            ,run
        )
        
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_execute(self):
        """
        test the execute method which accepts the following arguments:
        
        Parameters
        ----------
        name : type

        Returns
        -------
         str
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
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_foo(self):
        """
        test the foo method which accepts the following arguments:
        
        Parameters
        ----------
        name : type

        Returns
        -------
         list
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.foo(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.foo()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        