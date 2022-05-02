from config.secrets import LOGIN_BTN, MEMBER_ID, PASSWORD
from config.secrets import CHROMEDRIVER, COURSE_URL
from config.secrets import DROPDOWN_LINK, DROPDOWN_DIV, FORETEES_DROPDOWN_BTN, FORETEES_TOP_BTN
from config.secrets import TT_MENU_BTN, TT_MENU

from decorators import base_logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import date, timedelta
import json

# TEE_TIME and DAY_OF_WEEK need to be changed in settings file.
TEE_TIME = ""
DAY_OF_WEEK = ""
MEMBER_ID_INPUT = "_58_login"
MEMBER_PASSWORD_INPUT = "_58_password"
BTN_CSS_SELECTOR = LOGIN_BTN


class TeeTimeScheduler:
    """This class is for locators on the Login Page"""
    def __init__(self, tee_time, day_of_week):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.browser = webdriver.Chrome(executable_path=CHROMEDRIVER, options=chrome_options)
        self.url = COURSE_URL
        self.browser.get(self.url)
        self.tee_time = TEE_TIME
        self.day_of_week = DAY_OF_WEEK

    @base_logger()
    def login(self, driver):
        # find member id input box:
        driver.find_element(
            By.ID, MEMBER_ID_INPUT).send_keys(MEMBER_ID)

        # find password input box
        driver.find_element(
            By.ID, MEMBER_PASSWORD_INPUT).send_keys(PASSWORD)

        # find submit button to login
        driver.find_element(By.CSS_SELECTOR, LOGIN_BTN).click()
        # driver.find_element(By.CSS_SELECTOR, TeeTimeScheduler.BTN_CSS_SELECTOR).click()
        time.sleep(5)

    @base_logger()
    def wait_for_element(self, driver, locator:tuple, wait:int=60):
        """Wait for element to show up on page"""
        try:
            element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(locator))
            text = element.text
            if text:
                print(text)
                element.click()

            else:
                raise exceptions.NoSuchElementException

        except exceptions.ElementNotInteractableException as ni:
            print(f"Exception: {ni}")

        except exceptions.NoSuchElementException as ne:
            print(f"Exception: {ne}")

        except exceptions.ElementNotVisibleException as nv:
            print(f"Exception: {nv}")

        except AttributeError as ae:
            print(f"Error: {ae}")

        finally:
            driver.implicitly_wait(wait / 3)

    @base_logger()
    def hover_and_click_tee_times(self, locator, target, driver):
        """
        This is the first action to take on the ForeTess website once on it.

        :param locator: First element on ForeTees' site (top menu) to hover over and allow
        to move to target element. import TT_MENU from secrets.py

        :param target: Second element to interact with on ForeTees. While hovering over menu
        move mouse to target and click. import TT_MENU_BTN from secrets.py

        :param driver: This is the standard driver that will be created on the main page.
        """
        try:
            menu = driver.find_element(By.XPATH, locator)
            menu_btn = driver.find_element(By.XPATH, target)
            actions = ActionChains(driver)
            actions.move_to_element(menu)
            actions.click(menu_btn)
            actions.perform()

        except exceptions.NoSuchElementException as ne:
            print(ne)

        except exceptions.ElementNotInteractableException as ni:
            print(ni)

        except exceptions.ElementNotVisibleException as nv:
            print(nv)

        except exceptions.ElementNotSelectableException as ns:
            print(ns)

        finally:
            print("[+] ForeTees page method complete")

    @base_logger()
    def scheduler(self, day, time):
        """
        This method is for the scheduling of the tee time.
        :param day: day of the week that the tee time should be scheduled.
        :param time: time that the tee time would be scheduled for.
        """

        pass