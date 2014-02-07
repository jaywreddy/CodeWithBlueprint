class CommunityManager:

    communities = {}

    def add_new_community(name):
	new_community = Community(name)
	communities[new_community.get_id()] = new_community

    def get_community_users(communityId):
	communities[communityId].get_users()

    def get_community_articles(communityId):
	communities[communityId].get_articles()

class Community:

    id = 0

    def __init__(self, name):
	self.name = name
	self.id = id
	id += 1
    	self.users = []
	self.articles = []

    def add_user(userId):
	self.users.append(userId)

    def add_article(articleId):
	self.articles.append(articleId)

    def get_id():
	return self.id

    def get_users():
	return self.users

    def get_articles():
	return self.articles
    
    def get_name():
	return self.name
