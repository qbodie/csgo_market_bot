import json
from bs4 import BeautifulSoup
import requests

url_domain = 'https://market.csgo.com'
result = []


def collect_data(url='https://market.csgo.com/?s=pop&t=365&p=1&sd=desc'):
    response = requests.get(url)

    src = response.text

    soup = BeautifulSoup(src, 'lxml')
    #    with open(f'index.html', 'w', encoding='utf-8') as file:
    #        file.write(src)
    item_urls = soup.find('div', class_="market-right-inner").find('div', class_='market-items').find_all('a',
                                                                                                          class_='item hot')
    for a_item_url in item_urls:
        item_url = url_domain + a_item_url.get('href')
        item_price = a_item_url.find('div', class_='price').text.strip()
        item_name = a_item_url.find('div', class_='name').text.strip()
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

    return result


def total_pages():
    with open('index.html', 'r', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    final_page = int(soup.find('div', class_='w33 notresize page-counter').find('span').text)
    print(f'Total pages: {final_page}')
    return final_page


def main():
    count = 1
    for i in range(total_pages()):
        collect_data(url=f'https://market.csgo.com/?s=pop&t=365&p={count}&sd=desc')
        temp = len(result)
        print(f'Page #{count}')
        count += 1
        print('#' * 10)


if __name__ == '__main__':
    main()