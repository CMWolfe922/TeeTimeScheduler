from config.secrets import LOGIN_BTN, MEMBER_ID, PASSWORD
from selenium.webdriver.common.by import By
from decorators import base_logger
import time


class LoginPageLocators:
    """This class is for locators on the Login Page"""
    MEMBER_ID_INPUT = "_58_login"
    MEMBER_PASSWORD_INPUT = "_58_password"
    BTN_CSS_SELECTOR = LOGIN_BTN


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

