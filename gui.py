from framework import Framework


fame= Framework()
print("Welcome to Blu-Fame")

user_id = ""
def check_login():
    if user_id != "":
        return True
    else:
        print("Not Logged In !!!!")
        return False


while(True):
    cmd = raw_input("Main Menu:").split()
    if(cmd[0] == "h"):
       print(""" 
Commands:
register <user_name>
login <user_name>
my_articles 
my_communities
community_feed <community_name>
join <community_name>
community_users <community_name>
post <article_title> <url> <community>
       """)
    elif(cmd[0]=="register"):
        user_id = cmd[1]


    elif(cmd[0] == "login"):
        user_id = cmd[1] 
    elif(cmd[0] == "my_articles"):
        if not check_login(): break
        print(fame.get_user_articles(user_id))
    elif(cmd[0] == "my_communities"):
        if not check_login(): break
        print(fame.get_user_communties(user_id))
    elif(cmd[0] == "community_feed"):
        com_id = cmd[1]
        print(fame.rank_articles(com_id))
  
    elif(cmd[0] == "community_users"):
        com_id = cmd[1]
        print(fame.get_community_users(com_id))

    elif(cmd[0] == "post"):
        if not check_login(): break
        title = cmd[1]
        url = cmd[2]
        community = cmd[3]
        fame.post_article(title, url, user_id, community)

    elif(cmd[0] == "join"):
        if not check_login(): break
        com_id = cmd[1]
        fame.add_user_community(user_id, com_id)
        print("welcome to "+com_id)
       

    else:
        print("Help: h")
