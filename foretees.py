#!/usr/bin/env python3

from config.secrets import TT_MENU, TT_MENU_BTN, TEE_TIME, DAYS_AHEAD
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.secrets import CHROMEDRIVER, COURSE_URL
from decorators import base_logger
import datetime

"""
This script will be responsible for scheduling the round of golf. Once I can have
it schedule one round I should be able to put it on a loop to schedule 4 rounds.

Create a 'TODO' list of each step that needs to take place. That way I don't 
miss anything. I can use the saved recorded steps. 
"""


def schedule_tee_time_number_of_days_ahead(number_of_days=int(DAYS_AHEAD)):
    # Date of next round (always schedules seven days ahead of when the script is automatically run
    today = datetime.date.today()
    date_of_round = today + datetime.timedelta(days=number_of_days)
    day = datetime.datetime.strptime(str(date_of_round), "%Y-%m-%d")
    dow = day.day
    return dow


# This should be 7 but can bee changed if needed in the config.ini file
dow = schedule_tee_time_number_of_days_ahead()
partner_name = ""


class ForeTeesLocators:

    TEE_TIME_LINKS = (By.XPATH, "//div[@id='rwdNav']//ul//li[@class='topnav_item ']//a[@href='#']//span[@class='topnav_item'][normalize-space()='Tee Times']")
    MCV_TEE_TIMES = (By.XPATH, "//div[@id='rwdNav']//ul//li[@class='topnav_item ']//ul//li[@aria-haspopup='false']//a[@href='Member_select']//span[contains(text(),'Make, Change, or View Tee Times')]")
    TEETIME = (By.XPATH, "//a[normalize-space()='{}']".format(int(TEE_TIME)))
    CALENDAR = (By.XPATH, "(//a[normalize-space()='{}'])[1]".format(dow))
    PARTNER2 = (By.XPATH, "(//a[normalize-space()='Select Player #2'])[1]")
    PARTNER3 = (By.XPATH, "(//a[normalize-space()='Select Player #3'])[1]")
    PARTNER4 = (By.XPATH, "(//a[normalize-space()='Select Player #4'])[1]")
    PARTNERS_BY_NAME = (By.XPATH, "//span[normalize-space()='{}']".format(partner_name))

class ForeTees:
    """This is an action class. The methods are for making specific actions happen on the
    foretees website once logged in"""

    # Class Properties:

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
    def pick_date(self, driver, wait:int=60):
        """This method selects the date for the next tee time"""
        locator = ForeTeesLocators.CALENDAR
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(locator))
        print(element)
        element.click()


    @base_logger()
    def pick_tee_time(self, driver, wait:int=60):
        """This method picks the tee time"""
        time = ForeTeesLocators.TEETIME
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(time))
        print(element)
        element.click()



    @base_logger()
    def tee_time_scheduler(self, locator, time, calendar):

        pass


