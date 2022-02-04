#!/usr/bin/python3

from utils import print_logo
from main_scraper import scrape


def main():
    print_logo()
    scrape('./sources.json')
    print()


if __name__ == '__main__':
    main()
