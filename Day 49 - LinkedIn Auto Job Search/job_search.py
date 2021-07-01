### Project Goal: To use Selenium Webdriver to open LinkedIn, log in, search for jobs (usuing a previously
# found link) and save companies automatically.
# The original challenge was to use Easy Apply to apply automatically, but I altered the goal to avoid
# hassling companies when I am not yet looking to change jobs!

from selenium import webdriver
import time

chrome_driver_path = "/Users/valerie/Documents/chromedriver"

#Initialize driver.
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&geoId=101355337&keywords=python%20developer&location=Japan") # the url of the search.

login_link = driver.find_element_by_link_text("Sign in")
login_link.click()

email_input = driver.find_element_by_id("username")
email_input.send_keys("MY USERNAME HERE")

password_input = driver.find_element_by_id("password")
password_input.send_keys("MY PASSWORD HERE")

login_button = driver.find_element_by_tag_name("button")
login_button.click()

time.sleep(5) #Waiting for possible page load time.

# Find the jobs titles listed in the search.
listing = driver.find_elements_by_css_selector(".job-card-list__title")

for job_titles in listing:
        job = driver.find_element_by_link_text(job_titles.text) # Locate and click links using the job title text.
        job.click()
        time.sleep(4) # Sleep to allow to alow loadtime.
        save_button = driver.find_element_by_class_name("jobs-save-button") # Find and click the 'Save' button of the job
        save_button.click()
        time.sleep(4)
        exit_message = driver.find_element_by_css_selector("li-icon.artdeco-button__icon") # When a popup appears to confirm the save, click to exit it, so it won't obscure job listings.
        exit_message.click()
        time.sleep(4)

