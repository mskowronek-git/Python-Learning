import requests


class DataManager:

    def __init__(self):
        self.url_sheety = "https://api.sheety.co/dfb003ce482671814343e68b5d1ef8f5/flightDeals/prices"
        self.destination_data = {}
        # self.APP_ID = os.environ.get("APP_ID")
        # self.API_KEY = os.environ.get("API_KEY")

        # self.header = {
        #        "x-app-id": self.APP_ID,
        #         "x-app-key": self.API_KEY
        #     }



    def add_row(self):
        ask_for_row = input("Do you want to add new row? yes/no ")

        if ask_for_row.lower() == "yes":
            city = input("What is the name of the city? ")
            # IATA_code = input("What is the IATA code of this city? ")
            lowest_price = input("What is the lowest price for the flight to this city? ")

            new_row = {
                "price": {
                    "city": city.title(),
                    # "iataCode": IATA_code.capitalize(),
                    "lowestPrice": lowest_price
                }
            }

            send = requests.post(url=self.url_sheety, json=new_row)
            print(send.text)


    def read_rows(self):
        response = requests.get(self.url_sheety)
        data_gs = response.json()
        self.destination_data = data_gs["prices"]

        return self.destination_data


    def delete_row(self):
        to_delete = input("Which row do you want to delete? ")
        url_delete = f"{self.url_sheety}/{to_delete}"

        send = requests.delete(url=url_delete)
        print(send.text)


    def put_iata(self, iatacode, id):
        url_put = f"{self.url_sheety}/{id}"
        print(url_put)
        params_row = {
            "price": {
                "iataCode": iatacode
            }
        }
        response = requests.put(url=url_put, json=params_row)
        print(response.text)