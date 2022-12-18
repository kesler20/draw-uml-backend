import pandas as pd
import os
from dataclasses import dataclass
from typing import List, Any, Tuple, Union, Optional, Callable
from _types import DataFrame
import openpyxl as pxl
import zipfile


@dataclass
class ExcelDatabase:
    """Excel database which is index by columns, and sheet_names
    the columns are the different columns of the table, whilst the sheet_names refer to the
    different tables in the database.
    The database is saved in the OneDrive/Documents file called protocol_database.xlsx
    """

    __filename: str = "protocol_database.xlsx"

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def database(self) -> DataFrame:
        dfs = []
        for sheet in pd.ExcelFile(self.filename).sheet_names:
            dfs.append(pd.read_excel(self.filename, sheet_name=sheet))
        df: DataFrame = pd.concat(*dfs)
        return df

    @property
    def database_info(self) -> None:
        db = self.database
        print("General Info on the Database")
        print(db.info)
        print("These are the columns")
        print(db.columns)
        print("These are the rows")
        print(db.index)
        print("This is the count")
        print(db.count)
        print("This is the database")
        print(db)

    def _pp(self, table: DataFrame, table_name: str, message: str) -> None:
        """Pretty print, a convention to display events
        """
        print(f"{message}...")
        print(f"======= {table_name} ==========")
        print(table)

    def create_table(self, table_name: str, columns: List[str], rows: List[List[Any]]) -> None:
        """Create a table from the list of rows and columns passed where the index of the list or rows
        corresponds to the index of the list of columns
        """
        # collect the existing tables
        old_dfs: List[DataFrame] = []
        for sheet_name in pd.ExcelWriter(self.filename).sheets:
            old_dfs.append(pd.read_excel(self.filename, sheet_name=sheet_name))

        # create new_df
        new_df = pd.DataFrame(data={col: rows[index]
                                    for index, col in enumerate(columns)})
        # append new df to the old df
        old_dfs.append(new_df)
        self._pp(new_df, table_name, "Creating table")

        try:
            for df in old_dfs:
                excel_book = pxl.load_workbook(self.filename)
                with pd.ExcelWriter(self.filename, engine='openpyxl') as writer:
                    writer.book = excel_book
                    writer.sheets = {
                        worksheet.title: worksheet
                        for worksheet in excel_book.worksheets
                    }
                    df.to_excel(writer, table_name, index=False)
                    writer.save()
        except zipfile.BadZipFile:

            pd.DataFrame([0]).to_excel(
                self.filename, sheet_name="genesis table")

            for df in old_dfs:
                excel_book = pxl.load_workbook(self.filename)
                with pd.ExcelWriter(self.filename, engine='openpyxl') as writer:
                    writer.book = excel_book
                    writer.sheets = {
                        worksheet.title: worksheet
                        for worksheet in excel_book.worksheets
                    }
                    df.to_excel(writer, table_name, index=False)
                    writer.save()

    def get_table(self, table_name: str) -> DataFrame:
        df: DataFrame = pd.read_excel(self.filename, sheet_name=table_name)
        return df

    def query_table(self, query: Callable[[DataFrame], Any], table_name) -> DataFrame:
        """To query the table pass a lambda expression as the query callback which takes the df
        as an argument

        Example
        ---
        this is an example of querying values greater than or equal to 2
        ```python
        # initialise the database
        db = ExcelDatabase()
        # create a random table
        db.create_table("New Table", ["data", "another data"], [
                        [1, 2, 4, 6], [2, 10, 5, 7]])
        # query the values from the data column which are greater than or qual to 2
        print(db.query_table(lambda table: table["data"] >= 2, "New Table"))
        ```

        Output
        ---
        ```txt
        ======= New Table ==========
            data  another data
        0     1             2
        1     2            10
        2     4             5
        3     6             7
            data  another data
        1     2            10
        2     4             5
        3     6             7
        ```
        """
        table = self.get_table(table_name)
        return table.loc[query(table)]

    def get_table_slice(self, columns: Union[str, List[str]], table_name: str, index: Optional[Tuple[int, int]] = None) -> Any:
        """Get a specific columns and rows of the table

        Params
        ---
        index: Optional[Tuple[int,int]]
          the index is a tuple of indices representing where you want t get the rows from and to
          this is of the form (from, to) where from and to are integers
          if left to None this will return all the rows

        columns: List[str] or str
          this is an array of strings in the event that we want to select more than one column
          this is a string if you only want to select one column
          if the column is set to "*" all columns will be considered
        """
        table = self.get_table(table_name)
        if columns == "*":
            columns = [str(col) for col in table.columns]
        if index is None:
            return table[columns]
        return table[columns].loc[index[0]:index[1]]

    def get_n_rows_from_tables_above(self, n: int, table_name: str) -> Any:
        table = self.get_table(table_name)
        return table.head(n)

    def get_n_rows_from_tables_below(self, n: int, table_name: str) -> Any:
        table = self.get_table(table_name)
        return table.tail(n)

    def table_info(self, table_name: str) -> Any:
        table = self.get_table(table_name)
        print("Table info")
        print(table.info)
        print("Table Shape")
        print(table.shape)
        print("Table axes")
        print(table.axes)

    def get_table_names(self) -> List[str]:
        return list(pd.ExcelFile(self.filename).sheet_names)

    def get_value_by_column_name(self, row_index: int, column_name: str, table_name: str) -> Any:
        table = self.get_table(table_name)
        return table.at[row_index, column_name]

    def get_value_by_column_index(self, row_index: int, column_index: int, table_name: str) -> Any:
        table = self.get_table(table_name)
        return table.iat[row_index, column_index]

    def delete_table(self, table_name: str) -> Any:
        # get all the existing data
        existing_tables: List[Tuple[str, DataFrame]] = []
        for name in self.get_table_names():
            existing_tables.append((name, self.get_table(name)))
        # remove the current database
        os.remove(self.filename)

        # re-create the database without the selected sheet
        for name, df in existing_tables:
            if name != table_name:
                df.to_excel(self.filename, sheet_name=name, index=False)

    def append_row(self, row: List[List[Any]], table_name: str) -> None:
        table = self.get_table(table_name)
        new_values = []
        values = [list(table[col]) for col in table.columns]
        # the table values is a nested list of the form [[row1],[row2],[row3]]
        # where row1,2,3 are rows of columns 1,2,3 respectively
        for i in range(len(list(values))):
            # append the new row to the list of rows
            list(values)[i].append(row[i])
            # append the list of rows to the new values
            new_values.append(values)
            
        # create a new data frame with the new values
        df = pd.DataFrame(new_values, columns=table.columns)
        self._pp(df, table_name, "Appending a new row")
        self.create_table(table_name, df.columns, new_values)

    def update_rows(self, row_index: Union[List[int], int], row_values: Union[List[int], List[List[int]]], table_name) -> None:
        """Updating 1 or more rows within the given table

        Params
        ---

        row_index: list[int] or int
          the row index can be passed as a single integer 
          of a list of integers which will update multiple rows
          with the same values or different values with the row_values array 
          is an array of arrays where 

        row_values: list[list[int]] or list[int]
          array of values or array of arrays of values (if you want to update multiple rows)
          where the length of the outer array m is equal to the number of rows you want to update
          and the length of the inner array n is the length of the data frame you want to produce  
        """
        table = self.get_table(table_name)
        if type(row_index) == int:
            table.loc[row_index] = row_values
        else:
            table.loc[[row_index]] = row_values

        self._pp(table, table_name, "Updating  rows")
        table.to_excel(self.filename,
                       sheet_name=table_name, index=False)

    def delete_rows(self, rows: List[int], table_name: str) -> None:
        table = self.get_table(table_name)
        table.drop([rows], inplace=True)
        self._pp(table, table_name, "Deleting rows")
        table.to_excel(self.filename,
                       sheet_name=table_name, index=False)

    def put_column(self, column_name: str, column_values: List[Any], table_name: str) -> None:
        table = self.get_table(table_name)
        table[column_name] = column_values
        self._pp(table, table_name, "Put a new column")
        table.to_excel(self.filename,
                       sheet_name=table_name, index=False)

    def insert_column(self, column_index: int, column_name: str, column_values: List[Any], table_name: str) -> None:
        table = self.get_table(table_name)
        table.insert(column_index, column_name, column_values)
        self._pp(table, table_name, "Appending a new column")
        table.to_excel(self.filename,
                       sheet_name=table_name, index=False)

    def delete_columns(self, columns: List[str], table_name: str) -> Any:
        table = self.get_table(table_name)
        for column in columns:
            table.pop(column)
        self._pp(table, table_name, "Deleting Columns")
        table.to_excel(self.filename,
                       sheet_name=table_name, index=False)


db = ExcelDatabase()

db.create_table("table", ["col"], [[0]])
db.append_row([[1]],"table")