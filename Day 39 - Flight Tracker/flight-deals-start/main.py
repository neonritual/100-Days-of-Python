#This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests

from flight_search import FlightSearch



from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_info()
print(sheet_data)

new_data = {
        "prices": {
            "city": "Edogawa",
            "IATA Code": "test",
            "lowest price": 100,
        }
    }

requests.post(url="s",
             json=new_data)


# for num in range(len(sheet_data)):
#     if sheet_data[num]["iataCode"] == "" or sheet_data[num]["iataCode"] == "TESTING":
#         flight_search = FlightSearch()
#         data_manager.insert_aitaCode(flight_search.get_iata_code(sheet_data[num]['city']))
#
