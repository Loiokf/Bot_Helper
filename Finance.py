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

