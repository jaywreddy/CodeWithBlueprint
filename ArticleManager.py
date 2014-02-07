import Article, random

class ArticleManager:

    def __init__(self):
        self.article_ids = []
        self.id_to_article = {}

    def get_article_dict(self):
        return self.id_to_article

    '''
    Returns the list of all article id's
    '''
    def get_articles(self):
        return self.article_ids

    def get_article_url(self, id):
        return self.id_to_article[id].get_url()

    def get_article_title(self, id):
        return self.id_to_article[id].get_title()

    def get_article_score(self, id):
        return self.id_to_article[id].get_upvotes()

    def post_article(self, title, url, user_id, comm_id):
        article = Article(title, url, user_id, comm_id)
        article_id = article.get_id()
        self.id_to_article[article_id] = article
        self.article_ids.append(article_id)
        return article_id

    def upvote(self, article_id):
        article = self.id_to_article[article_id]
        article.upvote()

    def downvote(self, article_id):
        article = self.id_to_article[article_id]
        article.downvote()

    def get_random_article(self):
        rand_int = random.randint(1, len(self.article_ids))
        return self.id_to_article(rand_int)
