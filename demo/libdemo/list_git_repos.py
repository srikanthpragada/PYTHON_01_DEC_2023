import requests

user = input("Enter username :")
resp = requests.get(f"https://api.github.com/users/{user}/repos")
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

repos = resp.json()   # Get list of dict

for repo in repos:
    print(repo['name'])
    print(repo['description'])
    print('=' * 50)



