from selenium import webdriver

chrome_driver_path = "/Users/valerie/Documents/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(url) # Brings browser to a url.

driver.quit()  # This closes the whole browser down after.
driver.close() # This closes only the tab you were opening.

# To find and return the price of an amazon item:
#
driver.get("AMAZON LINK TO ITEM") # Go to the webpage of the item.
price = driver.find_element_by_id("priceblock_outprice") # This searches for an element with a particular ID, just like in Beautiful Soup.
print(price) # Prints it, then..
driver.quit()  # quits browser.
#
# To find the search bar on Python.org...

driver.get("https://python.org")
search_bar =  driver.find_element_by_name("q") # this finds the element named q to find the search bar.
# You can then choose how to display the info.
# Default returns it as a selenium object.
print(search_bar.tag_name) # This returns the type, which as a search bar, is an 'input'
print(search_bar.get_attribute("placeholder") # This returns its attribute under placeholder.
# This is useful for submitting forms automatically.

# You can even find images and their properties.
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)
# This returns the size of the logo {'height': 82, 'width': 290}

# You can also search by elements within certain selectors
documentation_link = driver.find_element_by_css_selector(".documentation-widget a") #finds an anchor tag "a" within "documentation-widget" class

# You can also drill down from the top of the page using XPath.
# You can find XPaths using Inspector on elements of websites (with right click).
bug_link = driver.find_element_by_xpath("INSERT XPATH")



