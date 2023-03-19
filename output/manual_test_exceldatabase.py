
import unittest
from exceldatabase import ExcelDatabase

print("Testing:" + ExcelDatabase.__doc__)
        
if __name__ == "__main__":
    exceldatabase = ExcelDatabase()
    
    exceldatabase.filename()
                
    exceldatabase.database()
                
    exceldatabase.database_info()
                
    exceldatabase._pp(table, table_name, message)
                
    exceldatabase.create_table(table_name, columns, rows)
                
    exceldatabase.get_table(table_name)
                
    exceldatabase.query_table()
                
    exceldatabase.get_table_slice(columns, table_name, index)
                
    exceldatabase.get_n_rows_from_tables_above(n, table_name)
                
    exceldatabase.get_n_rows_from_tables_below(n, table_name)
                
    exceldatabase.table_info(table_name)
                
    exceldatabase.get_table_names()
                
    exceldatabase.get_value_by_column_name(row_index, column_name, table_name)
                
    exceldatabase.get_value_by_column_index(row_index, column_index, table_name)
                
    exceldatabase.delete_table(table_name)
                
    exceldatabase.append_row(row, table_name)
                
    exceldatabase.update_rows()
                
    exceldatabase.delete_rows(rows, table_name)
                
    exceldatabase.put_column(column_name, column_values, table_name)
                
    exceldatabase.insert_column(column_index, column_name, column_values, table_name)
                
    exceldatabase.delete_columns(columns, table_name)
                
        