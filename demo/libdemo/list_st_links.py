from bs4 import BeautifulSoup
import requests

website = "http://www.srikanthtechnologies.com/"
resp = requests.get(website)
contents = resp.text

bs = BeautifulSoup(contents, 'html.parser')

links = bs.find_all("a")

hrefs = set()
for link in links:
    href = link['href']
    if href == '#':  # ignore
        continue

    if not href.startswith("http"):
        href = website + href   # make url absolute

    hrefs.add(href)

for href in hrefs:
    print(href)
