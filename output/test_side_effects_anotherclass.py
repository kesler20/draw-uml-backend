
import unittest
from anotherclass import AnotherClass

print("Testing:" + AnotherClass.__doc__)
        

class Test_AnotherClass(unittest.TestCase):        
    '''Object Description'''
        
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
        
    def setUp(self):
        self.test_client = AnotherClass(
            testing
        )
        
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        