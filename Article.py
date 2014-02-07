class Article:
    id = 0

    def __init__(self, title, url, user_id, comm_id):
        Article.id += 1

        self.upvotes = 0

        self.title = title
        self.url = url
        self.user_id = user_id
        self.comm_id = comm_id
        self.article_id = Article.id

    def upvote(self):
        self.upvotes += 1    

    def downvote(self):
        self.downvote -= 1

    def get_id(self):
        return self.article_id

    def get_user_id(self):
        return self.user_id

    def get_comm_id(self):
        return self.comm_id

    def get_upvotes(self):
        return self.upvotes

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title
        

