class CommunityManager:

    communities = {}

    def add_user_community(userId, communityId):
	communities[communityId].add_user(userId)

    def remove_user_community(userId, communityId):
	communities[communityId].remove_user(userId)

    def add_new_community(self, name):
	new_community = Community(name)
	communities[new_community.get_id()] = new_community

    def get_community_users(self, communityId):
	return communities[communityId].get_users()

    def get_community_articles(self, communityId):
	return communities[communityId].get_articles()

    def get_communities(self):
	return communities.keys()

class Community:

    id = 0

    def __init__(self, name):
	self.name = name
	self.id = id
	Community.id += 1
    	self.users = []
	self.articles = []

    def add_user(self, userId):
	self.users.append(userId)

    def remove_user(self, userId):
	self.users.remove(userId)

    def add_article(self, articleId):
	self.articles.append(articleId)

    def get_id(self):
	return self.id

    def get_users(self):
	return self.users

    def get_articles(self):
	return self.articles
    
    def get_name(self):
	return self.name
