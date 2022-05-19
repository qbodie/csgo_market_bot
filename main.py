import json
from bs4 import BeautifulSoup
import requests

url = 'https://market.csgo.com'
result = []

def collect_data():
    response = requests.get(url='https://market.csgo.com/?s=pop&t=365&sd=desc')

    src = response.text

    soup = BeautifulSoup(src, 'lxml')
#    with open(f'index.html', 'w', encoding='utf-8') as file:
#        file.write(src)
    item_urls = soup.find('div', class_="market-right-inner").find('div', class_='market-items').find_all('a', class_='item hot')
    for a_item_url in item_urls:
        item_url = url + a_item_url.get('href')
        item_price = a_item_url.find('div', class_='price').text.strip()
        item_name = a_item_url.find('div', class_='name').text.strip()
        # print(item_name)
        # print(item_url)
        # print(item_price)
        result.append(
            {
                "item_name": item_name,
                "item_price": item_price,
                "item_url": item_url
            }
        )
    # print(len(result))
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)




def main():
    collect_data()


if __name__ == '__main__':
    main()
