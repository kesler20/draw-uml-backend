
import unittest
from exceldatabase import ExcelDatabase

print("Testing:" + ExcelDatabase.__doc__)
        
if __name == "__main__":
    exceldatabase = ExcelDatabase()
    
    exceldatabase.filename(self)
                
    exceldatabase.database(self)
                
    exceldatabase.database_info(self)
                
    exceldatabase._pp(self, table, table_name, message)
                
    exceldatabase.create_table(self, table_name, columns, rows)
                
    exceldatabase.get_table(self, table_name)
                
    exceldatabase.query_table(self)
                
    exceldatabase.get_table_slice(self, columns, table_name, index)
                
    exceldatabase.get_n_rows_from_tables_above(self, n, table_name)
                
    exceldatabase.get_n_rows_from_tables_below(self, n, table_name)
                
    exceldatabase.table_info(self, table_name)
                
    exceldatabase.get_table_names(self)
                
    exceldatabase.get_value_by_column_name(self, row_index, column_name, table_name)
                
    exceldatabase.get_value_by_column_index(self, row_index, column_index, table_name)
                
    exceldatabase.delete_table(self, table_name)
                
    exceldatabase.append_row(self, row, table_name)
                
    exceldatabase.update_rows(self)
                
    exceldatabase.delete_rows(self, rows, table_name)
                
    exceldatabase.put_column(self, column_name, column_values, table_name)
                
    exceldatabase.insert_column(self, column_index, column_name, column_values, table_name)
                
    exceldatabase.delete_columns(self, columns, table_name)
                
        