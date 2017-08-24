import re

import click
import requests
from bs4 import BeautifulSoup as BS

RND_URL = 'http://bash.im/random'
BEST_URL = 'http://bash.im/best'
NEWEST_URL = 'http://bash.im/'
ABYSS_URL = 'http://bash.im/abyss'
ABYSS_TOP_URL = 'http://bash.im/abysstop'
ABYSS_BEST_URL = 'http://bash.im/abyssbest'

URLS = {
    'random': RND_URL,
    'best': BEST_URL,
    'new': NEWEST_URL,
    'abyss': ABYSS_URL,
    'abyss_top': ABYSS_TOP_URL,
    'abyss_best': ABYSS_BEST_URL,
}

ALIASES = {
    '': URLS['random'],
    'rnd': URLS['random'],
    'r': URLS['random'],
    'b': URLS['best'],
    'n': URLS['new'],
    'a': URLS['abyss'],
    'at': URLS['abyss_top'],
    'ab': URLS['abyss_best'],
}


def get_quotes(url, amount):
    soup = BS(requests.get(url).content, 'lxml')

    quotes_raw = soup('div', class_='text')

    return [re.sub(r'(&gt;)*|(&lt;)*', '', re.sub(r'(<br\/>)', '\n', str(q)[18:-6])) for q in quotes_raw][0:amount]


def pprint(quotes):
    for q in quotes:
        click.echo(q)
        click.echo('-------------------------------')
