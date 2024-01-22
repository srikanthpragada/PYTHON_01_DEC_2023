import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

top_10 = sorted(countries,
                key=lambda c: c['area'],
                reverse=True)[:10]
for country in top_10:
    name = country['name']['common']
    population = country['population']
    area = country['area']
    print(f"{name:50} {population:10} {area:10}" )
