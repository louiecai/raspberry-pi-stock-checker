import scrapers
import json
import termcolor

from utils import pretty_print

scrapers = {
    'PiShop.us': scrapers.scrape_pishop,
    'CanaKit': scrapers.scrape_canakit
}


def scrape(source_json: str) -> None:
    with open(source_json) as source_file:
        types = json.loads(source_file.read())
        for name, sources in types.items():
            print(termcolor.colored(f'{name}', attrs=['bold']))
            for source_name, source_url in sources.items():
                if source_name not in scrapers:
                    continue

                scrapers[source_name](source_name, source_url)
