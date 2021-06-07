import requests

new_data = {
        "prices": {
            "city": "Edogawa",
            "iata code": "test",
            "lowest price": "100",
        }
    }

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ffffff"
}

test_resp = requests.post(url="https://api.sheety.co/73cd1f0353410408aed4363f4338e98c/flightDeals/prices",
             json=new_data, headers=headers)

print(test_resp)