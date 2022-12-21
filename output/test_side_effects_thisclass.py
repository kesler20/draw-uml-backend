
import unittest
from thisclass import ThisClass

print("Testing:" + ThisClass.__doc__)
        

class Test_ThisClass(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self):
        self.test_client = ThisClass(
            value
        )
        
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        