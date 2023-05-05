import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
import unittest
from person import Person
print("Testing:" + Person.__doc__)
        
class Test_Person(unittest.TestCase):        
    """This should represent a person in real life
    
    testing the side effects of the Person class
    
    Example 
    -------
    How those tests are run
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
        self.test_client = Person(
            name
            ,age
        )
        
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_get_full_name(self):
        """
        test the `get_full_name` method which accepts the following arguments:
        
        Parameters
        ----------
        last_name

        Returns
        -------
        str
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_full_name(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_full_name()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        