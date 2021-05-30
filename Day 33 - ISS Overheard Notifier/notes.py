import requests as requests

#Using a website's API:

response = requests.get(url="http://api.open-notify.org/iss-now.json")
#this captures the "response" from the ISS website's API.

# print(response.status_code) #prints a Response Code.

#Response Codes:
#1XX: Hold On
#2XX: Here you go
#3XX: Go Away
#4XX: You Screwed Up
#5XX: I Screwed Up

response.raise_for_status() #as part of the Requests module, this raises an exception for status errors.


data = response.json() #accesses the actual data from the json
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)
