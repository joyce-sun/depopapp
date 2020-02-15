import requests
from bs4 import BeautifulSoup
import json
import pprint



def displayCount(u_name):
    URL = 'https://www.depop.com/' + u_name + "/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='__NEXT_DATA__')
    d = json.loads(results.text)
    try:
        followerCount = d['props']['pageProps']['shop']['followers']
        print(followerCount)
    except KeyError:
        print("invalid username")


while(True):
    u_name = input("Please enter username: ")
    if (u_name == "bye"):
        exit()
    displayCount(u_name)






