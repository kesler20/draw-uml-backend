
import unittest
import Complete

print("Testing:" + Complete.__doc__)
        

class Test_Complete(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self):
        self.test_client = Complete(
            name
        )
        
    def test_side_effects_gefqwregqw(self):
        """
        test the gefqwregqw method which accepts the following arguments:
        
        ---
        Params:
        namefeqqef : efqfeqtype

        ---
        Returns:
        - efgrqqe
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.gefqwregqw(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.gefqwregqw()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        