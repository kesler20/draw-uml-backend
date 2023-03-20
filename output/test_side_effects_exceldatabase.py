
import pytest
from exceldatabase import ExcelDatabase

print("Testing:" + ExcelDatabase.__doc__)
        
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_filename():
        """
        test the `filename` method which accepts the following arguments:
        
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
    def test_side_effects_database():
        """
        test the `database` method which accepts the following arguments:
        
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
    def test_side_effects_database_info():
        """
        test the `database_info` method which accepts the following arguments:
        
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
    def test_side_effects__pp():
        """
        test the `_pp` method which accepts the following arguments:
        
        Parameters
        ----------
        table,table_name,message

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
    def test_side_effects_create_table():
        """
        test the `create_table` method which accepts the following arguments:
        
        Parameters
        ----------
        table_name,columns,rows

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
    def test_side_effects_get_table():
        """
        test the `get_table` method which accepts the following arguments:
        
        Parameters
        ----------
        table_name

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
    def test_side_effects_query_table():
        """
        test the `query_table` method which accepts the following arguments:
        
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
    def test_side_effects_get_table_slice():
        """
        test the `get_table_slice` method which accepts the following arguments:
        
        Parameters
        ----------
        columns,table_name,index

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
    def test_side_effects_get_n_rows_from_tables_above():
        """
        test the `get_n_rows_from_tables_above` method which accepts the following arguments:
        
        Parameters
        ----------
        n,table_name

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
    def test_side_effects_get_n_rows_from_tables_below():
        """
        test the `get_n_rows_from_tables_below` method which accepts the following arguments:
        
        Parameters
        ----------
        n,table_name

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
    def test_side_effects_table_info():
        """
        test the `table_info` method which accepts the following arguments:
        
        Parameters
        ----------
        table_name

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
    def test_side_effects_get_table_names():
        """
        test the `get_table_names` method which accepts the following arguments:
        
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
    def test_side_effects_get_value_by_column_name():
        """
        test the `get_value_by_column_name` method which accepts the following arguments:
        
        Parameters
        ----------
        row_index,column_name,table_name

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
    def test_side_effects_get_value_by_column_index():
        """
        test the `get_value_by_column_index` method which accepts the following arguments:
        
        Parameters
        ----------
        row_index,column_index,table_name

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
    def test_side_effects_delete_table():
        """
        test the `delete_table` method which accepts the following arguments:
        
        Parameters
        ----------
        table_name

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
    def test_side_effects_append_row():
        """
        test the `append_row` method which accepts the following arguments:
        
        Parameters
        ----------
        row,table_name

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
    def test_side_effects_update_rows():
        """
        test the `update_rows` method which accepts the following arguments:
        
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
    def test_side_effects_delete_rows():
        """
        test the `delete_rows` method which accepts the following arguments:
        
        Parameters
        ----------
        rows,table_name

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
    def test_side_effects_put_column():
        """
        test the `put_column` method which accepts the following arguments:
        
        Parameters
        ----------
        column_name,column_values,table_name

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
    def test_side_effects_insert_column():
        """
        test the `insert_column` method which accepts the following arguments:
        
        Parameters
        ----------
        column_index,column_name,column_values,table_name

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
    def test_side_effects_delete_columns():
        """
        test the `delete_columns` method which accepts the following arguments:
        
        Parameters
        ----------
        columns,table_name

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
    