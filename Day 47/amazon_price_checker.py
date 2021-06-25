from bs4 import BeautifulSoup
import requests

response = requests.get("URL TO TRACKED ITEM WILL GO HERE SOON")
amazon_response = response.text

soup = BeautifulSoup(amazon_response, "html.parser")
price_data = soup.find_all(
# TODO: HTML DATA GOES HERE with soup search)

