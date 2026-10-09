from bs4 import BeautifulSoup
import requests

URL = "https://mashina.kg/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

response = requests.get(url=URL, headers=HEADERS)
print(response)
print(response.status_code)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
a = soup.find('div', class_='flex flex-wrap items-center gap-x-6 gap-y-2')
# print(a)
categories = []
for i in a:
    categories.append(i.text)

print(categories)
