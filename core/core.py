import re
import pydoc

import bs4
import requests


class Core:
    __RND_URL = 'http://bash.im/random'
    __BEST_URL = 'http://bash.im/best'
    __NEWEST_URL = 'http://bash.im/index/'
    __ABYSS_URL = 'http://bash.im/abyss'
    __ABYSS_TOP_URL = 'http://bash.im/abysstop'
    __ABYSS_BEST_URL = 'http://bash.im/abyssbest'

    __URLS = {
        'random': __RND_URL,
        'best': __BEST_URL,
        'new': __NEWEST_URL,
        'abyss': __ABYSS_URL,
        'abyss_top': __ABYSS_TOP_URL,
        'abyss_best': __ABYSS_BEST_URL,
    }

    __ALIASES = {
        '': __URLS['random'],
        'rnd': __URLS['random'],
        'r': __URLS['random'],
        'b': __URLS['best'],
        'n': __URLS['new'],
        'a': __URLS['abyss'],
        'at': __URLS['abyss_top'],
        'ab': __URLS['abyss_best'],
    }

    __DELIM = '\n--------------------------------------------------------\n'

    def __init__(self):
        self.current_page = int(bs4.BeautifulSoup(
            requests.get(self.__NEWEST_URL + '1345').content,
            'lxml'
        ).find(
            'input',
            class_='page'
        ).get('max'))

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
        # return [re.sub(r'<br/>', '\n', str(q)[18:-6]) for q in raw_quotes]

    def get_quotes(self, url):
        soup = bs4.BeautifulSoup(requests.get(url).content, 'lxml')

        quotes_raw = soup('div', class_='text')

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
        pass
#
#
# if __name__ == '__main__':
#     core = Core()
#     print(core.current_page)
