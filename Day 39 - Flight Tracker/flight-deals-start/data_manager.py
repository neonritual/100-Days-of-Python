from pprint import pprint
import requests
from secrets import *


headers = {
    "Content-Type": "application/json",
    "Authorization": f"{bearer}"
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_destination_info()

    def get_destination_info(self):
        response = requests.get(url=sheety_endpoint, headers=headers)
        response.raise_for_status()
        self.sheet = response.json()
        self.sheet_data = self.sheet["prices"]
        return self.sheet_data


    # def insert_aitaCode(self, num, data):
    #     new_data = {
    #         "price": {
    #             "iataCode": data,
    #         }
    #     }
    #     requests.put(url=f"{sheety_endpoint}/{num + 2}", json=new_data, headers=headers)
    #
