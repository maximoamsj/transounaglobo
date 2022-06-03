#import modules
import requests
from bs4 import BeautifulSoup
from time import sleep
import tweepy
# keys
client = tweepy.Client(
    consumer_key = 'HhOSC03pfJEoYwHaZmAFPCyyi',
    consumer_secret = 'jDZqUGh1aVghDps4JDoRBWiGsLu2zt3oMXhBete5t7hO9eqOh3',
    access_token = '1529992664728354817-busESph0xTGM9dX2Toe1HP6we2GHhM',
    access_token_secret = '6fQBP8zokQxJumtWvin8YtOWCLNBko9Y5N939JjOFJP6L'
)

transar_lista = ['transa', 'transam', 'transava', 'transavam', 'transou', 'transaram', 'transara', 'transará', 'transarão', 'transaria', 'transariam', 'transe', 'transem', 'transasse', 'transassem', 'transar', 'transarem', 'transando', 'transado', 'faz sexo', 'fazem sexo']
url = 'http://globo.com'
response = requests.get(url)
text = response.text
data = BeautifulSoup(text, 'html.parser')
post_links = data.find_all("a", {"class": "post__link"})

print('As notícias são: ')
for x in post_links:
    text = x.text.strip()
    #print(text, x['href'])
    res = any(ele in text for ele in transar_lista)
    if res == True:
        print(text, x['href'])
        client.create_tweet(text='ALGUEM TRANSOU NA GLOBO' + '\n' + x['href'])
