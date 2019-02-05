class Articles:
    '''
    articles class to define sources Objects
    '''

    def __init__(self,title,author,description,urlToImage,publishedAt):
        self.title = title
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
