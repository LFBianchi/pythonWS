# scrappingoreilly.py

import requests
from bs4 import BeautifulSoup

url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

tds = soup.find_all('article', class_='SearchCard--29xc9')
print(soup.prettify())
