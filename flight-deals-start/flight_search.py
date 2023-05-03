import requests
import datetime
from dateutil.relativedelta import relativedelta


API_KEY = "_P2ZdvM0benKwINRYggzEHSp-FnHNAb2"
URL = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:

    def ask_prices(self, city_iata, max_price):
        date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        six_months = datetime.date.today() + relativedelta(months=+6)

        header = {
            "apikey": API_KEY
        }

        parameters = {
            "fly_from": "PL",
            "fly_to": city_iata,
            "date_from": date_tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "price_to": max_price,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }

        response = requests.get(url=URL, params=parameters, headers=header)
        return response.json()