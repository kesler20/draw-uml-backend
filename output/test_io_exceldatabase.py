
import pytest
from exceldatabase import ExcelDatabase

print("Testing:" + ExcelDatabase.__doc__)
        
    @staticmethod
    @pytest.mark.parametrize(,str,[
        (,str),
        (None,[],"expected_value2"),
        ("","",str),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_filename(self,*args):
        """test the filename method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        str
        """
        test_result = self.test_client.filename(,str)
        self.assertEqual(type(test_result),str) 
    
    @staticmethod
    @pytest.mark.parametrize(,DataFrame,[
        (,DataFrame),
        (None,[],"expected_value2"),
        ("","",DataFrame),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_database(self,*args):
        """test the database method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        DataFrame
        """
        test_result = self.test_client.database(,DataFrame)
        self.assertEqual(type(test_result),DataFrame) 
    
    @staticmethod
    @pytest.mark.parametrize(,None,[
        (,None),
        (None,[],"expected_value2"),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_database_info(self,*args):
        """test the database_info method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        None
        """
        test_result = self.test_client.database_info(,None)
        self.assertEqual(type(test_result),None) 
    
    @staticmethod
    @pytest.mark.parametrize(table,table_name,message,None,[
        (table,table_name,message,None),
        (None,['table'],"expected_value2"),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io__pp(self,*args):
        """test the _pp method which accepts the following arguments:
        
        Parameters
        ----------
        table : DataFrame, table_name : str, message : str

        Returns
        -------
        None
        """
        test_result = self.test_client._pp(table,table_name,message,None)
        self.assertEqual(type(test_result),None) 
    
    @staticmethod
    @pytest.mark.parametrize(table_name,columns,rows,None,[
        (table_name,columns,rows,None),
        (None,['table_name'],"expected_value2"),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_create_table(self,*args):
        """test the create_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str, columns : List[str], rows : List[List[Any]]

        Returns
        -------
        None
        """
        test_result = self.test_client.create_table(table_name,columns,rows,None)
        self.assertEqual(type(test_result),None) 
    
    @staticmethod
    @pytest.mark.parametrize(table_name,DataFrame,[
        (table_name,DataFrame),
        (None,[],"expected_value2"),
        ("","",DataFrame),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table(self,*args):
        """test the get_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
        DataFrame
        """
        test_result = self.test_client.get_table(table_name,DataFrame)
        self.assertEqual(type(test_result),DataFrame) 
    
    @staticmethod
    @pytest.mark.parametrize(,DataFrame,[
        (,DataFrame),
        (None,[],"expected_value2"),
        ("","",DataFrame),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_query_table(self,*args):
        """test the query_table method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        DataFrame
        """
        test_result = self.test_client.query_table(,DataFrame)
        self.assertEqual(type(test_result),DataFrame) 
    
    @staticmethod
    @pytest.mark.parametrize(columns,table_name,index,Any,[
        (columns,table_name,index,Any),
        (None,['columns'],"expected_value2"),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table_slice(self,*args):
        """test the get_table_slice method which accepts the following arguments:
        
        Parameters
        ----------
        columns : Union[str,List[str]], table_name : str, index : Optional[Tuple[int,int]]=None

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_table_slice(columns,table_name,index,Any)
        self.assertEqual(type(test_result),Any) 
    
    @staticmethod
    @pytest.mark.parametrize(n,table_name,Any,[
        (n,table_name,Any),
        (None,[],"expected_value2"),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_n_rows_from_tables_above(self,*args):
        """test the get_n_rows_from_tables_above method which accepts the following arguments:
        
        Parameters
        ----------
        n : int, table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_n_rows_from_tables_above(n,table_name,Any)
        self.assertEqual(type(test_result),Any) 
    
    @staticmethod
    @pytest.mark.parametrize(n,table_name,Any,[
        (n,table_name,Any),
        (None,[],"expected_value2"),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_n_rows_from_tables_below(self,*args):
        """test the get_n_rows_from_tables_below method which accepts the following arguments:
        
        Parameters
        ----------
        n : int, table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_n_rows_from_tables_below(n,table_name,Any)
        self.assertEqual(type(test_result),Any) 
    
    @staticmethod
    @pytest.mark.parametrize(table_name,Any,[
        (table_name,Any),
        (None,[],"expected_value2"),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_table_info(self,*args):
        """test the table_info method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.table_info(table_name,Any)
        self.assertEqual(type(test_result),Any) 
    
    @staticmethod
    @pytest.mark.parametrize(,List[str],[
        (,List[str]),
        (None,[],"expected_value2"),
        ("","",List[str]),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table_names(self,*args):
        """test the get_table_names method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        List[str]
        """
        test_result = self.test_client.get_table_names(,List[str])
        self.assertEqual(type(test_result),List[str]) 
    
    @staticmethod
    @pytest.mark.parametrize(row_index,column_name,table_name,Any,[
        (row_index,column_name,table_name,Any),
        (None,['row_index'],"expected_value2"),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_value_by_column_name(self,*args):
        """test the get_value_by_column_name method which accepts the following arguments:
        
        Parameters
        ----------
        row_index : int, column_name : str, table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_value_by_column_name(row_index,column_name,table_name,Any)
        self.assertEqual(type(test_result),Any) 
    
    @staticmethod
    @pytest.mark.parametrize(row_index,column_index,table_name,Any,[
        (row_index,column_index,table_name,Any),
        (None,['row_index'],"expected_value2"),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_value_by_column_index(self,*args):
        """test the get_value_by_column_index method which accepts the following arguments:
        
        Parameters
        ----------
        row_index : int, column_index : int, table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_value_by_column_index(row_index,column_index,table_name,Any)
        self.assertEqual(type(test_result),Any) 
    
    @staticmethod
    @pytest.mark.parametrize(table_name,Any,[
        (table_name,Any),
        (None,[],"expected_value2"),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_table(self,*args):
        """test the delete_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.delete_table(table_name,Any)
        self.assertEqual(type(test_result),Any) 
    
    @staticmethod
    @pytest.mark.parametrize(row,table_name,None,[
        (row,table_name,None),
        (None,[],"expected_value2"),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_append_row(self,*args):
        """test the append_row method which accepts the following arguments:
        
        Parameters
        ----------
        row : List[List[Any]], table_name : str

        Returns
        -------
        None
        """
        test_result = self.test_client.append_row(row,table_name,None)
        self.assertEqual(type(test_result),None) 
    
    @staticmethod
    @pytest.mark.parametrize(,None,[
        (,None),
        (None,[],"expected_value2"),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_update_rows(self,*args):
        """test the update_rows method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        None
        """
        test_result = self.test_client.update_rows(,None)
        self.assertEqual(type(test_result),None) 
    
    @staticmethod
    @pytest.mark.parametrize(rows,table_name,None,[
        (rows,table_name,None),
        (None,[],"expected_value2"),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_rows(self,*args):
        """test the delete_rows method which accepts the following arguments:
        
        Parameters
        ----------
        rows : List[int], table_name : str

        Returns
        -------
        None
        """
        test_result = self.test_client.delete_rows(rows,table_name,None)
        self.assertEqual(type(test_result),None) 
    
    @staticmethod
    @pytest.mark.parametrize(column_name,column_values,table_name,None,[
        (column_name,column_values,table_name,None),
        (None,['column_name'],"expected_value2"),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_put_column(self,*args):
        """test the put_column method which accepts the following arguments:
        
        Parameters
        ----------
        column_name : str, column_values : List[Any], table_name : str

        Returns
        -------
        None
        """
        test_result = self.test_client.put_column(column_name,column_values,table_name,None)
        self.assertEqual(type(test_result),None) 
    
    @staticmethod
    @pytest.mark.parametrize(column_index,column_name,column_values,table_name,None,[
        (column_index,column_name,column_values,table_name,None),
        (None,['column_index', 'column_name'],"expected_value2"),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_insert_column(self,*args):
        """test the insert_column method which accepts the following arguments:
        
        Parameters
        ----------
        column_index : int, column_name : str, column_values : List[Any], table_name : str

        Returns
        -------
        None
        """
        test_result = self.test_client.insert_column(column_index,column_name,column_values,table_name,None)
        self.assertEqual(type(test_result),None) 
    
    @staticmethod
    @pytest.mark.parametrize(columns,table_name,Any,[
        (columns,table_name,Any),
        (None,[],"expected_value2"),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_columns(self,*args):
        """test the delete_columns method which accepts the following arguments:
        
        Parameters
        ----------
        columns : List[str], table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.delete_columns(columns,table_name,Any)
        self.assertEqual(type(test_result),Any) 
    