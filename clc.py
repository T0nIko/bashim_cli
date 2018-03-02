import argparse

import core


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('mode', help='Mode', type=str)
    parser.add_argument('-r', '--reset', help='Reset page', action='store_true')

    args = parser.parse_args()

    clc_core = core.Core()

    if args.reset:
        clc_core.reset_page()

    clc_core.quote_selection(args.mode)


if __name__ == '__main__':
    main()
