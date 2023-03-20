
import pytest
from exceldatabase import ExcelDatabase

print("Testing:" + ExcelDatabase.__doc__)
        
    @pytest.mark.parametrize(,str,[
        (,str),
        (None,[],str),
        ("","",str),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_filename():
        """test the `filename` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        str
        """
        test_result = self.test_client.filename()
        self.assertEqual(type(test_result),type(str)) 
    
    @pytest.mark.parametrize(,DataFrame,[
        (,DataFrame),
        (None,[],DataFrame),
        ("","",DataFrame),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_database():
        """test the `database` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        DataFrame
        """
        test_result = self.test_client.database()
        self.assertEqual(type(test_result),type(DataFrame)) 
    
    @pytest.mark.parametrize(,None,[
        (,None),
        (None,[],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_database_info():
        """test the `database_info` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        None
        """
        test_result = self.test_client.database_info()
        self.assertEqual(type(test_result),type(None)) 
    
    @pytest.mark.parametrize(table,table_name,message,None,[
        (table,table_name,message,None),
        (None,['table'],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io__pp(table,table_name,message):
        """test the `_pp` method which accepts the following arguments:
        
        Parameters
        ----------
        table : DataFrame, table_name : str, message : str

        Returns
        -------
        None
        """
        test_result = self.test_client._pp(table,table_name,message)
        self.assertEqual(type(test_result),type(None)) 
    
    @pytest.mark.parametrize(table_name,columns,rows,None,[
        (table_name,columns,rows,None),
        (None,['table_name'],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_create_table(table_name,columns,rows):
        """test the `create_table` method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str, columns : List[str], rows : List[List[Any]]

        Returns
        -------
        None
        """
        test_result = self.test_client.create_table(table_name,columns,rows)
        self.assertEqual(type(test_result),type(None)) 
    
    @pytest.mark.parametrize(table_name,DataFrame,[
        (table_name,DataFrame),
        (None,[],DataFrame),
        ("","",DataFrame),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table(table_name):
        """test the `get_table` method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
        DataFrame
        """
        test_result = self.test_client.get_table(table_name)
        self.assertEqual(type(test_result),type(DataFrame)) 
    
    @pytest.mark.parametrize(,DataFrame,[
        (,DataFrame),
        (None,[],DataFrame),
        ("","",DataFrame),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_query_table():
        """test the `query_table` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        DataFrame
        """
        test_result = self.test_client.query_table()
        self.assertEqual(type(test_result),type(DataFrame)) 
    
    @pytest.mark.parametrize(columns,table_name,index,Any,[
        (columns,table_name,index,Any),
        (None,['columns'],Any),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table_slice(columns,table_name,index):
        """test the `get_table_slice` method which accepts the following arguments:
        
        Parameters
        ----------
        columns : Union[str,List[str]], table_name : str, index : Optional[Tuple[int,int]]=None

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_table_slice(columns,table_name,index)
        self.assertEqual(type(test_result),type(Any)) 
    
    @pytest.mark.parametrize(n,table_name,Any,[
        (n,table_name,Any),
        (None,[],Any),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_n_rows_from_tables_above(n,table_name):
        """test the `get_n_rows_from_tables_above` method which accepts the following arguments:
        
        Parameters
        ----------
        n : int, table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_n_rows_from_tables_above(n,table_name)
        self.assertEqual(type(test_result),type(Any)) 
    
    @pytest.mark.parametrize(n,table_name,Any,[
        (n,table_name,Any),
        (None,[],Any),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_n_rows_from_tables_below(n,table_name):
        """test the `get_n_rows_from_tables_below` method which accepts the following arguments:
        
        Parameters
        ----------
        n : int, table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_n_rows_from_tables_below(n,table_name)
        self.assertEqual(type(test_result),type(Any)) 
    
    @pytest.mark.parametrize(table_name,Any,[
        (table_name,Any),
        (None,[],Any),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_table_info(table_name):
        """test the `table_info` method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.table_info(table_name)
        self.assertEqual(type(test_result),type(Any)) 
    
    @pytest.mark.parametrize(,List[str],[
        (,List[str]),
        (None,[],List[str]),
        ("","",List[str]),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_table_names():
        """test the `get_table_names` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        List[str]
        """
        test_result = self.test_client.get_table_names()
        self.assertEqual(type(test_result),type(List[str])) 
    
    @pytest.mark.parametrize(row_index,column_name,table_name,Any,[
        (row_index,column_name,table_name,Any),
        (None,['row_index'],Any),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_value_by_column_name(row_index,column_name,table_name):
        """test the `get_value_by_column_name` method which accepts the following arguments:
        
        Parameters
        ----------
        row_index : int, column_name : str, table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_value_by_column_name(row_index,column_name,table_name)
        self.assertEqual(type(test_result),type(Any)) 
    
    @pytest.mark.parametrize(row_index,column_index,table_name,Any,[
        (row_index,column_index,table_name,Any),
        (None,['row_index'],Any),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_value_by_column_index(row_index,column_index,table_name):
        """test the `get_value_by_column_index` method which accepts the following arguments:
        
        Parameters
        ----------
        row_index : int, column_index : int, table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.get_value_by_column_index(row_index,column_index,table_name)
        self.assertEqual(type(test_result),type(Any)) 
    
    @pytest.mark.parametrize(table_name,Any,[
        (table_name,Any),
        (None,[],Any),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_table(table_name):
        """test the `delete_table` method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.delete_table(table_name)
        self.assertEqual(type(test_result),type(Any)) 
    
    @pytest.mark.parametrize(row,table_name,None,[
        (row,table_name,None),
        (None,[],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_append_row(row,table_name):
        """test the `append_row` method which accepts the following arguments:
        
        Parameters
        ----------
        row : List[List[Any]], table_name : str

        Returns
        -------
        None
        """
        test_result = self.test_client.append_row(row,table_name)
        self.assertEqual(type(test_result),type(None)) 
    
    @pytest.mark.parametrize(,None,[
        (,None),
        (None,[],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_update_rows():
        """test the `update_rows` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        None
        """
        test_result = self.test_client.update_rows()
        self.assertEqual(type(test_result),type(None)) 
    
    @pytest.mark.parametrize(rows,table_name,None,[
        (rows,table_name,None),
        (None,[],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_rows(rows,table_name):
        """test the `delete_rows` method which accepts the following arguments:
        
        Parameters
        ----------
        rows : List[int], table_name : str

        Returns
        -------
        None
        """
        test_result = self.test_client.delete_rows(rows,table_name)
        self.assertEqual(type(test_result),type(None)) 
    
    @pytest.mark.parametrize(column_name,column_values,table_name,None,[
        (column_name,column_values,table_name,None),
        (None,['column_name'],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_put_column(column_name,column_values,table_name):
        """test the `put_column` method which accepts the following arguments:
        
        Parameters
        ----------
        column_name : str, column_values : List[Any], table_name : str

        Returns
        -------
        None
        """
        test_result = self.test_client.put_column(column_name,column_values,table_name)
        self.assertEqual(type(test_result),type(None)) 
    
    @pytest.mark.parametrize(column_index,column_name,column_values,table_name,None,[
        (column_index,column_name,column_values,table_name,None),
        (None,['column_index', 'column_name'],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_insert_column(column_index,column_name,column_values,table_name):
        """test the `insert_column` method which accepts the following arguments:
        
        Parameters
        ----------
        column_index : int, column_name : str, column_values : List[Any], table_name : str

        Returns
        -------
        None
        """
        test_result = self.test_client.insert_column(column_index,column_name,column_values,table_name)
        self.assertEqual(type(test_result),type(None)) 
    
    @pytest.mark.parametrize(columns,table_name,Any,[
        (columns,table_name,Any),
        (None,[],Any),
        ("","",Any),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete_columns(columns,table_name):
        """test the `delete_columns` method which accepts the following arguments:
        
        Parameters
        ----------
        columns : List[str], table_name : str

        Returns
        -------
        Any
        """
        test_result = self.test_client.delete_columns(columns,table_name)
        self.assertEqual(type(test_result),type(Any)) 
    