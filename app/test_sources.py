import unittest
from .models import sources
Sources = sources.Sources

class Testsources(unittest.TestCase):
    '''
    Test class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(3159,'mpasho','willy Paul did somethihng today','something.com','some category','some country')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__ == '__main__':
    unittest.main()