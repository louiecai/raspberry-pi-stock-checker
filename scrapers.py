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


def scrape_adafruit(name: str, url: str) -> None:
    soup = BeautifulSoup(better_request(url, name).text, "lxml")
    in_stock = soup.find('div', itemprop='availability', class_='oos-header') is None
    price = soup.find('span', itemprop='price').text[2:-1]
    pretty_print(name, price, in_stock, start='\t')


def scrape_vilros(name: str, url: str) -> None:
    soup = BeautifulSoup(better_request(url, name).text, "lxml")
    in_stock = soup.find('div', class_='payment-buttons').text[66:74] != 'Sold Out'
    price = soup.find('span', class_='theme-money large-title').text
    pretty_print(name, price, in_stock, start='\t')


def scrape_chicago(name: str, url: str) -> None:
    soup = BeautifulSoup(better_request(url, name).text, "lxml")
    in_stock = soup.find('span', class_='sold_out').text == ''
    price = soup.find('span', class_='money').text
    pretty_print(name, price, in_stock, start='\t')


def scrape_sparkfun(name: str, url: str) -> None:
    soup = BeautifulSoup(better_request(url, name).text, "lxml")
    in_stock = soup.find('div', class_='quantity-row').find('strong').text != 'Out of stock.'
    price = '$' + soup.find('span', itemprop='price').text
    pretty_print(name, price, in_stock, start='\t')


def scrape_okdo(name: str, url: str) -> None:
    soup = BeautifulSoup(better_request(url, name).text, "lxml")
    in_stock = soup.find('span', class_='c-stock-level c-stock-level--low') is None
    price = soup.find('span', class_='woocommerce-Price-amount amount').text
    pretty_print(name, price, in_stock, start='\t')


def scrape_microcenter(name: str, url: str) -> None:
    soup = BeautifulSoup(better_request(url, name).text, "lxml")
    if soup.find('div', id='pnlInventory') is None:
        in_stock = True
        other = None
    else:
        in_stock = False
        other = soup.find('div', id='pnlInventory').text[2:-2]
    price = soup.find('span', id='pricing').text if soup.find('span', id='pricing') is not None else 'N/A'
    pretty_print(name, price, in_stock, start='\t', other=other)
