from selenium import webdriver


### CHALLENGE: Make a dictionary of events shown on the Python.org website, with the key being the numbers from 0.
### Ex. {0: 2020-02-20, Event Name} etc.

chrome_driver_path = "/Users/valerie/Documents/chromedriver"

#Initialize driver.
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://python.org")

# Scrape data for Dates of Events.
dates = driver.find_elements_by_css_selector(".event-widget time")

# Scrape data for Names of events.
event_names = driver.find_elements_by_css_selector(".event-widget li a")

# Combine both in numbered entries in dictionary.
event_list = {num:(dates[num].text, event_names[num].text) for num in range(0, len(event_names))}
print(event_list)

# Quite the browser window.
driver.quit()

