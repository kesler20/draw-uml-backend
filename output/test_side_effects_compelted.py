
import unittest
from compelted import Compelted

print("Testing:" + Compelted.__doc__)
        

class Test_Compelted(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self):
        self.test_client = Compelted(this)
        
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        