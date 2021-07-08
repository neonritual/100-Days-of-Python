## CHALLENGE: The challenge was to scrape a Zillow search for a certain property type (in this case, a
# a 2br rental in the San Frnacisco area under 3k, that also allows cats), use Selenium to input them individually
# into a Google form, then create a spreadsheet from the data.

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

GOOGLE_FORM_LINK = "https://forms.gle/h4SUsrRFxhtck8h37"
ZILLOW_SEARCH = "https://www.zillow.com/homes/for_rent/2-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.79725111914063%2C%22east%22%3A-122.06940688085938%2C%22south%22%3A37.509961353769796%2C%22north%22%3A38.03967272127907%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22cat%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
DRIVER_PATH = "/Users/valerie/Documents/chromedriver"


#Set HTTP Headers to pass along to Zillow.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

address_list = []
price_list = []
links_list_raw = []
links_list_firstpass = []
links_list = []

# Initialize and get data from Zillow search
response = requests.get(ZILLOW_SEARCH, headers=headers)
zillow_response = response.text
soup = BeautifulSoup(zillow_response, "html.parser")

# Pass data into Beautiful Soup and find the listing divs.
listing_prices_raw = soup.find_all(class_="list-card-price")
# list-card-info == class for all listing cards
for price in listing_prices_raw:
    price_list.append(price.getText())

listing_addresses_raw = soup.find_all(class_="list-card-addr")
for address in listing_addresses_raw:
    address_list.append(address.getText())

listing_links_raw = soup.find_all(class_="list-card-link")
for link in listing_links_raw:
    url = link.get("href")
    links_list_raw.append(url)

# Removing duplicate entries while retaining list order.
links_list_firstpass = list(dict.fromkeys(links_list_raw))

# Fixing incomplete URLs.
for link in links_list_firstpass:
    try:
        new_link = link.replace("/b/", "https://www.zillow.com/b/")
        links_list.append(new_link)
    except AttributeError:
        pass

time.sleep(5)

#Initialize driver.
driver = webdriver.Chrome(DRIVER_PATH)
driver.get(GOOGLE_FORM_LINK)

# Create for loop that will input data into Google form fields, iterating through the individual lists until
# complete.
for n in range(len(price_list)):

    address_xpath = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_xpath = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_xpath = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    price_xpath.send_keys(price_list[n])
    address_xpath.send_keys(address_list[n])
    link_xpath.send_keys(links_list[n])
    submit_button.click()
    time.sleep(4)
    go_back_link = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    go_back_link.click()
    time.sleep(4)
