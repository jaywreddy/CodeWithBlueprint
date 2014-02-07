class UserManager:
    def __init__(self):
	self.users= {}

    def add_user(self, user_id):
        self.users[user_id] = {'articles':[], 'communities':[]}
        return True

    def add_user_article(self, user_id, article_id):
        self.users[user_id]['articles'].append(article_id)
        return True

    def get_user_articles(self, user_id):
        return set(self.users[user_id]['articles'])

    def add_user_community(self, user_id, community_id):
        return self.users[user_id]['communities'].append(community_id)
        return True

    def get_user_communities(self, user_id):
        return set(self.users[user_id]['communities'])

    def remove_user_community(self, user_id, community_id):
        if community_id in self.users[user_id]['communities']:
            self.users[user_id]['communities'].remove(community_id)
        return True        
