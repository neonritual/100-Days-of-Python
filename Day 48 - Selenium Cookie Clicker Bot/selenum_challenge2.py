from selenium import webdriver

### CHALLENGE: Access the main Wikipedia page, and print the number of articles shown in the welcome message.

## NOTE: I am using the Japanese Wikipedia Main Page, so the numbers will be different than the English.
# At time of writing, it is 1,275,782.


chrome_driver_path = "/Users/valerie/Documents/chromedriver"

#Initialize driver.
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://ja.wikipedia.org/wiki/メインページ")

welcome = driver.find_element_by_css_selector("#frame-welcome #number b a")
print(welcome.text)


driver.quit()
