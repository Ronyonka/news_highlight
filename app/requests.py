from app import app
import urllib.request,json
from .models import sources

Sources = sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v1/sources'.format(sources,api_key)
    
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
        title = sources_item.get('title')
        description = sources_item.get('description')
        author = sources_item.get('author')
        publishedAt = sources_item.get('publishedAt')

       
        sources_object = Sources(id,name,title,description,author,publishedAt)
        sources_results.append(sources_object)

    return sources_results