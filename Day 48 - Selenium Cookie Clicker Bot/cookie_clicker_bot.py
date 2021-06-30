from selenium import webdriver
import time

chrome_driver_path = "/Users/valerie/Documents/chromedriver"

#Initialize driver.
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Locate cookie in center of page.
cookie = driver.find_element_by_id("cookie")
#
# # Find list of store items in the div with class store, and their IDs.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

# Set a time for a "timeout" that is 5 seconds from initial time, and five minute interval.
timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    # Every five seconds:
    if time.time() > timeout:

        # Upgrade <b> tagged available items and set up price list.
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        #Convert <b> tagged text into int prices:
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create a dict of store items and prices:
        cookie_upgrades = {}
        for number in range(len(item_prices)):
            cookie_upgrades[item_prices[number]] =  item_ids[number]

        # Get our current cookie count:
        my_money = driver.find_element_by_id("money").text
        if "," in my_money:
            my_money = my_money.replace(",", "")
        cookie_count = int(my_money)

        # Find upgrades you can afford:
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Buy the most expensive tem you can afford:

        highest_affordable_upgrade = max(affordable_upgrades)
        print(highest_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another five seconds until the next check.
        timeout = time.time() + 5

    # After 5 mins, stop the bot and check cookies per second.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break



