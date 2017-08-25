import re

import click
import requests
from bs4 import BeautifulSoup as BS


class Core:
    _RND_URL = 'http://bash.im/random'
    _BEST_URL = 'http://bash.im/best'
    _NEWEST_URL = 'http://bash.im/'
    _ABYSS_URL = 'http://bash.im/abyss'
    _ABYSS_TOP_URL = 'http://bash.im/abysstop'
    _ABYSS_BEST_URL = 'http://bash.im/abyssbest'

    _URLS = {
        'random': _RND_URL,
        'best': _BEST_URL,
        'new': _NEWEST_URL,
        'abyss': _ABYSS_URL,
        'abyss_top': _ABYSS_TOP_URL,
        'abyss_best': _ABYSS_BEST_URL,
    }

    _ALIASES = {
        '': _URLS['random'],
        'rnd': _URLS['random'],
        'r': _URLS['random'],
        'b': _URLS['best'],
        'n': _URLS['new'],
        'a': _URLS['abyss'],
        'at': _URLS['abyss_top'],
        'ab': _URLS['abyss_best'],
    }

    def __init__(self):
        pass

    @staticmethod
    def _clean_quotes(raw_quotes):
        return [re.sub(r'(&gt;)*|(&lt;)*', '', re.sub(r'(<br\/>)', '\n', str(q)[18:-6])) for q in raw_quotes]

    def get_quotes(self, url):
        soup = BS(requests.get(url).content, 'lxml')

        quotes_raw = soup('div', class_='text')

        return self._clean_quotes(quotes_raw)

    def quote_selection(self, mode):
        pass

    def pprint(self, quotes):
        for q in quotes:
            click.echo(q)
            click.echo('-------------------------------')
