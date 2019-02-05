from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to your first stop shop for news'
    news_sources = get_sources('sources')
    return render_template('index.html', title = title,news_sources = news_sources)

@app.route('/source/<int:source_id>')
def news(source_id):

    '''
    View movie page function that returns the source details
    '''
    title = 'Home - Welcome to your first stop shop for news'
    return render_template('news.html',title= title,id = source_id)
