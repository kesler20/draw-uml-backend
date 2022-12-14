
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            

class  str = "protocol_database.xlsx"(Protocol):
    ...
            

class DataFrame(Protocol):
    ...
            
            
class ExcelDatabase(Protocol):   
        
    def filename(self) -> str:
        ...
          
    def database(self) -> DataFrame:
        ...
          
    def database_info(self) -> None:
        ...
          
    def _pp(self, message : str) -> None:
        ...
          
    def create_table(self, rows : List[List[Any]]) -> None:
        ...
          
    def get_table(self, table_name : str) -> DataFrame:
        ...
          
    def query_table(self) -> DataFrame:
        ...
          
    def get_table_slice(self, index : Optional[Tuple[int,int]]=None) -> Any:
        ...
          
    def get_n_rows_from_tables_above(self, table_name : str) -> Any:
        ...
          
    def get_n_rows_from_tables_below(self, table_name : str) -> Any:
        ...
          
    def table_info(self, table_name : str) -> Any:
        ...
          
    def get_table_names(self) -> List[str]:
        ...
          
    def get_value_by_column_name(self, table_name : str) -> Any:
        ...
          
    def get_value_by_column_index(self, table_name : str) -> Any:
        ...
          
    def delete_table(self, table_name : str) -> Any:
        ...
          
    def append_row(self, table_name : str) -> None:
        ...
          
    def update_rows(self) -> None:
        ...
          
    def delete_rows(self, table_name : str) -> None:
        ...
          
    def put_column(self, table_name : str) -> None:
        ...
          
    def insert_column(self, table_name : str) -> None:
        ...
          
    def delete_columns(self, table_name : str) -> Any:
        ...
          