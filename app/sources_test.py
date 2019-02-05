import unittest
from .models import sources
Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of Source class
    '''
    
    def setUp(self):
        '''
        Set up metod that ill run before every test
        '''
        self.new_source = Sources('lkl','hhh','aolol','somewhere.com','abc','au')
 
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__ == '__main__':
    unittest.main()