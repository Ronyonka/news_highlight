import unittest
from .models import articles
Articles = articles.Articles

class SourcesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of Source class
    '''
    
    def setUp(self):
        '''
        Set up metod that ill run before every test
        '''
        self.new_article = Articles("A spacecraft carries precious cargo to a new planet in 'A Sun Will Always Sing'","Karin Lowachee","In Karin Lowachee’s original short story, a spacecraft carrying precious cargo embarks on a lifetime journey to a better world. 'A Sun Will Always Sing' is part of Better Worlds, The Verge’s science fiction project about hope.", "https://www.theverge.com/2019/2/4/18139371/karin-lowachee-sci-fi-story-video-seimei-ai-better-worlds", "2019-02-04T15:00:00Z")
 
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == '__main__':
    unittest.main()