
import unittest
from exceldatabase import ExcelDatabase

print("Testing:" + ExcelDatabase.__doc__)
        

class Test_ExcelDatabase(unittest.TestCase):        
    ''''''
        
    def setUp(self):
        self.test_client = ExcelDatabase(
            filename
        )
        
    def test_io_filename(self):
        """
        test the filename method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - str
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.filename(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.filename(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.filename(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.filename(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_database(self):
        """
        test the database method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - DataFrame
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.database(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.database(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.database(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.database(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_database_info(self):
        """
        test the database_info method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.database_info(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.database_info(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.database_info(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.database_info(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io__pp(self):
        """
        test the _pp method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client._pp(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client._pp(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client._pp(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client._pp(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_create_table(self):
        """
        test the create_table method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.create_table(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.create_table(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.create_table(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.create_table(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_table(self):
        """
        test the get_table method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - DataFrame
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.get_table(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_table(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.get_table(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_table(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_query_table(self):
        """
        test the query_table method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - DataFrame
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.query_table(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.query_table(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.query_table(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.query_table(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_table_slice(self):
        """
        test the get_table_slice method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.get_table_slice(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_table_slice(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.get_table_slice(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_table_slice(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_n_rows_from_tables_above(self):
        """
        test the get_n_rows_from_tables_above method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.get_n_rows_from_tables_above(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_n_rows_from_tables_above(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.get_n_rows_from_tables_above(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_n_rows_from_tables_above(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_n_rows_from_tables_below(self):
        """
        test the get_n_rows_from_tables_below method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.get_n_rows_from_tables_below(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_n_rows_from_tables_below(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.get_n_rows_from_tables_below(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_n_rows_from_tables_below(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_table_info(self):
        """
        test the table_info method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.table_info(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.table_info(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.table_info(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.table_info(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_table_names(self):
        """
        test the get_table_names method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - List[str]
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.get_table_names(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_table_names(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.get_table_names(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_table_names(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_value_by_column_name(self):
        """
        test the get_value_by_column_name method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.get_value_by_column_name(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_value_by_column_name(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.get_value_by_column_name(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_value_by_column_name(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_value_by_column_index(self):
        """
        test the get_value_by_column_index method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.get_value_by_column_index(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_value_by_column_index(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.get_value_by_column_index(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_value_by_column_index(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_delete_table(self):
        """
        test the delete_table method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.delete_table(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.delete_table(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.delete_table(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.delete_table(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_append_row(self):
        """
        test the append_row method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.append_row(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.append_row(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.append_row(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.append_row(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_update_rows(self):
        """
        test the update_rows method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.update_rows(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.update_rows(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.update_rows(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.update_rows(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_delete_rows(self):
        """
        test the delete_rows method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.delete_rows(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.delete_rows(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.delete_rows(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.delete_rows(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_put_column(self):
        """
        test the put_column method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.put_column(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.put_column(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.put_column(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.put_column(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_insert_column(self):
        """
        test the insert_column method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.insert_column(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.insert_column(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.insert_column(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.insert_column(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_delete_columns(self):
        """
        test the delete_columns method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.delete_columns(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.delete_columns(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.delete_columns(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.delete_columns(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        