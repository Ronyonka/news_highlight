class Articles:
    '''
    articles class to define sources Objects
    '''

    def __init__(self,id,title,description,author,urlToImage,publishedAt,content,url):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.url =url