### CHALLENGE: Make a Twitter bot to tweet at a company when your computer's speed test result is below
# their guarenteed speeds.
# Since I did not want to actually tweet at a company even as a test, so this just tweets without @.

from selenium import webdriver
import time

# These are the guaranteed upload and download speeds of my fictional internet company.
PROMISED_DOWN = 100.00
PROMISED_UP = 10.00
TWITTER_USERNAME = ""
TWITTER_PASSWORD = ""
chrome_driver_path = "/Users/valerie/Documents/chromedriver"




class InternetSpeedBot():
    def __init__(self):
        # Initialize driver.
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.up_speed = 0
        self.down_speed = 0


    def tweet(self):
        #Log in to twitter.
        self.driver.get("https://www.twitter.com")
        time.sleep(4)
        login_button = self.driver.find_element_by_link_text("Log in")
        login_button.click()

        time.sleep(2)

        input_username = self.driver.find_element_by_name("session[username_or_email]")
        input_username.send_keys(TWITTER_USERNAME)

        input_password = self.driver.find_element_by_name("session[password]")
        input_password.send_keys(TWITTER_PASSWORD)

        login_to_twitter = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        login_to_twitter.click()

        time.sleep(2)

        # Locate the tweet input field, and tweet using recently grabbed variables.
        tweet_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div'
                                                        )
        tweet_field.send_keys(
        f"Hey random ISP, why is my speed {self.down_speed} down and {self.up_speed} up when I pay for 100down/10up?")

        send_tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'
        )
        send_tweet_button.click()

    def get_internet_speed(self):
        # Run an internet speed test and grab the up/down speeds.
        self.driver.get("https://www.speedtest.net")
        time.sleep(5)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()

        time.sleep(50)
        self.down_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text
        self.up_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        ).text

        # Compare the grabbed speeds to the speeds promised by my ISP; if lower than advertised,
        # tweet.
        if float(self.up_speed) < PROMISED_UP or float(self.down_speed) < PROMISED_DOWN:
            self.tweet()



isb = InternetSpeedBot()
isb.get_internet_speed()


