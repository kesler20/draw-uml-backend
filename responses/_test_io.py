
import unittest
import Complete

print("Testing:" + Complete.__doc__)
        

class Test_Complete(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self):
        self.test_client = Complete(
            name
        )
        
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        