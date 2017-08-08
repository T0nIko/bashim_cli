import requests, re

from bs4 import BeautifulSoup as BS

RND_URL = 'http://bash.im/random'
BEST_URL = 'http://bash.im/best'
NEWEST_URL = 'http://bash.im/'
ABYSS_URL = 'http://bash.im/abyss'
ABYSS_TOP_URL = 'http://bash.im/abysstop'
ABYSS_BEST_URL = 'http://bash.im/abyssbest'


def get_quotes(url):
    soup = BS(requests.get(url).content, 'lxml')

    quotes_raw = soup('div', class_='text')

    return [re.sub(r'(<br\/>)', '\n', str(q)[18:-6]) for q in quotes_raw]


get_quotes(NEWEST_URL)
