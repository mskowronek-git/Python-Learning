import requests

class FlightData:

    def __init__(self):
        self.API_key = "_P2ZdvM0benKwINRYggzEHSp-FnHNAb2"

        self.header = {
            "apikey": self.API_key
        }




    def search_IATA(self, city):
        endpoint = "https://api.tequila.kiwi.com/locations/query"

        parameters = {
            "term": city,
            "locale": "en-US",
            "location_types": "city"
        }

        response = requests.get(endpoint, params=parameters, headers=self.header)
        results = response.json()
        return ((results["locations"][0])["code"])


