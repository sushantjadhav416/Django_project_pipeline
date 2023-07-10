import requests
from pprint import pprint

username=input("Enter your correct account username:")

url = f"https://api.github.com/users/{username}"

userdata = requests.get(url).json()

pprint(userdata['public_repos'])