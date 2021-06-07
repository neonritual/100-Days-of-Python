from pprint import pprint
import requests
import os
# FLIGHT_SHEET_API = os.environ.get('FLIGHT_SHEET_API')

sheety_endpoint = ""
# sheety_endpoint = f"https://api.sheety.co/{os.environ.get('FLIGHT_SHEET_API')}/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_destination_info()


    def get_destination_info(self):
        response = requests.get(sheety_endpoint)
        sheet = response.json()
        self.sheet_data = sheet["prices"]
        return self.sheet_data

    def insert_aitaCode(self, data):
        new_data = {
            "prices": {
                "iataCode": data
            }
        }
        requests.put(url=f"{sheety_endpoint}/2", json=new_data)

    def testing_sheety(self):
        new_data = {
            "prices": {
                "city": "test"
            }
        }
                     json=new_data)