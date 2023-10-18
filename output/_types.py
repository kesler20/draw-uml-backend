
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            
            
class DataPipeline(Protocol):   
        
    def load_data_source_to_data_lake(self, limit : int) -> bool:
        ...
          
    def transform_data(self, transformation_function : str) -> str:
        ...
          