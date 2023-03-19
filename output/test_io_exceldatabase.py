
import unittest
from exceldatabase import ExcelDatabase

print("Testing:" + ExcelDatabase.__doc__)
        

class Test_ExcelDatabase(unittest.TestCase):        
    """"""
        
    def setUp(self):
        self.test_client = ExcelDatabase(
            filename
        )
        
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_filename(self,*args):
        """
        test the filename method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          str
        """
        test_result = self.test_client.filename(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_database(self,*args):
        """
        test the database method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          DataFrame
        """
        test_result = self.test_client.database(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_database_info(self,*args):
        """
        test the database_info method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          None
        """
        test_result = self.test_client.database_info(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io__pp(self,*args):
        """
        test the _pp method which accepts the following arguments:
        
        Parameters
        ----------
        table : DataFrame, table_name : str, message : str

        Returns
        -------
          None
        """
        test_result = self.test_client._pp(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_create_table(self,*args):
        """
        test the create_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str, columns : List[str], rows : List[List[Any]]

        Returns
        -------
          None
        """
        test_result = self.test_client.create_table(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table(self,*args):
        """
        test the get_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
          DataFrame
        """
        test_result = self.test_client.get_table(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_query_table(self,*args):
        """
        test the query_table method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          DataFrame
        """
        test_result = self.test_client.query_table(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table_slice(self,*args):
        """
        test the get_table_slice method which accepts the following arguments:
        
        Parameters
        ----------
        columns : Union[str,List[str]], table_name : str, index : Optional[Tuple[int,int]]=None

        Returns
        -------
          Any
        """
        test_result = self.test_client.get_table_slice(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_n_rows_from_tables_above(self,*args):
        """
        test the get_n_rows_from_tables_above method which accepts the following arguments:
        
        Parameters
        ----------
        n : int, table_name : str

        Returns
        -------
          Any
        """
        test_result = self.test_client.get_n_rows_from_tables_above(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_n_rows_from_tables_below(self,*args):
        """
        test the get_n_rows_from_tables_below method which accepts the following arguments:
        
        Parameters
        ----------
        n : int, table_name : str

        Returns
        -------
          Any
        """
        test_result = self.test_client.get_n_rows_from_tables_below(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_table_info(self,*args):
        """
        test the table_info method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
          Any
        """
        test_result = self.test_client.table_info(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table_names(self,*args):
        """
        test the get_table_names method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          List[str]
        """
        test_result = self.test_client.get_table_names(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_value_by_column_name(self,*args):
        """
        test the get_value_by_column_name method which accepts the following arguments:
        
        Parameters
        ----------
        row_index : int, column_name : str, table_name : str

        Returns
        -------
          Any
        """
        test_result = self.test_client.get_value_by_column_name(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_value_by_column_index(self,*args):
        """
        test the get_value_by_column_index method which accepts the following arguments:
        
        Parameters
        ----------
        row_index : int, column_index : int, table_name : str

        Returns
        -------
          Any
        """
        test_result = self.test_client.get_value_by_column_index(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_table(self,*args):
        """
        test the delete_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
          Any
        """
        test_result = self.test_client.delete_table(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_append_row(self,*args):
        """
        test the append_row method which accepts the following arguments:
        
        Parameters
        ----------
        row : List[List[Any]], table_name : str

        Returns
        -------
          None
        """
        test_result = self.test_client.append_row(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_update_rows(self,*args):
        """
        test the update_rows method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          None
        """
        test_result = self.test_client.update_rows(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_rows(self,*args):
        """
        test the delete_rows method which accepts the following arguments:
        
        Parameters
        ----------
        rows : List[int], table_name : str

        Returns
        -------
          None
        """
        test_result = self.test_client.delete_rows(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_put_column(self,*args):
        """
        test the put_column method which accepts the following arguments:
        
        Parameters
        ----------
        column_name : str, column_values : List[Any], table_name : str

        Returns
        -------
          None
        """
        test_result = self.test_client.put_column(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_insert_column(self,*args):
        """
        test the insert_column method which accepts the following arguments:
        
        Parameters
        ----------
        column_index : int, column_name : str, column_values : List[Any], table_name : str

        Returns
        -------
          None
        """
        test_result = self.test_client.insert_column(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_columns(self,*args):
        """
        test the delete_columns method which accepts the following arguments:
        
        Parameters
        ----------
        columns : List[str], table_name : str

        Returns
        -------
          Any
        """
        test_result = self.test_client.delete_columns(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        