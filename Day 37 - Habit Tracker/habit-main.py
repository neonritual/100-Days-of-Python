import requests
from datetime import datetime

today = datetime.now()

USERNAME = "viviy"
TOKEN = "fhrehwurgb4w"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
#HTTP Post Request:
# Creating an account:
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Create a graph:

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Study Graph",
#     "unit": "hours",
#     "type": "float",
#     "color": "ajisai"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
#Adding a Pixel to our graph:
headers = {
    "X-USER-TOKEN": TOKEN ##same as above but copied here for visibility
    }
graph1_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
graph1_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?  "),
}
requests.post(url=graph1_endpoint, json=graph1_config, headers=headers)

#
# #Deleting a pixel
# headers = {
#     "X-USER-TOKEN": TOKEN ##same as above but copied here for visibility
#     }
#
# graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20210603"
#
# requests.delete(url=graph_delete_endpoint, headers=headers)
