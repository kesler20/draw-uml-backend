
import unittest
from operatingsysteminterface import OperatingSystemInterface

print("Testing:" + OperatingSystemInterface.__doc__)
        

class Test_OperatingSystemInterface(unittest.TestCase):        
    """
    
    testing the side effects of the OperatingSystemInterface class
    
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
        self.test_client = OperatingSystemInterface()
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects___init__(self):
        """
        test the __init__ method which accepts the following arguments:
        
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
        test_result = self.test_client.__init__(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.__init__()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects___enter__(self):
        """
        test the __enter__ method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
         os
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.__enter__(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.__enter__()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects___exit__(self):
        """
        test the __exit__ method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
         os
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.__exit__(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.__exit__()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_gcu(self):
        """
        test the gcu method which accepts the following arguments:
        
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
        test_result = self.test_client.gcu(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.gcu()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_copy_file_from_folder(self):
        """
        test the copy_file_from_folder method which accepts the following arguments:
        
        Parameters
        ----------
        file : str, source_folder : str="jaguar"

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.copy_file_from_folder(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.copy_file_from_folder()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_move_folder_resources(self):
        """
        test the move_folder_resources method which accepts the following arguments:
        
        Parameters
        ----------
        destination_path : str

        Returns
        -------
         None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.move_folder_resources(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.move_folder_resources()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_read_word_in_directory(self):
        """
        test the read_word_in_directory method which accepts the following arguments:
        
        Parameters
        ----------
        word : str

        Returns
        -------
         'list[str]'
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.read_word_in_directory(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.read_word_in_directory()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        