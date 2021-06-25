#This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_info()
notification_manager = NotificationManager()

### Populate the IATA Codes in Sheet.
# for num in range(1, len(sheet_data)):
#     if sheet_data[num]["iataCode"] == "":
#         flight_search = FlightSearch()
#         data = flight_search.get_iata_code(sheet_data[num]['city'])
#         data_manager.insert_aitaCode(num, data)


## Get Price from Sheet and then Tequila, and compare.
for num in range(1, len(sheet_data)):
    flight_data = FlightData()
    code = sheet_data[num]["iataCode"]
    tequila_price = flight_data.get_price(code)
    sheet_price = sheet_data[num]["lowestPrice"]
    print(f"{sheet_data[num]['city']}: {tequila_price}")
    if sheet_price > tequila_price:
        notification_manager.send_SMS(tequila_price, sheet_data[num]['city'],
            code, flight_data.get_date_depart(code), flight_data.get_date_return(code))

