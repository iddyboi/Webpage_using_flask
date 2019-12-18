# from bs4 import BeautifulSoup
# from urllib.request import urlopen as uReq
# import requests

# req = requests.get('https://www.bbc.co.uk/sport/football/gossip')
# soup = BeautifulSoup(req.text, 'html.parser')
# results = soup.find_all('p')
# print(results[4].text)
import requests

url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

querystring = {"font": "Impact", "font_size": "50",
               "meme": "Condescending-Wonka", "top": "Top text", "bottom": "Bottom text"}

headers = {
    'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
