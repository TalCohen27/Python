import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
titles = soup.findAll("h2", {"class": "story-heading"})
for title in titles:
    print(str(title.text).strip())

