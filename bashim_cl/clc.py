import argparse

from core import Core


def main_f():
    parser = argparse.ArgumentParser()

    parser.add_argument('mode', help='Mode', type=str)
    parser.add_argument('-r', '--reset', help='Reset page', action='store_true')

    args = parser.parse_args()

    core = Core()

    if args.reset:
        core.reset_page()

    core.quote_selection(args.mode)


if __name__ == '__main__':
    main_f()
