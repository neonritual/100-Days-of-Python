from selenium import webdriver
from selenium.webdriver.common.keys import Keys

### Using CHallenge 2's data, more studying...


chrome_driver_path = "/Users/valerie/Documents/chromedriver"

#Initialize driver.
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://ja.wikipedia.org/wiki/メインページ")

# welcome = driver.find_element_by_css_selector("#frame-welcome #number b a")
# welcome.click()  ## This will click the link found at 'welcome', aka the number of aticles on wiki.

#### But you can also click a link just by knowing its text. For example,
#### to click the link text "今日の一枚”, you can use:

# image_of_the_day = driver.find_element_by_link_text("今日の一枚")
# image_of_the_day.click()


#-------

## To be able to input inside of a serach bar, you first find the search bar.
search = driver.find_element_by_name("search")

#### Then use send_keys to input into it.
search.send_keys("Python") ## This inputs 'Python'.
search.send_keys(Keys.ENTER) ## This uses the imported Keys to press the enter key.
