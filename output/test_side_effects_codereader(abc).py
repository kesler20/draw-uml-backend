import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
import unittest
from codereader(abc) import CodeReader(ABC)
print("Testing:" + CodeReader(ABC).__doc__)
        
class Test_CodeReader(ABC)(unittest.TestCase):        
    """
    
    testing the side effects of the CodeReader(ABC) class
    
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
        self.test_client = CodeReader(ABC)(
            source_code_path
            ,response_code_path
        )
        
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_source_code_path(self):
        """
        test the `source_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        Path
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.source_code_path(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.source_code_path()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_response_code_path(self):
        """
        test the `response_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        Path
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.response_code_path(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.response_code_path()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_set_response_code_path(self):
        """
        test the `set_response_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        path

        Returns
        -------
        
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.set_response_code_path(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.set_response_code_path()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_set_source_code_path(self):
        """
        test the `set_source_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        path

        Returns
        -------
        
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.set_source_code_path(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.set_source_code_path()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_read(self):
        """
        test the `read` method which accepts the following arguments:
        
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
        test_result = self.test_client.read(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.read()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        