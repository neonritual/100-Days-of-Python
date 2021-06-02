import requests
from twilio.rest import Client


account_sid = *INSERT HERE
auth_token = **INSERT TOKEN
API_KEY = *INSERT HERE
MY_LAT = **INSERT LAT HERE
MY_LONG = **INSERT LONG HERE
PART = "current,minutely,daily,alerts"
TRILIO_NUMBER = ""
MY_NUMBER = ""



response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&"
                        f"exclude={PART}&appid={API_KEY}&unites=metric")

response.raise_for_status()
data = response.json()

print(data["hourly"][0]["weather"][0]["id"])

hours_list = []
will_rain = False

for hour in range(0, 12):
    hours_list.append(data["hourly"][hour]["weather"][0]["id"])

for x in hours_list:
    if x < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Looks like rain. Better bring an umbrella!",
        from_= TRILIO_NUMBER,
        to=MY_NUMBER
    )
    print(message.status)

