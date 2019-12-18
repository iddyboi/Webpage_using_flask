from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import requests

req = requests.get('https://www.bbc.co.uk/sport/football/gossip')
soup = BeautifulSoup(req.text, 'html.parser')
results = soup.find_all('p')
print(results[4].text)
