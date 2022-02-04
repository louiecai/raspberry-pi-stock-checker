from bs4 import BeautifulSoup

from utils import better_request, pretty_print


def scrape_pishop(name: str, url: str) -> None:
    soup = BeautifulSoup(better_request(url, name).text, "lxml")
    in_stock = soup.find('div', class_='form-action').find('input')['value'] != "Out of stock"
    price = soup.find('span', class_='price price--withoutTax').text
    pretty_print(name, price, in_stock, start='\t')


def scrape_canakit(name: str, url: str) -> None:
    soup = BeautifulSoup(better_request(url, name).text, "lxml")
    tags = soup.find_all('tr', height=50)

    for tag in tags:
        type_name = tag.find('td').find('b').text[9:]
        price = tag.find('span', class_='priceListPrice').text
        status = tag.find('div').find('a').text
        in_stock = status != 'Sold Out'
        date = status[11:] if status != 'Sold Out' else None

        pretty_print(f'{name} - {type_name}', price, in_stock, start='\t', date=date)
