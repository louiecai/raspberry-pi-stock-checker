import json
import termcolor

import scrapers

scrapers = {
    'PiShop.us': scrapers.scrape_pishop,
    'CanaKit': scrapers.scrape_canakit,
    'Adafruit': scrapers.scrape_adafruit,
    'Vilros': scrapers.scrape_vilros,
    'Chicago Electronic': scrapers.scrape_chicago,
    'Sparkfun': scrapers.scrape_sparkfun,
    'Okdo': scrapers.scrape_okdo,
    'Microcenter': scrapers.scrape_microcenter
}


def scrape(source_json: str, config={}) -> None:
    with open(source_json) as source_file:
        types = json.loads(source_file.read())
        for name, sources in types.items():
            if name in config.keys() and not config[name]:
                continue

            print(termcolor.colored(f'{name}', attrs=['bold']))
            for source_name, source_url in sources.items():
                if source_name not in scrapers:
                    continue

                scrapers[source_name](source_name, source_url)

            print()
