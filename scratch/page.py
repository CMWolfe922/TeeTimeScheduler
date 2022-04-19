from TeeTimeScheduler.browser import HomePageLocators, LoggedInHomePageLocators, LoginPageLocators
from config.secrets import COURSE_URL, MEMBER_ID, PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


CHROMEDRIVER_PATH = r"C:\\Users\\charl\\webdriver\\chromedriver_win32\\chromedriver.exe"

# Create a webdriver instance
driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# open the webpage
driver.get(COURSE_URL)

# Create a HomePageLocator object HPL to search for the button
HPL = HomePageLocators.find_element_by_css_selector(
    HomePageLocators.MEMBER_LOGIN)

# Click the button
HPL.click()

# Close Page
driver.close()
