import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for country in countries:
    name = country['name']['common']
    region = country['region']
    capital = ",".join(country.get('capital', []))
    print(f"{name:50} {region:20} {capital}")
