import requests
from bs4 import BeautifulSoup

url = 'https://opendatascience.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

post_items = soup.find_all('div', class_='post-item')
post_item_list = []

for post_item in post_items:
    post = {}
    post['title'] = post_item.select_one('h2 a').text.strip()
    post['date'] = post_item.select_one('span.legend-default i.fa-clock-o').next_sibling.strip()
    post['excerpt'] = post_item.select_one('div.intro').text.strip()
    post_item_list.append(post)

for post in post_item_list:
    print("Title:", post['title'])
    print("Date:", post['date'])
    print("Content:", post['excerpt'])
    print("-" * 30)