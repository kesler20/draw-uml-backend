
from typing import List, Any, Union, Dict, Optional, Tuple
from output._types import *
        
class DataPipeline(object):
    """DataPipeline is 
    This is the data pipeline for the entire protocol data
    
    
    Example
    -------
    
    ```python
    datapipeline = DataPipeline()
    
    datapipeline.load_data_source_to_data_lake(data_source_name, limit)
                
    datapipeline.transform_data(schema, data_source, transformation_function)
                
    ```        
        
    """
    
    def __init__(self, data_lake : str, data_warehouse : str, transactions_data_source : str, food_data_source : str, receipts_data_source : str, pomodoros_data_source : str, gym_data_source : str, fitness_data_source : str) -> None:
        # signature description
        self.data_lake = data_lake
        # signature description
        self.data_warehouse = data_warehouse
        # signature description
        self.transactions_data_source = transactions_data_source
        # signature description
        self.food_data_source = food_data_source
        # signature description
        self.receipts_data_source = receipts_data_source
        # signature description
        self.pomodoros_data_source = pomodoros_data_source
        # signature description
        self.gym_data_source = gym_data_source
        # signature description
        self.fitness_data_source = fitness_data_source
    
    def load_data_source_to_data_lake(self, data_source_name : str, limit : int) -> bool:
        """load_data_source_to_data_lake This will load data from the source and publish the data to the predefined data lake
        
        Parameters
        ----------
            
        data_source_name : str
            the name of the data source to load into the datalake
        limit : int
            maximum number of items to load into the data lake
        
        Returns
        -------
        bool
            true if the load operation is succesful
        """
        ...
                          
    
    def transform_data(self, schema : str, data_source : str, transformation_function : str) -> str:
        """transform_data Given a schema, data source and a transformation function this method will apply the transformation to the data from the data source and return the transformed data
        
        Parameters
        ----------
            
        schema : str
            The schema of the data source after the transformation
        data_source : str
            The data source to grab the data from
        transformation_function : str
            The function which will be applied to the data source
        
        Returns
        -------
        str
            The data after being transformed and validated with the given schema
        """
        ...
                          