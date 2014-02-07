from CommunityManager import CommunityManager
from UserManager import UserManager
from ArticleManager import ArticleManager

class Framework:

	def __init__(self):
		self.article_manager = ArticleManager()
		self.community_manager = CommunityManager()
		self.user_manager = UserManager()

	# def get_article_by_id(self, aid):
	# 	return self.article_manager.get_article_by_id(aid)

	# Article methods
	def get_articles(self):
		return self.user_manager.get_articles()

	def get_article_url(self, aid):
		return self.user_manager.get_article_url(aid)

	def get_article_title(self, aid):
		return self.article_manager.get_article_title(aid)

	def get_article_score(self, aid):
		return self.article_manager.get_article_score(aid)

	def post_article(self, title, url, uid, cid):
		aid = self.article_manager.post_article(title, url, uid, cid)
		self.community_manager.post_article(uid, aid)
		self.user_manager.add_user_article(uid, aid)

	def upvote(self, aid):
		self.article_manager.upvote(aid)

	def downvote(self, aid):
		self.article_manager.downvote(aid)

	def get_top_articles(self):
		aids = self.get_articles()
		top_aids = rank_articles(aids)[:20]
		return get_articles(top_aids)

	def get_random_article(self):
		return self.article_manager.get_random_article()

	# User methods
	def add_user(self, username):
		return self.user_manager.add_user(username)

	def get_users(self):
		return self.user_manager.get_all_users()

	def get_user_communities(self, uid):
		return self.user_manager.get_user_communities(self, uid)

	def get_user_articles(self, uid):
		aids = self.user_manager.get_user_articles(uid)
		return self.get_articles(aids)

	def add_user_community(self, uid, cid):
		self.user_manager.add_user_community(uid, cid)
		self.community_manager.add_user_community(uid, cid)

	def remove_user_community(self, uid, cid):
		self.user_manager.remove_user_community(uid, cid)
		self.community_manager.remove_user_community(uid, cid)

	# Community methods
	def get_communities(self):
		return self.community_manager.get_communityIds()

	def add_community(self, name):
		self.community_manager.add_new_community(name)

	def get_community_users(self, cid):
		return self.community_manager.get_community_users(cid)

	def get_community_articles(self, cid):
		aids = self.community_manager.get_community_articles(cid)
		return self.get_articles(aids)

	# Helper methods
	def rank_articles(aids): 
		return sorted(aids, key=self.get_article_score)

	def get_articles(self, aids):
		articles = []
		for aid in aids:
			article = (self.get_article_title(aid), self.get_article_url(aid), self.get_article_score(aid))
			articles.append(article)
		return articles

if __name__ == '__main__':
	import IPython; IPython.embed()
