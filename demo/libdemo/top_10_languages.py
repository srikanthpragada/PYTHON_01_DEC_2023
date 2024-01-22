from bs4 import BeautifulSoup
import requests

website = "https://www.tiobe.com/tiobe-index/"
resp = requests.get(website)
contents = resp.text

bs = BeautifulSoup(contents, 'html.parser')
table = bs.find(id="top20")  # find <table> with id top20

rows = table.tbody.find_all('tr')

for row in rows[:10]:
    cols = row.find_all('td')
    name = cols[4].text # name
    ranking = cols[5].text  # ranking
    print(f"{name:30} {ranking}")

