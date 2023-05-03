#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from pprint import pprint
from flight_search import FlightSearch
from notification_manager import NotificationManager

google_sheet = DataManager()
IATA_generator = FlightData()
searcher = FlightSearch()
notification = NotificationManager()

# google_sheet.add_row()
# google_sheet.delete_row()

data_gs = google_sheet.read_rows()
pprint(data_gs)

for city in data_gs:
    if city["iataCode"] == "":
        google_sheet.put_iata(IATA_generator.search_IATA(city["city"]), city["id"])

for city in data_gs:

    result = searcher.ask_prices(city["iataCode"], city["lowestPrice"])


    for info in result["data"]:
        if len(info) != 0:
            print(info)
            price = info["price"]
            cityFrom = info["cityFrom"]
            cityTo = info["cityTo"]
            airportCodeFrom =  info["flyFrom"]
            airportCodeTo =  info["flyTo"]
            local_departure = (info["local_departure"])[:10]
            local_departure_back = info["route"]
            local_departure_back = (local_departure_back[1]["local_departure"])[:10]

            notification.send_sms(price, cityFrom, airportCodeFrom, cityTo,
                                  airportCodeTo, local_departure, local_departure_back)








