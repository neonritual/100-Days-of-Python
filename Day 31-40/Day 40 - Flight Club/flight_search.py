import requests
from secrets import *

# TEQUILA_API = Oq3SFYfhb3n0vKpVnWWy-NB0IkeI5B8g
headers = {
   "apikey": TEQUILA_API,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city_name):
        response = requests.get(url=
                                f"https://tequila-api.kiwi.com/locations/query?term={city_name}&"
                                "locale=en-US&location_types=airport&limit=2&active_only=true", headers=headers, )
        self.info = response.json()
        self.data = self.info["locations"][0]["code"]
        return self.data