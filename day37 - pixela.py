import requests
import os
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = os.environ.get("PIXELA_TOKEN")
pixela_username = "bottomtext"
user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "Pages Read",
    "unit": "page",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": pixela_token
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

date = datetime.datetime.now().strftime("%Y%m%d")
yday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(("%Y%m%d"))
books_endpoint = f"{graph_endpoint}/{graph_id}/{yday}"
books_params = {
    "quantity": "100"
}
response = requests.delete(url=books_endpoint, headers=headers)
print(response.text)