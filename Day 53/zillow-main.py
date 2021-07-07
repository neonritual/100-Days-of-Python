## CHALLENGE: The challenge was to scrape a Zillow search for a certain property type (in this case, a
# a 2br rental in the San Frnacisco area under 3k, that also allows cats), use Selenium to input them individually
# into a Google form, then create a spreadsheet from the data.

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

GOOGLE_FORM_LINK = "https://forms.gle/h4SUsrRFxhtck8h37"
ZILLOW_SEARCH = "https://www.zillow.com/homes/for_rent/2-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.79725111914063%2C%22east%22%3A-122.06940688085938%2C%22south%22%3A37.509961353769796%2C%22north%22%3A38.03967272127907%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22cat%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
chrome_driver_path = "/Users/valerie/Documents/chromedriver"


#Set HTTP Headers to pass along to Amazon.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

listing_addresses_list = []
listing_prices_list = []
listing_links_list_raw = []
listing_links_list_reordered = []
listing_links_list_replaced = []

# Initialize and get data from Zillow search
response = requests.get(ZILLOW_SEARCH, headers=headers)
zillow_response = response.text
soup = BeautifulSoup(zillow_response, "html.parser")

# Pass data into Beautiful Soup and find the listing divs.

listing_prices_raw = soup.find_all(class_="list-card-price")
# list-card-info == class for all listing cards
for price in listing_prices_raw:
    listing_prices_list.append(price.getText())

listing_addresses_raw = soup.find_all(class_="list-card-addr")
for address in listing_addresses_raw:
    listing_addresses_list.append(address.getText())

listing_links_raw = soup.find_all(class_="list-card-link")
for link in listing_links_raw:
    url = link.get("href")
    listing_links_list_raw.append(url)

# listing_links_list = list(set(listing_links_list_raw))
listing_links_list_reordered = list(dict.fromkeys(listing_links_list_raw))

for link in listing_links_list_reordered:
    try:
        new_link = link.replace("/b/", "https://www.zillow.com/b/")
        listing_links_list_replaced.append(new_link)
    except AttributeError:
        pass

print(listing_prices_list)
print(len(listing_prices_list))
print(listing_addresses_list)
print(len(listing_addresses_list))
print(listing_links_list_replaced)
print(len(listing_links_list_replaced))

#TODO: Use Selenium to nav to Google form and imput values from each list.


