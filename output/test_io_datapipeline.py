import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
import unittest
from datapipeline import DataPipeline
print("Testing:" + DataPipeline.__doc__)
        
class Test_DataPipeline(unittest.TestCase):        
    """This is the data pipeline for the entire protocol data"""
        
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
        
    @parametrize("data_source_name,limit,bool",[
        (data_source_name,limit,bool),
        (None,[],bool),
        ("","",bool),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_load_data_source_to_data_lake(self,data_source_name,limit,expected):
        """test the `load_data_source_to_data_lake` method which accepts the following arguments:
        
        Parameters
        ----------
        data_source_name : str, limit : int

        Returns
        -------
        bool
        """
        test_result = self.test_client.load_data_source_to_data_lake(data_source_name,limit)
        self.assertEqual(type(test_result),type(expected)) 
    
    @parametrize("schema,data_source,transformation_function,str",[
        (schema,data_source,transformation_function,str),
        (None,['schema'],str),
        ("","",str),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_transform_data(self,schema,data_source,transformation_function,expected):
        """test the `transform_data` method which accepts the following arguments:
        
        Parameters
        ----------
        schema : str, data_source : str, transformation_function : str

        Returns
        -------
        str
        """
        test_result = self.test_client.transform_data(schema,data_source,transformation_function)
        self.assertEqual(type(test_result),type(expected)) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        