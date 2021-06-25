import requests as requests
import datetime

MY_LAT = 35.689487
MY_LONG = 139.691711


#
# #Using a website's API:
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #this captures the "response" from the ISS website's API.
#
# # print(response.status_code) #prints a Response Code.
#
# #Response Codes:
# #1XX: Hold On
# #2XX: Here you go
# #3XX: Go Away
# #4XX: You Screwed Up
# #5XX: I Screwed Up
#
# response.raise_for_status() #as part of the Requests module, this raises an exception for status errors.
#
#
# data = response.json() #accesses the actual data from the json
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("http://api.sunsire-sunset.org/json", params=parameters)
#getting sunrise sunset time data

response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()





