## CHALLENGE: The challenge this time was to create an Instagram Follow bot that would open up an
# account that you have a similar audience to, and follow all of the people who follow it.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/valerie/Documents/chromedriver"
SIMILAR_ACCOUNT = "healthy_life_log"
USERNAME = "my username goes here"
PASSWORD = "my pssword goes here"


class InstaFollower():
    def __init__(self):
        # Initialize driver.
        self.driver = webdriver.Chrome(chrome_driver_path)

    def login(self):
        # Log into Instagram; ignore prompt to save details at this time.
        self.driver.get("http://instagram.com")
        time.sleep(2)
        input_username = self.driver.find_element_by_name("username")
        input_username.send_keys(USERNAME)

        input_password = self.driver.find_element_by_name("password")
        input_password.send_keys(PASSWORD)

        login_button = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div'
        )
        login_button.click()

        time.sleep(2)
        dont_save_info_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button'
        )
        dont_save_info_button.click()

    def find_followers(self):
        # Open the follower list of the similar account.
        self.driver.get(f"http://instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        open_follower_page = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'
        )
        open_follower_page.click()
        time.sleep(3)
        modal = self.driver.find_element_by_xpath('//div[@Class="isgrP"]')
        self.driver.execute_script("arguments[0].scrolltop = arguments[0].scrollHeight", modal)
        time.sleep(3)

    def follow(self):
        # Follow the accounts in the similar account's follower list, except in the case you are already following that account.
        all_followers = self.driver.find_elements_by_css_selector("li button")
        for follower in all_followers:
            try:
                follower.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()