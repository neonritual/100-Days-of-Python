import requests

new_data = {
    "price": {
        "city": "Edogawa",
        "iataCode": "test",
        "lowestPrice": 100,
    }
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer please"
}

test_resp = requests.post(url="https://api.sheety.co/73cd1f0353410408aed4363f4338e98c/flightDeals/prices", json=new_data, headers=headers)
print(test_resp)