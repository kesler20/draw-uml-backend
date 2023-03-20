
import pytest
from commander import Commander

print("Testing:" + Commander.__doc__)
        
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_run():
        """
        test the `run` method which accepts the following arguments:
        
        Parameters
        ----------
        name

        Returns
        -------
        int
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.run(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.run()
        self.assertEqual(test_result,side_effect_output[0])
    
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_side_effects_execute():
        """
        test the `execute` method which accepts the following arguments:
        
        Parameters
        ----------
        n

        Returns
        -------
        list
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.execute(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.execute()
        self.assertEqual(test_result,side_effect_output[0])
    