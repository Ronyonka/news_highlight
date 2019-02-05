from app import app
import urllib.request,json
from .models import sources,articles

Sources = sources.Sources
Articles = articles.Articles
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
articles_base_url = app.config["ARTICLE_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id =sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')


       
        sources_object = Sources(id,name,description)
        sources_results.append(sources_object)

    return sources_results

def get_articles(id):
    '''Function thet gets the json response to our url request'''
    get_articles_url = articles_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(article_list):
    '''
    Function that processes the airticle result and transforms them to a list of objects
    Args:
        article_list: a list of dictionaries that contain articles
    Returns:
        article_results: a list of article objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        title = article_item.get('title')
        description = article_item.get('description')
        author = article_item.get('author')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')
        url = article_item.get('url')
        if urlToImage:
            article_object = Articles(id,title,description,author,urlToImage,publishedAt,content,url)
            article_results.append(article_object)

    return article_results