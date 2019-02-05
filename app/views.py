from flask import render_template
from app import app
from .requests import get_sources
from .models import sources,articles
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to your first stop shop for news'
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    general_sources = get_sources('general')
    technology_sources = get_sources('technology')

    return render_template('index.html', title = title, business = business_sources, sports = sports_sources, technology = technology_sources, general= general_sources)

# @app.route('/articles/<id>')
# def articles(id):

#     '''
#     View movie page function that returns the source details
#     '''
    
#     return render_template('articles.html',id = id, articles = articles)
