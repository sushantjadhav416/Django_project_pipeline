import base64
from github import Github 
from pprint import pprint

G = Github()
username = input("Enter your correct account username:")
user = G.get_user(username)
for repo in user.get_repos():
    print(repo)

