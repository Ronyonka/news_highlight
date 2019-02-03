import unittest
from .models import sources
Sources = sources.Sources

class Testsources(unittest.Testcase):
    '''
    Test class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources()