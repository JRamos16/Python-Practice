import requests
from bs4 import BeautifulSoup

base_url = 'https://www.nytimes.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,'html.parser')

# print(soup.contents)
print(soup.find_all("div", {"class": "css-plkyuz"}))
# for story_heading in soup.find_all(class_="indicate-hover css-on97le"):
#     print(story_heading)
