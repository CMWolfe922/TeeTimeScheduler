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


class HomePageDropDown:
    """This class is for locators on the Home Page"""
    DROP_DOWN_MENU = ".ui-link"
    DD_BTN_ATTEMPT_1 = "//a[contains(@href, '#menu']"
    DD_FORETEES_BTN_XPATH = "//span[@class='smartphone-nav-heading'][normalize-space()='Foretees']"
    DD_BUTTON = "//div[@id='mm-menu-link']"

class LoginPageLocators:
    """This class is for locators on the Login Page"""
    MEMBER_ID_INPUT = "_58_login"
    MEMBER_PASSWORD_INPUT = "_58_password"
    # BTN_CSS_SELECTOR = ".mm_login.login-page .background-wrap #content-wrapper-login .login-col-left .button-holder .btn"
    BTN_CSS_SELECTOR = LOGIN_BTN



class HomePageLocators:
    """This class is for locators on the members home page after logging in"""
    FORETEES_BUTTON_PARTIAL = "Foretees"
    FORETEES_BUTTON_XPATH = "//span[text()[normalize-space()='Foretees']]"
    FORETEES_XPATH_LONG = "//div[@id='textured-cssmenu']/ul[1]/li[5]/a[1]/span[1]"
    FORETEES_BUTTON_CSS_SELECTOR = "div#textured-cssmenu>ul>li:nth-of-type(5)>a>span"
    FORETEES_BUTTON_PAGE_ID = "//*[@data-pageid='53']"
    # Error Message: selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
    FORETEES_BUTTON_XPATH_1 = "//span[@class='textured-nav-heading textured-nav-heading-unselected'][normalize-space()='Foretees']"


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


@base_logger()
def click_foretees(driver):
    locator = HomePageLocators.FORETEES_BUTTON_XPATH_1
    driver.find_element(By.XPATH, locator).click()


@base_logger()
def click_drop_down(driver):
    locator = HomePageDropDown.DD_BUTTON
    try:
        element = driver.find_element(By.XPATH, locator)
        element.click_and_hold()
        return element
    except selenium_exceptions as se:
        print(f"Exception Raised {se}")

    try:
        element = driver.find_element(By.XPATH, locator)
        element.click()
        return element
    except selenium_exceptions as se:
        print(f"Exception Raised {se}")


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
    # click_foretees(driver)
    click_drop_down(driver)
    # ================================================================ #
    # close Browser
    driver.close()
