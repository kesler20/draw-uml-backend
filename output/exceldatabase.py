
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass
from output._types import  str, DataFrame
        
@dataclass
class ExcelDatabase:
    """ExcelDatabase is a class"""
    
    __filename :  str = "protocol_database.xlsx"
    
    @property
    def filename(self):
        """filename property getter"""
        return self.__filename
                
    def set_filename(self,filename : str):
        """filename property setter"""
        self.__filename = filename
            
    @property
    def filename(self) -> str:
        """filename has the following params
        """
        ...        
                  
    @property
    def database(self) -> DataFrame:
        """database has the following params
        """
        ...        
                  
    @property
    def database_info(self) -> None:
        """database_info has the following params
        """
        ...        
                  
    
    def _pp(self, table : DataFrame, table_name : str, message : str) -> None:
        """_pp has the following params
        
        Parameters
        ---
            
        table DataFrame
            to be passed as parameter 2
        table_name str
            to be passed as parameter 3
        message str
            to be passed as parameter 4
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def create_table(self, table_name : str, columns : List[str], rows : List[List[Any]]) -> None:
        """create_table has the following params
        
        Parameters
        ---
            
        table_name str
            to be passed as parameter 2
        columns List[str]
            to be passed as parameter 3
        rows List[List[Any]]
            to be passed as parameter 4
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def get_table(self, table_name : str) -> DataFrame:
        """get_table has the following params
        
        Parameters
        ---
            
        table_name str
            to be passed as parameter 2
        
        Returns
        ---
        result: DataFrame
        """
        ...
                          
    
    def query_table(self) -> DataFrame:
        """query_table has the following params
        """
        ...        
                  
    
    def get_table_slice(self, columns : Union[str,List[str]], table_name : str, index : Optional[Tuple[int,int]]=None) -> Any:
        """get_table_slice has the following params
        
        Parameters
        ---
            
        columns Union[str,List[str]]
            to be passed as parameter 2
        table_name str
            to be passed as parameter 3
        index Optional[Tuple[int,int]]=None
            to be passed as parameter 4
        
        Returns
        ---
        result: Any
        """
        ...
                          
    
    def get_n_rows_from_tables_above(self, n : int, table_name : str) -> Any:
        """get_n_rows_from_tables_above has the following params
        
        Parameters
        ---
            
        n int
            to be passed as parameter 2
        table_name str
            to be passed as parameter 3
        
        Returns
        ---
        result: Any
        """
        ...
                          
    
    def get_n_rows_from_tables_below(self, n : int, table_name : str) -> Any:
        """get_n_rows_from_tables_below has the following params
        
        Parameters
        ---
            
        n int
            to be passed as parameter 2
        table_name str
            to be passed as parameter 3
        
        Returns
        ---
        result: Any
        """
        ...
                          
    
    def table_info(self, table_name : str) -> Any:
        """table_info has the following params
        
        Parameters
        ---
            
        table_name str
            to be passed as parameter 2
        
        Returns
        ---
        result: Any
        """
        ...
                          
    
    def get_table_names(self) -> List[str]:
        """get_table_names has the following params
        """
        ...        
                  
    
    def get_value_by_column_name(self, row_index : int, column_name : str, table_name : str) -> Any:
        """get_value_by_column_name has the following params
        
        Parameters
        ---
            
        row_index int
            to be passed as parameter 2
        column_name str
            to be passed as parameter 3
        table_name str
            to be passed as parameter 4
        
        Returns
        ---
        result: Any
        """
        ...
                          
    
    def get_value_by_column_index(self, row_index : int, column_index : int, table_name : str) -> Any:
        """get_value_by_column_index has the following params
        
        Parameters
        ---
            
        row_index int
            to be passed as parameter 2
        column_index int
            to be passed as parameter 3
        table_name str
            to be passed as parameter 4
        
        Returns
        ---
        result: Any
        """
        ...
                          
    
    def delete_table(self, table_name : str) -> Any:
        """delete_table has the following params
        
        Parameters
        ---
            
        table_name str
            to be passed as parameter 2
        
        Returns
        ---
        result: Any
        """
        ...
                          
    
    def append_row(self, row : List[List[Any]], table_name : str) -> None:
        """append_row has the following params
        
        Parameters
        ---
            
        row List[List[Any]]
            to be passed as parameter 2
        table_name str
            to be passed as parameter 3
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def update_rows(self) -> None:
        """update_rows has the following params
        """
        ...        
                  
    
    def delete_rows(self, rows : List[int], table_name : str) -> None:
        """delete_rows has the following params
        
        Parameters
        ---
            
        rows List[int]
            to be passed as parameter 2
        table_name str
            to be passed as parameter 3
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def put_column(self, column_name : str, column_values : List[Any], table_name : str) -> None:
        """put_column has the following params
        
        Parameters
        ---
            
        column_name str
            to be passed as parameter 2
        column_values List[Any]
            to be passed as parameter 3
        table_name str
            to be passed as parameter 4
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def insert_column(self, column_index : int, column_name : str, column_values : List[Any], table_name : str) -> None:
        """insert_column has the following params
        
        Parameters
        ---
            
        column_index int
            to be passed as parameter 2
        column_name str
            to be passed as parameter 3
        column_values List[Any]
            to be passed as parameter 4
        table_name str
            to be passed as parameter 5
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def delete_columns(self, columns : List[str], table_name : str) -> Any:
        """delete_columns has the following params
        
        Parameters
        ---
            
        columns List[str]
            to be passed as parameter 2
        table_name str
            to be passed as parameter 3
        
        Returns
        ---
        result: Any
        """
        ...
                          