import requests
import datetime
import os


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{os.environ.get('SHEETY_API')}/myWorkouts/workouts"




headers = {
    "x-app-id": os.environ.get("NUTRIONIX_API_KEY"),
    "x-app-key": os.environ.get("NUTRIONIX_USER_ID"),
    "x-remote-user-id": os.environ.get("NUTRIONIX_APP_ID")
}
exercise_config = {
    "query": str(input("What did you do today?     ")),
    "gender": "female",
    "weight_kg": 52,
    "height_cm": 156,
    "age": 34
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
data = response.json()

today = datetime.datetime.now()

the_date = today.strftime("%d/%m/%Y")
the_time = today.strftime("%H:%M:%S")


sheety_config = {
    "workout": {
        "date": str(the_date),
        "time": str(the_time),
        "exercise": data["exercises"][0]['name'].title(),
        "duration": data["exercises"][0]['duration_min'],
        "calories": data["exercises"][0]['nf_calories'],
    }
}
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bear {os.environ.get('SHEETY_BEARER')}",
}

sheety_response = requests.post(url=sheety_endpoint, headers=headers, json=sheety_config)
print(sheety_response.text)


