import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
from secrets import *

tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
now = dt.datetime.now()
TODAYS_DATE = now.strftime("%d/%m/%Y")
SIX_MO_FROM_NOW = (now + relativedelta(months=+6)).strftime("%d/%m/%Y")


headers = {
    "apikey": TEQUILA_API,
}

class FlightData:
    #This class is responsible for structuring the flight data.
    # def __init__(self):
    #     self.get_price()

    def get_price(self, code):
        response = requests.get(url=f"{tequila_endpoint}?fly_from=LON&fly_to={code}&dateFrom={TODAYS_DATE}&"
                                  f"dateTo={SIX_MO_FROM_NOW}&limit=1", headers=headers)
        response.raise_for_status()
        data = response.json()
        if data["data"] == "":
            return "unavailable"
        else:
            return data["data"][0]["price"]

    def get_date_depart(self, code):
        response = requests.get(url=f"{tequila_endpoint}?fly_from=LON&fly_to={code}&dateFrom={TODAYS_DATE}&"
                                  f"dateTo={SIX_MO_FROM_NOW}&limit=1", headers=headers)
        response.raise_for_status()
        data = response.json()
        local = data["data"][0]["route"][0]["local_arrival"]
        return local[:9]

    def get_date_return(self, code):
        response = requests.get(url=f"{tequila_endpoint}?fly_from=LON&fly_to={code}&dateFrom={TODAYS_DATE}&"
                                    f"dateTo={SIX_MO_FROM_NOW}&limit=1", headers=headers)
        response.raise_for_status()
        data = response.json()
        local = data["data"][0]["route"][0]["local_departure"]
        return local[:9]






