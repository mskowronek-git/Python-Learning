import requests
from twilio.rest import Client

account_sid = "AC1bded87764a93bdb796ff2bbc7e9b710"
auth_token = "3cc66b5a4979b281718f593aab146f9d"

class NotificationManager:


    def send_sms(self, price, cityFrom, airportCodeFrom, cityTo, airportCodeTo,
                 local_departure, local_departure_back):

            client = Client(account_sid, auth_token)

            sms_message = f"Low price alert! Only {price}EUR to fly from {cityFrom}-{airportCodeFrom}" \
                          f" to {cityTo}-{airportCodeTo}, from {local_departure} to {local_departure_back}."

            message = client.messages.create(
                body=sms_message,
                from_="+14406893449",
                to="+48605323082"
            )
            print(message.sid)