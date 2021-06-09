#This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager
## A remake of the original flight price notifier as a "flight club" that emails users when
## prices are low.

data_manager = DataManager()
sheet_data = data_manager.get_destination_info()
user_data = data_manager.get_user_info()
notification_manager = NotificationManager()

def new_user_prompt():
    user_first_name = input("What is your first name? \n")
    user_last_name = input("What is your last name?\n")
    user_email = input("What is your email?\n")
    user_email_confirm = input("Please type your email again to confirm.\n")
    if user_email == user_email_confirm:
        print("You're in the club!")
        data_manager.add_new_user(user_first_name,user_last_name, user_email)
    else:
        print("Sorry, please try again.")
        new_user_prompt()

# new_user_prompt()



### Populate the IATA Codes in Sheet. Only run if there are blank/new IATA Codes.
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
    if sheet_price > tequila_price:
        print(f"{sheet_data[num]['city']}: {tequila_price}")
        for user_num in range(0, len(user_data)):
            receiver_email = user_data[user_num]["email"]
            notification_manager.send_emails(receiver_email, tequila_price, sheet_data[num]['city'], code, flight_data.get_date_depart(code), flight_data.get_date_return(code))
        print("no email??")
        # notification_manager.send_SMS(tequila_price, sheet_data[num]['city'],
        #     code, flight_data.get_date_depart(code), flight_data.get_date_return(code))

