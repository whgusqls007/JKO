from newspaper import Article

class CrawlingNewspaper():
    def __init__(self):
        pass

    def getArticle(self, url):
        article = Article(url, language='ko')
        article.download()
        article.parse()
        return article

