import requests
from bs4 import BeautifulSoup
import re
import csv

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

def clean_text(value):
    if not value:
        return None
    return " ".join(value.split())

def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    response.raise_for_status()
    return response.text

def parse_year(char):
    match = re.search(r"\b(19|20)\d{2}\b", char)
    if match:
        return match.group()
    return None

def parse_millage(char):
    if "km" in char.lower():
        return clean_text(char)
    return None

def parse_engine_size(char):
    match = re.search(r"\d+(?:[.,]\d+)?\s*", char.lower())

    if match:
        return match.group()
    return None

def parse_transmission(char):
    char = char.lower()
    transmissions = [
        "автомат",
        "механика",
        "вариатор",
        "робот",
    ]
    for transmission in transmissions:
        if transmission in char:
            return transmission
    return None

def parse_hand_drive(char):
    char = char.lower()
    if "слева" in char:
        return char
    if "справа" in char:
        return char
    return None

def parse_car_type(char):
    char = char.lower()
    car_types = [
        "купе",
        "внедорожник",
        "седан",
        "хэтчбек",
        "минивэн",
        "пикап"
    ]
    for car_type in car_types:
        if car_type in char:
            return car_type
    return None

def parse_listings(html):
    soup = BeautifulSoup(html, "html.parser")
    # cards = soup.select('a[href^="/details/"]')

    cards = soup.find('div', class_="grid_root w-full grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-4")
    

    cars = []

    for card in cards:
        #title
        title = card.find('h3')
        chars = card.find('p')
        if not title:
            continue
        title = title.text

        year = None
        millage = None
        engine_size = None
        transmission = None
        hand_drive = None
        car_type = None

        chars = card.find('p')
        chars = [
            clean_text(x) 
            for x in chars
            .get_text(" ", strip=True)
            .split(' ‧ ')
            if clean_text(x)
        ]

        for char in chars:
            if year is None:
                value = parse_year(char)
                if value:
                    year = value
                    continue

            if millage is None:
                value = parse_millage(char)
                if value:
                    millage = value

            if engine_size is None:
                value = parse_engine_size(char)
                if value:
                    engine_size = value

            if transmission is None:
                value = parse_transmission(char)
                if value:
                    transmission = value

            if hand_drive is None:
                value = parse_hand_drive(char)
                if value:
                    hand_drive = value

            if car_type is None:
                value = parse_car_type(char)
                if value:
                    car_type = value

        # list_with_data
        # try:
        #     chars = card.find('p').text.split(' ‧ ')
        #     year = chars[0]
        #     millage = chars[1]
        #     engine_size = chars[2]
        #     transmission = chars[3]
        #     hand_drive = chars[4]
        #     car_type = chars[5]
        # except IndexError:
        #     print(title)
        #     car_type = None
        # year, millage, engine_size, transmission, hand_drive, car_type = chars

        # price
        div_price = card.find('div', class_="flex flex-1 items-center gap-1.5 min-w-0")
        price_com = div_price.find('span', class_="text-sm font-medium leading-5 whitespace-nowrap text-text-primary").text

        price_dollar = div_price.find('span', class_="text-sm font-medium leading-5 text-text-primary whitespace-nowrap").text

        dict_car = {
            "title": title,
            "year" : year,
            "millage" : millage,
            "engine_size" : engine_size,
            "transmission" : transmission,
            "hand_drive" : hand_drive,
            "car_type" : car_type,
            "price_com": price_com,
            "price_dollar": price_dollar
        }

        cars.append(dict_car)

    return cars

# html = get_html(URL)
# cars = parse_listings(html)
# print(cars)

def get_last_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', class_='w-full overflow-x-auto mt-6').find('ul', class_='inline-flex items-center gap-1')
    pages = []
    for last_page in pagination:
        pages.append(last_page)
    last_page = int(pages[-3].find('a').text)

    return last_page


def save_to_csv(cars, filename):
    if not cars:
        print("no data")
        return 

    field_names = cars[0].keys()

    with open(filename, "a", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader() # writing columns
        writer.writerows(cars) # write data

    print(f"saved {len(cars)}", f"{filename}")


def parse_all_mashina_kg(
        start_page=1,
        max_pages=None
):

    for i in range(start_page, max_pages+1):
        url = f"{URL}?np={i}"
        html = get_html(url)
        try:
            cars = parse_listings(html)
        except:
            cars = []

        save_to_csv(cars, 'cars.csv')


html = get_html(URL)

parse_all_mashina_kg(start_page=1, max_pages=get_last_page(get_html(URL)))
# save_to_csv(cars, 'cars.csv')