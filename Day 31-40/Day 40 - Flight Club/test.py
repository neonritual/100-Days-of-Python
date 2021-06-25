import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
from secrets import *

tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
now = dt.datetime.now()
TODAYS_DATE = now.strftime("%d/%m/%Y")
SIX_MO_FROM_NOW = (now + relativedelta(months=+6)).strftime("%d/%m/%Y")
#
headers = {
    "Content-Type": "application/json",
    "Authorization": f"{bearer}"
}

response = requests.get(url=sheety_user_endpoint, headers=headers)
response.raise_for_status()
sheet = response.json()
sheet_data = sheet["users"]
print(sheet_data)


# headers = {
#     "apikey": TEQUILA_API,
# }
#
# response = requests.get(url=f"{tequila_endpoint}?fly_from=LON&fly_to=DPS&dateFrom={TODAYS_DATE}&"
#                                     f"dateTo={SIX_MO_FROM_NOW}&limit=1", headers=headers)
# data = response.json()
# if data["data"] == "":
#     print("nothin")
# else:
#     print("hey")