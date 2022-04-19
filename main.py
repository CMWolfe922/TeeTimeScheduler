from browser import Browser, HomePageLocators
from config.secrets import COURSE_URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Create a webdriver instance
browser = Browser(COURSE_URL)

# open the webpage
browse = browser.browse()

# Create a HomePageLocator object HPL to search for the button
HPL = HomePageLocators()

# Search for the HPL object
homePageElem = browse.find_element_by_css_selector(HPL.MEMBER_LOGIN)

# Click the button
homePageElem.click()

# Close Page
browse.close()
