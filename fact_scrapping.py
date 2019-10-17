import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.unkno.com/')

soup = BeautifulSoup(response.content, 'html.parser')
facts = soup.find_all('div', id='content')

print(facts[0].getText())