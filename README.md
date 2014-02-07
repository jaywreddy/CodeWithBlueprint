CodeWithBlueprint
=================
Our Blueprint app

https://github.com/jaywreddy/CodeWithBlueprint.git

We created a simple command line interface for Blu-Frame.
Our design is hierarchically structured, with a central Manager (framework.py) that handles interaction between the between the three Managers (UserManager, CommunityManager, and ArticleManager). Each other respective managers handles the user, community, and article objects internally.

Usage:
    To view all the functions, type “h”
    
Community (Martin)
- id’s
- users
- articles
#CommunityManager.py

Article: (Michelle)
#Article.py
- constructor: Article(title, url, user_id, comm_id)
- upvote()
- downvote()
- get_id
- get_user_id
- get_comm_id
- get_upvotes()
- get_url()
- get_title()

#ArticleManager.py
- dictionary of ids to article object : id_to_articles
- get_article_url(id)
- get_article_title(id)
- get_article_score(id)
- get_random_article()
- post_article(title, url, user_id, comm_id) → return article_id
- upvote(id) --> None
- downvote(id) --> None

User class: (Jay)
- username
- password
- articles - list of id’s
- communities - list of id’s
- post(Community, *link to article*)
- upvote
- downvote

#User.py
UserManager API: (John)
    def add_user(self, username):

    def add_user_article(self, user_id, article_id):

    def get_user_articles(self, user_id):

    def add_user_community(self, user_id, community_id):

    def get_user_communities(self, user_id):

    def remove_user_community(self, user_id, community_id):


def rank_articles(article_ids): 
    return sorted(article_ids, key=self.get_article_score)


