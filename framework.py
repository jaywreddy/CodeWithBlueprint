class Framework:

	def __init__(self):
		self.article_manager = ArticleManager()
		self.community_manager = CommunityManager()
		self.user_manager = UserManager()

	def get_user_id(self, username):
		return self.user_manager.get_user(user_name)

	def add_user(self, username, password):
		return self.user_manager.add_user(username, password)

	# def get_article_by_id(self, aid):
	# 	return self.article_manager.get_article_by_id(aid)

	def get_user_by_id(self, uid):
		return self.article_manager.get_user_by_id(uid)


	# Article methods

	def get_article_url(self, aid):
		return self.user_manager.get_article_url(aid)

	def get_article_title(self, aid):
		return self.article_manager.get_article_title(aid)

	def get_article_score(self, aid):
		return self.article_manager.get_article_score(aid)

	def get_community_articles(self, cid):
		return self.article_manager.get_community_articles(cid)

	def get_user_articles(self, uid):
		return self.article_manager.get_user_articles(uid)

	def post_article(self, title, url, uid, cid):
		aid = self.article_manager.post_article(title, url, uid, cid)
		self.community_manager.post_article(uid, aid)
		self.user_manager.post_article(uid, aid)

	def upvote(self, aid):
		self.article_manager.upvote(aid)

	def downvote(self, aid):
		self.article_manager.downvote(aid)

	def get_user_communities(self, uid):
		self.user_manager.get_user_communities(self, uid)

	def add_user_community(self, uid, cid):
		self.user_manager.add_user_community(uid, cid)
		self.community_manager.add_user_community(uid, cid)

	

