
from config.secrets import COURSE_URL, PASSWORD, MEMBER_ID
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decorators import logger, timer
import time


# Path to Chrome Driver
CHROMEDRIVER_PATH = r"C:\\Users\\charl\\webdriver\\chromedriver_win32\\chromedriver.exe"
FIREFOXDRIVER_PATH = r"C:\Users\charl\webdriver\geckodriver-v0.31.0-win64\geckodriver.exe"


class HomePageLocators:
    """This class is for locators on the Home Page"""
    MEMBER_LOGIN = 'a#dnn_ctr354_HtmlModule_lblContent > a:nth-child(1)'
    MEMBER_LOGIN_LINK = "https://members.burloaksgolfclub.com/web/pages/login"


class LoginPageLocators:
    """This class is for locators on the Login Page"""
    MEMBER_ID_INPUT = "_58_login"
    MEMBER_PASSWORD_INPUT = "_58_password"
    MEMBER_LOGIN_BUTTON = ".mm_login.login-page .background-wrap #content-wrapper-login .login-col-left .button-holder .btn"


class LoggedInHomePageLocators:
    """This class is for locators on the members home page after logging in"""
    FORETEES_BUTTON_PARTIAL = "Foretees"
    FORETEES_BUTTON_XPATH = "//*[@id='textured-cssmenu'']/ul/li[5]/a"
    FORETEES_BUTTON_CSS_SELECTOR = "li.textured-nav-parent:nth-child(5) > a:nth-child(1) > span:nth-child(1)"


def login():

    # find member id input box:
    driver.find_element(
        By.ID, LoginPageLocators.MEMBER_ID_INPUT).send_keys(MEMBER_ID)

    # find password input box
    driver.find_element(
        By.ID, LoginPageLocators.MEMBER_PASSWORD_INPUT).send_keys(PASSWORD)

    # find submit button to login
    driver.find_element(
        By.CSS_SELECTOR, LoginPageLocators.MEMBER_LOGIN_BUTTON).click()

    time.sleep(5)


def click_foretees():

    # find the foretees button using CSS_SELECTOR
    driver.find_element(
        By.PARTIAL_LINK_TEXT, LoggedInHomePageLocators.FORETEES_BUTTON).click()

    time.sleep(5)


if __name__ == '__main__':
    # Create a webdriver instance
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)

    # Open the url with driver
    driver.get(COURSE_URL)
    # ================================================================ #
    # RUN INITIAL PROGRAM FUNCTIONS:
    # ================================================================ #

    # run login function
    login()

    # run click foretees function
    click_foretees()

    # ================================================================ #
    # close Browser
    driver.close()
