from selenium import webdriver
from selenium.webdriver.common.keys import Keys
### ---------------
### CHALLENGE: Using the course's dummy form page, use Selenium to navigate to the login fields and enter your information.
### ----------------


chrome_driver_path = "/Users/valerie/Documents/chromedriver"

#Initialize driver.
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com")

# Locate the fields and input information..
first_name_input = driver.find_element_by_name("fName")
first_name_input.send_keys("Vivi")

last_name_input = driver.find_element_by_name("lName")
last_name_input.send_keys("Yamanaka")

email_input = driver.find_element_by_name("email")
email_input.send_keys("email@email.email")

## Locate submit button and click it.
button = driver.find_element_by_tag_name("button")
button.click()

# #### Then use send_keys to input into it.
# search.send_keys("Python") ## This inputs 'Python'.
# search.send_keys(Keys.ENTER) ## This uses the imported Keys to press the enter key.
