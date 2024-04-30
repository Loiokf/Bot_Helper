"""from bs4 import BeautifulSoup
from urllib.request import urlopen
from models import Parser, Rate, ABC


def tag_to_string(obj):
    for pos in range(len(obj)):
        obj[pos] = str(obj[pos])
    return obj


class GetInfoAboutRate(Parser, ABC):
    URL = "https://www.cbr.ru/currency_base/daily/"  # Central bank website
    soup = BeautifulSoup(urlopen(URL).read(), "html.parser")

    @classmethod
    def get_data(cls) -> list[Rate]:
        all_cur: list[Rate] = []
        exchange_rates = cls.soup.find_all("tr")[1:]
        for rate in exchange_rates:
            cur_obj = tag_to_string(rate.find_all("td")[1:])
            cost = cur_obj[3][4:len(cur_obj[3]) - 5]
            cost = float(str(cost).replace(",", "."))
            val = int(cur_obj[1][4:len(cur_obj[1]) - 5])
            if val != 1:
                cost /= val
            cost = round(cost, 3)

            rate = Rate(
                rate_text=cur_obj[2][4:len(cur_obj[2]) - 5],
                rate_symbol=cur_obj[0][4:len(cur_obj[0]) - 5],
                sum_rub=cost
            )
            all_cur.append(rate.text)
        return all_cur"""

import datetime
import requests
import xml.etree.ElementTree as ET
from datetime import date


class GetInfoAboutRate:

    def __init__(self):
        self.result = []

    def get_currency_rates(self):
        # Формируем URL запроса
        url = "http://www.cbr.ru/scripts/XML_daily.asp"
        params = {
            "date_req": date.today().strftime("%d/%m/%Y")
        }

        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        currency_rates = {}

        for valute in root.findall(".//Valute"):
            code = valute.find("CharCode").text
            if code in ["USD", "EUR", "CNY", "JPY"]:
                rate = valute.find("Value").text
                currency_rates[code] = float(rate.replace(",", "."))
        return currency_rates

        currency_rates = get_currency_rates()
        self.result.append(f"Курсы валют на сегодняшний день: ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
                           "USD: {:.2f} RUB".format(currency_rates["USD"])
                           "EUR: {:.2f} RUB".format(currency_rates["EUR"])
                           "CNY: {:.2f} RUB".format(currency_rates["CNY"])
                           "JPY: {:.2f} RUB".format(currency_rates["JPY"]))
        for i in self.result:
            return i
