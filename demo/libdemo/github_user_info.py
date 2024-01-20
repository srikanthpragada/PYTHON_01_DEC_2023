import requests

user = input("Enter username :")
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

details = resp.json()
print('Name        :', details['name'])
print('Location    :', details['location'])
print('Repos Count :', details['public_repos'])
