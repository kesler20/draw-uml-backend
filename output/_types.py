
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            
            
<<<<<<< HEAD
class DatabaseInterface(Protocol):   
        
    def create(self, body : dict) -> dict:
        ...
          
    def read(self, name : str) -> dict:
        ...
          
    def update(self, name : str) -> dict:
        ...
          
    def delete(self, name : str) -> dict:
=======
class DataPipeline(Protocol):   
        
    def load_data_source_to_data_lake(self, limit : int) -> bool:
        ...
          
    def transform_data(self, transformation_function : str) -> str:
>>>>>>> new-feature
        ...
          