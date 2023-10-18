import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
import unittest
from datapipeline import DataPipeline
print("Testing:" + DataPipeline.__doc__)
        
class Test_DataPipeline(unittest.TestCase):        
    """This is the data pipeline for the entire protocol data
    
    testing the side effects of the DataPipeline class
    
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
        self.test_client = DataPipeline(
            data_lake
            ,data_warehouse
            ,transactions_data_source
            ,food_data_source
            ,receipts_data_source
            ,pomodoros_data_source
            ,gym_data_source
            ,fitness_data_source
        )
        
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_load_data_source_to_data_lake(self):
        """
        test the `load_data_source_to_data_lake` method which accepts the following arguments:
        
        Parameters
        ----------
        data_source_name,limit

        Returns
        -------
        bool
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.load_data_source_to_data_lake(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.load_data_source_to_data_lake()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_transform_data(self):
        """
        test the `transform_data` method which accepts the following arguments:
        
        Parameters
        ----------
        schema,data_source,transformation_function

        Returns
        -------
        str
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.transform_data(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.transform_data()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        