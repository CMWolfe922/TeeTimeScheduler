from config.secrets import COURSE_URL
from login import login
from selenium import webdriver
from homepage import HomePage
from config.secrets import CHROMEDRIVER, FIREFOXDRIVER, SAFARIDRIVER, EDGEDRIVER
from config.secrets import DROPDOWN_LINK, DROPDOWN_DIV, FORETEES_DROPDOWN_BTN, FORETEES_TOP_BTN
import time


class Drivers(webdriver):

    def __init__(self, url, driver_name="Chrome"):
        self.url = url
        if driver_name == "FireFox":
            self.driver = webdriver.Chrome(FIREFOXDRIVER)
        elif driver_name == "Edge":
            self.driver = webdriver.Chrome(EDGEDRIVER)
        elif driver_name == "Safari":
            self.driver = webdriver.Chrome(SAFARIDRIVER)
        elif driver_name == "Chrome":
            self.driver = webdriver.Chrome(CHROMEDRIVER)

    def __repr__(self):
        return f"Browser Object Created: Using {self.driver} to open {self.url}"

# # Path to Chrome Driver
# CHROMEDRIVER_PATH = r"C:\\webdriver\\chromedriver.exe"
# FIREFOXDRIVER_PATH = r"C:\\webdriver\\geckodriver.exe"


driver = Drivers(COURSE_URL)


homepage = HomePage

if __name__ == '__main__':
    driver = Drivers(COURSE_URL)

    # Open the url with driver
    driver.get(COURSE_URL)

    # ================================================================ #
    # RUN INITIAL PROGRAM FUNCTIONS:
    # ================================================================ #

    # run login function
    login(driver)

    # Run HomePage Method
    homepage.wait_for_element(FORETEES_TOP_BTN)
    # ================================================================ #
    time.sleep(10)
    # close Browser
    driver.close()
