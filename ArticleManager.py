class ArticleManager:

    def __init__(self):
        self.articles = []
        self.id_to_article = {}

    def get_article_dict(self):
        return self.id_to_article

    '''
    Returns Article Object given an ID
    '''
    def get_article_by_id(self, id):
        return self.id_to_article[id]

    def post_article(self, title, url, user_id, comm_id):
        article = Article(title, url, user_id, comm_id)
        article_id = article.get_id()
        self.id_to_article[article_id] = article
        self.articles.append(article)
        return article_id

    def upvote_article(self, article_id):
        article = self.id_to_article[article_id]
        article.upvote()

    def downvote_article(self, article_id):
        article = self.id_to_article[article_id]
        article.downvote()

    def get_article_url(self, id):
        return self.id_to_article[id].get_url()

    def get_article_title(self, id):
        return self.id_to_article[id].get_title()

    def get_article_score(self, id):
        return self.id_to_article[id].get_upvotes()
