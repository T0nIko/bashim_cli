import re
import os
import pydoc

import bs4
import requests


class Core:
    def __init__(self):
        self.__RND_URL = 'http://bash.im/random'
        self.__BEST_URL = 'http://bash.im/best'
        self.__NEWEST_URL = 'http://bash.im/index/'
        self.__ABYSS_URL = 'http://bash.im/abyss'
        self.__ABYSS_TOP_URL = 'http://bash.im/abysstop'
        self.__ABYSS_BEST_URL = 'http://bash.im/abyssbest'

        self.__URLS = {
            'random': self.__RND_URL,
            'best': self.__BEST_URL,
            'new': self.__NEWEST_URL,
            'abyss': self.__ABYSS_URL,
            'abyss_top': self.__ABYSS_TOP_URL,
            'abyss_best': self.__ABYSS_BEST_URL,
        }

        self.__ALIASES = {
            '': self.__URLS['random'],
            'rnd': self.__URLS['random'],
            'r': self.__URLS['random'],
            'b': self.__URLS['best'],
            'n': self.__URLS['new'],
            'a': self.__URLS['abyss'],
            'at': self.__URLS['abyss_top'],
            'ab': self.__URLS['abyss_best'],
        }

        self.__DELIM = '\n--------------------------------------------------------\n'

        try:
            with open(os.path.join(os.environ['HOME'], '.bashim'), 'r') as f:
                self.current_page = int(f.readline())
                self.__NEWEST_URL += str(self.current_page)
        except:
            with open(os.path.join(os.environ['HOME'], '.bashim'), 'w') as f:
                self.current_page = int(bs4.BeautifulSoup(
                    requests.get(self.__NEWEST_URL).content,
                    'lxml'
                ).find(
                    'input',
                    class_='page'
                ).get('max'))
                self.__NEWEST_URL += str(self.current_page)
                f.write(str(self.current_page))

    @staticmethod
    def __clean_quotes(raw_quotes):
        return [
            re.sub(
                r'(&lt;)*',
                '',
                re.sub(
                    r'(&gt;)*|(&lt;)*',
                    '',
                    re.sub(
                        r'<br/>',
                        '\n',
                        str(q)[18:-6]
                    )
                )
            ) for q in raw_quotes
        ]

    def get_quotes(self, url):
        soup = bs4.BeautifulSoup(requests.get(url).content, 'lxml')

        quotes_raw = soup('div', class_='text')

        if url == 0:  # TODO: reset
            pass

        return self.__clean_quotes(quotes_raw)

    def quote_selection(self, mode):
        try:
            try:
                self.__pprint(self.get_quotes(self.__URLS[mode]))
            except:
                self.__pprint(self.get_quotes(self.__ALIASES[mode]))
        except:
            self.__pprint(self.get_quotes(self.__URLS['random']))

    def __pprint(self, quotes):
        pydoc.pager(''.join([quote + self.__DELIM for quote in quotes]))

    def reset_page(self):
        with open(os.path.join(os.environ['HOME'], '.bashim'), 'w') as f:
            f.write(bs4.BeautifulSoup(
                requests.get(self.__NEWEST_URL).content,
                'lxml'
            ).find(
                'input',
                class_='page'
            ).get('max'))
