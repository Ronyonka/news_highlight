import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = "https://newsapi.org/v1/sources?language=en&category={}"
    ARTICLE_API_BASE_URL =  'https://newsapi.org/v1/articles?source=the-verge&apiKey=e36d67f02d724927982d7af6a45e8483'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

# NEWS_API_KEY = 'e36d67f02d724927982d7af6a45e8483'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True