from config.secrets import COURSE_URL, PASSWORD, MEMBER_ID, LOGIN_BTN
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions as selenium_exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from decorators import base_logger

import time

# Path to Chrome Driver
CHROMEDRIVER_PATH = r"C:\\webdriver\\chromedriver.exe"
FIREFOXDRIVER_PATH = r"C:\\webdriver\\geckodriver.exe"


class HomePageLocators:
    """This class is for locators on the Home Page"""
    DROP_DOWN_MENU = ".humburger"


class LoginPageLocators:
    """This class is for locators on the Login Page"""
    MEMBER_ID_INPUT = "_58_login"
    MEMBER_PASSWORD_INPUT = "_58_password"
    # BTN_CSS_SELECTOR = ".mm_login.login-page .background-wrap #content-wrapper-login .login-col-left .button-holder .btn"
    BTN_CSS_SELECTOR = LOGIN_BTN


class LoggedInHomePageLocators:
    """This class is for locators on the members home page after logging in"""
    FORETEES_BUTTON_PARTIAL = "Foretees"
    FORETEES_BUTTON_XPATH = "//span[text()[normalize-space()='Foretees']]"
    FORETEES_XPATH_LONG = "//div[@id='textured-cssmenu']/ul[1]/li[5]/a[1]/span[1]"
    FORETEES_BUTTON_CSS_SELECTOR = "div#textured-cssmenu>ul>li:nth-of-type(5)>a>span"
    FORETEES_BUTTON_PAGE_ID = "//*[@data-pageid='53']"


@base_logger()
def login(driver):
    # find member id input box:
    driver.find_element(
        By.ID, LoginPageLocators.MEMBER_ID_INPUT).send_keys(MEMBER_ID)

    # find password input box
    driver.find_element(
        By.ID, LoginPageLocators.MEMBER_PASSWORD_INPUT).send_keys(PASSWORD)

    # find submit button to login
    # driver.find_element(By.CSS_SELECTOR, LoginPageLocators.MEMBER_LOGIN_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, LoginPageLocators.BTN_CSS_SELECTOR).click()
    time.sleep(5)



def click_foretees(driver, menu):
    pass

@base_logger()
def home_page(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.DROP_DOWN_MENU).click_and_hold()
        driver.implicitly_wait(10)
    except selenium_exceptions as se:
        print(se)


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
    home_page(driver)

    # ================================================================ #
    # close Browser
    driver.close()
