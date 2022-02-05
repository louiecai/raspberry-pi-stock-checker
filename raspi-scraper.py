#!/usr/bin/python3

from utils import print_logo, parse_config
from main_scraper import scrape


def main():
    config = parse_config('./config.yaml')
    print_logo()
    scrape('./sources.json', config)
    print()


if __name__ == '__main__':
    main()
