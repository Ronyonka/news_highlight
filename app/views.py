from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    news_sources = get_sources('sources')
    print(news_sources)
    title = "Home - If it isn't here, it probably didn't happen"
    return render_template('index.html', title = title, sources=news_sources)

@app.route('/source/<source_id>')
def movie(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',id = source_id)