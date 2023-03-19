
import unittest
from exceldatabase import ExcelDatabase

print("Testing:" + ExcelDatabase.__doc__)
        

class Test_ExcelDatabase(unittest.TestCase):        
    """
    
    testing the side effects of the ExcelDatabase class
    
    Example of how those tests are run
    ---
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
        self.test_client = ExcelDatabase(
            filename
        )
        
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_filename(self):
        """
        test the filename method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
         str
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.filename(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.filename()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_database(self):
        """
        test the database method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
         DataFrame
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.database(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.database()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_database_info(self):
        """
        test the database_info method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.database_info(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.database_info()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects__pp(self):
        """
        test the _pp method which accepts the following arguments:
        
        Parameters
        ----------
        table : DataFrame, table_name : str, message : str

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client._pp(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client._pp()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_create_table(self):
        """
        test the create_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str, columns : List[str], rows : List[List[Any]]

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.create_table(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.create_table()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_get_table(self):
        """
        test the get_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
         DataFrame
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_table(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_table()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_query_table(self):
        """
        test the query_table method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
         DataFrame
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.query_table(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.query_table()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_get_table_slice(self):
        """
        test the get_table_slice method which accepts the following arguments:
        
        Parameters
        ----------
        columns : Union[str,List[str]], table_name : str, index : Optional[Tuple[int,int]]=None

        Returns
        -------
         Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_table_slice(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_table_slice()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_get_n_rows_from_tables_above(self):
        """
        test the get_n_rows_from_tables_above method which accepts the following arguments:
        
        Parameters
        ----------
        n : int, table_name : str

        Returns
        -------
         Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_n_rows_from_tables_above(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_n_rows_from_tables_above()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_get_n_rows_from_tables_below(self):
        """
        test the get_n_rows_from_tables_below method which accepts the following arguments:
        
        Parameters
        ----------
        n : int, table_name : str

        Returns
        -------
         Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_n_rows_from_tables_below(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_n_rows_from_tables_below()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_table_info(self):
        """
        test the table_info method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
         Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.table_info(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.table_info()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_get_table_names(self):
        """
        test the get_table_names method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
         List[str]
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_table_names(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_table_names()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_get_value_by_column_name(self):
        """
        test the get_value_by_column_name method which accepts the following arguments:
        
        Parameters
        ----------
        row_index : int, column_name : str, table_name : str

        Returns
        -------
         Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_value_by_column_name(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_value_by_column_name()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_get_value_by_column_index(self):
        """
        test the get_value_by_column_index method which accepts the following arguments:
        
        Parameters
        ----------
        row_index : int, column_index : int, table_name : str

        Returns
        -------
         Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_value_by_column_index(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_value_by_column_index()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_delete_table(self):
        """
        test the delete_table method which accepts the following arguments:
        
        Parameters
        ----------
        table_name : str

        Returns
        -------
         Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.delete_table(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.delete_table()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_append_row(self):
        """
        test the append_row method which accepts the following arguments:
        
        Parameters
        ----------
        row : List[List[Any]], table_name : str

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.append_row(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.append_row()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_update_rows(self):
        """
        test the update_rows method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.update_rows(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.update_rows()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_delete_rows(self):
        """
        test the delete_rows method which accepts the following arguments:
        
        Parameters
        ----------
        rows : List[int], table_name : str

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.delete_rows(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.delete_rows()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_put_column(self):
        """
        test the put_column method which accepts the following arguments:
        
        Parameters
        ----------
        column_name : str, column_values : List[Any], table_name : str

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.put_column(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.put_column()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_insert_column(self):
        """
        test the insert_column method which accepts the following arguments:
        
        Parameters
        ----------
        column_index : int, column_name : str, column_values : List[Any], table_name : str

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.insert_column(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.insert_column()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_delete_columns(self):
        """
        test the delete_columns method which accepts the following arguments:
        
        Parameters
        ----------
        columns : List[str], table_name : str

        Returns
        -------
         Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.delete_columns(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.delete_columns()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        