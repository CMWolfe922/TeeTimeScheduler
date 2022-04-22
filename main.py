from config.secrets import COURSE_URL
from login import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from homepage import HomePage
from config.secrets import CHROMEDRIVER, FIREFOXDRIVER, SAFARIDRIVER, EDGEDRIVER
from config.secrets import DROPDOWN_LINK, DROPDOWN_DIV, FORETEES_DROPDOWN_BTN, FORETEES_TOP_BTN
import time


def get_driver(driver_name="Chrome"):

    if driver_name == "FireFox":
        _driver = webdriver.Chrome(FIREFOXDRIVER)
        return _driver
    elif driver_name == "Edge":
        _driver = webdriver.Chrome(EDGEDRIVER)
        return _driver
    elif driver_name == "Safari":
        _driver = webdriver.Chrome(SAFARIDRIVER)
        return _driver
    elif driver_name == "Chrome":
        _driver = webdriver.Chrome(CHROMEDRIVER)
        return _driver
    else:
        return None

# # Path to Chrome Driver
# CHROMEDRIVER_PATH = r"C:\\webdriver\\chromedriver.exe"
# FIREFOXDRIVER_PATH = r"C:\\webdriver\\geckodriver.exe"


homepage = HomePage()
locator = (By.XPATH, FORETEES_TOP_BTN)

if __name__ == '__main__':
    driver = get_driver()

    # Open the url with driver
    driver.maximize_window()
    driver.get(COURSE_URL)

    # ================================================================ #
    # RUN INITIAL PROGRAM FUNCTIONS:
    # ================================================================ #

    # run login function
    login(driver)

    # Run HomePage Method
    homepage.wait_for_element(driver, locator)
    # ================================================================ #
    time.sleep(10)
    # close Browser
    driver.close()
