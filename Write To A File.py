import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

with open('file_to_save.txt', 'w') as open_file:

    soup = BeautifulSoup(r_html, "html.parser")
    titles = soup.findAll("h2", {"class": "story-heading"})
    for title in titles:
        open_file.write(str(title.text).strip() + "\n")


