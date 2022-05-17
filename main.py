import json
from bs4 import BeautifulSoup
import requests


def collect_data():
    response = requests.get(url='https://market.csgo.com/?s=pop&t=365&sd=desc')

    src = response.text
#    print(src)
#    with open(f'index.html', 'w', encoding='utf-8') as file:
#        file.write(src)


def main():
    collect_data()


if __name__ == '__main__':
    main()
