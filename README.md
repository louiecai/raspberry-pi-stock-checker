# Raspberry Pi Stock Checker
 ```
______  ___   ___________ _____      _____ _____ ______  ___  ______ ___________ 
| ___ \/ _ \ /  ___| ___ \_   _|    /  ___/  __ \| ___ \/ _ \ | ___ \  ___| ___ \
| |_/ / /_\ \\ `--.| |_/ / | |______\ `--.| /  \/| |_/ / /_\ \| |_/ / |__ | |_/ /
|    /|  _  | `--. \  __/  | |______|`--. \ |    |    /|  _  ||  __/|  __||    / 
| |\ \| | | |/\__/ / |    _| |_     /\__/ / \__/\| |\ \| | | || |   | |___| |\ \
\_| \_\_| |_/\____/\_|    \___/     \____/ \____/\_| \_\_| |_/\_|   \____/\_| \_|  By Louie Cai
 ```

Raspi-scraper is a configurable python webscraper that checks raspberry pi stocks from verified sellers.



## Dependencies

Python libraries needed ([How to install python packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)):

```python
bs4
request
json
termcolor
pyyaml
```



## Installation

Windows (git bash)/Mac OS/Linux:

```bash
git clone https://github.com/louie-cai/raspberry-pi-stock-checker.git
cd raspberry-pi-stock-checker
```



## Usage

Windows:

```bash
python raspi-scraper.py
```

Mac OS/Linux:

```
python3 raspi-scraper.py
```

Linux (if your python interpreter is at `/usr/bin/python3`):

```bash
./raspi-scraper.py
```

### Configuration

Adjust `config.yaml` to turn on/off different Raspberry Pi models.



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



## License
[MIT](https://choosealicense.com/licenses/mit/)
