import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
import unittest
from databaseinterface import DatabaseInterface
print("Testing:" + DatabaseInterface.__doc__)
        
class Test_DatabaseInterface(unittest.TestCase):        
    """This is the interface to the database of the wiz_app system (the resourcemanager). 

To get started import the database and the valid modes of the database from the business rules.

```python
from wiz_app_connector.infrastructure.db.wiz_app_db import DatabaseInterface
from wiz_app_connector.domain.business_rules import ValidDatabaseMode
# setup a database with a development mode
db = DatabaseInterface("v1",ValidDatabaseMode.DEV)

# send a post request
db.use_url(endpoint="sensor").create(body={})
    
    testing the side effects of the DatabaseInterface class
    
    Example 
    -------
    How those tests are run
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
        self.test_client = DatabaseInterface(
            version
            ,mode
        )
        
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_create(self):
        """
        test the `create` method which accepts the following arguments:
        
        Parameters
        ----------
        body

        Returns
        -------
        dict
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.create(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.create()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_read(self):
        """
        test the `read` method which accepts the following arguments:
        
        Parameters
        ----------
        name

        Returns
        -------
        dict
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.read(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.read()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_update(self):
        """
        test the `update` method which accepts the following arguments:
        
        Parameters
        ----------
        name

        Returns
        -------
        dict
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.update(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.update()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_delete(self):
        """
        test the `delete` method which accepts the following arguments:
        
        Parameters
        ----------
        name

        Returns
        -------
        dict
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.delete(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.delete()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        