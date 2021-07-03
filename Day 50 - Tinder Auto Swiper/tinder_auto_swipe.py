### Project Goal: To use Selenium Webdriver to open Tinder and auto-swipe.
## Because I don't want to rudely swipe yes on a bunch of random people, I will be making mine
## auto-swipe left on everyone instead.

## UNFINISHED as my dummy Facebook account was suspended for "suspicious activity" relating to testing this code.

from selenium import webdriver
import time

chrome_driver_path = "/Users/valerie/Documents/chromedriver"

#Initialize driver.
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/app/recs")




# login_link = driver.find_element_by_class_name("Pos(r) Z(1)")




# accept_cookies = driver.find_element_by_link_text("I Accept")
# accept_cookies.click()
#if8marbleeggplant

time.sleep(2)
login_link = driver.find_element_by_xpath("//*[@id='u2005023502']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login_link.click()
time.sleep(2)
login_with_facebook = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
login_with_facebook.click()
time.sleep(2)

base_window = driver.window_handles[0]
tinder_login_window = driver.window_handles[1]
driver.switch_to.window(tinder_login_window)

input_username = driver.find_element_by_xpath('//*[@id="email"]')
input_username.send_keys("MY EMAIL")

email_input = driver.find_element_by_xpath('//*[@id="pass"]')
email_input.send_keys("MY PASSWORD")

login_button = driver.find_element_by_name("login")
login_button.click()

driver.switch_to.window(base_window)
time.sleep(6)


allow_cookies = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[2]/div/div/div[1]/button')
allow_cookies.click()
allow_location = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
no_alerts= driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[2]')
no_alerts.click()

time.sleep(20)

# swipe_no = driver.find_element_by_css_selector(
#     '.M(0) Pos(f) Ov(h) P(0) Expand Fz($s) C($c-base) Ovsby(n)')

swipe_no = driver.find_elements_by_tag_name("button")[9]
swipe_no.click()


# [9]

swipe_no.click()