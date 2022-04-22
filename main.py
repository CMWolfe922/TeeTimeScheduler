from config.secrets import COURSE_URL
from login import login
from selenium import webdriver
from homepage import click_foretees, click_drop_down, home_page

# Path to Chrome Driver
CHROMEDRIVER_PATH = r"C:\\webdriver\\chromedriver.exe"
FIREFOXDRIVER_PATH = r"C:\\webdriver\\geckodriver.exe"


if __name__ == '__main__':
    # Create a webdriver instance
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)

    # Open the url with driver
    driver.get(COURSE_URL)

    # ================================================================ #
    # RUN INITIAL PROGRAM FUNCTIONS:
    # ================================================================ #

    # run login function
    login(driver)

    # wait for page to load
    driver.implicitly_wait(10)

    # run home_page function
    # click_foretees(driver)
    click_drop_down(driver)
    # ================================================================ #
    # close Browser
    driver.close()
