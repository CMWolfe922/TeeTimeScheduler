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



class HomePageLocators:
    """This class is for locators on the Home Page"""
    DROP_DOWN_MENU = ".ui-link"


class LoginPageLocators:
    """This class is for locators on the Login Page"""
    MEMBER_ID_INPUT = "_58_login"
    MEMBER_PASSWORD_INPUT = "_58_password"
    BTN_CSS_SELECTOR = LOGIN_BTN


class HomePage:
    """This class is for locators on the members home page after logging in"""
    # partial link text
    FORETEES_BUTTON_PARTIAL = "Foretees"

    # xpath attempts
    FORETEES_BUTTON_XPATH = "//span[text()[normalize-space()='Foretees']]"
    FORETEES_XPATH_LONG = "//div[@id='textured-cssmenu']/ul[1]/li[5]/a[1]/span[1]"
    FORETEES_BUTTON_PAGE_ID = "//*[@data-pageid='53']"
    DD_BTN_ATTEMPT_1 = "//a[contains(@href, '#menu']"

    # css selector attempts
    DROP_DOWN_MENU = ".ui-link"
    FORETEES_BUTTON_CSS_SELECTOR = "div#textured-cssmenu>ul>li:nth-of-type(5)>a>span"
    DD_CSS_PATH = "html.aui.ltr.yui3-js-enabled.gecko.js.firefox.firefox99.firefox99-0.win.secure body.yui3-skin-sam.controls-visible.guest-site.signed-in.private-page.site.dockbar-split.body-bg div#mm-0.mm-page.mm-slideout div.vegas-slider div#wrap header.header_like_burl-oaks div.d-none.d-block.d-xs-block.d-sm-block.d-md-block.d-lg-none.public-menu-overlay-menu ul li div.text-right a.menu-text.ui-link"


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



def click_foretees(driver):

    drop_down = HomePage.DD_BTN_ATTEMPT_1
    driver.find_element(By.XPATH, drop_down).click_and_hold(10)

@base_logger()
def home_page(driver):
    try:
        element = driver.find_element(By.CSS_SELECTOR, HomePageLocators.DROP_DOWN_MENU).click_and_hold()
        if not element:
            try:
                driver.find_element(By.CSS_SELECTOR, HomePageLocators.DROP_DOWN_MENU).click_and_hold()
                driver.implicitly_wait(10)
            except selenium_exceptions as se:
                print(f"Exception Raised {se}")

    except selenium_exceptions as se:
        print(f"Exception Raised {se}")


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
    # home_page(driver)
    click_foretees(driver)

    # ================================================================ #
    # close Browser
    driver.close()
