#!/usr/bin/env python3

from config.secrets import TT_MENU, TT_MENU_BTN
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.secrets import CHROMEDRIVER, COURSE_URL
from decorators import base_logger

"""
This script will be responsible for scheduling the round of golf. Once I can have
it schedule one round I should be able to put it on a loop to schedule 4 rounds.

Create a 'TODO' list of each step that needs to take place. That way I don't 
miss anything. I can use the saved recorded steps. 
"""


# TODO: Hover on top of 'Tee Times' to then move mouse down one; Element XPATH below

#  Remember to just hover
TEE_TIMES = "//body/div[@id='wrapper']/div[@id='rwd_wrapper']/div[@id='pageHeader']/div[@id='rwdNavBlock']/div[@id='rwdNav']/ul/li[1]/a[1]"

# RESULT: drop down menu with 4 options shows up.

# TODO: 'Move Mouse' to the 'Make, Change, or View Tee Times' element and click()
MCV_TEE_TIMES = "//div[@id='rwdNav']//ul//li[@class='topnav_item ']//ul//li[@aria-haspopup='false']//a[@href='Member_select']//span[contains(text(),'Make, Change, or View Tee Times')]"

# RESULT: Get Brought to the Select Dates Page with the calendar

# TODO: click the date one week ahead of today (so if monday click next monday,
#  if tuesday click next tuesday, etc..)

# Calendar Locator/Selector below
CALENDAR = "(//a[normalize-space()='29'])[1]"

# RESULT: The Tee Time scheduler shows up. This is where you pick the time and your four team mates.

# TODO: Click on the time saved in the options file.

TEE_TIME_LINK = "//a[normalize-space()='8:00 AM']"

# RESULT: Go to the screen where you select the players with whom you want to play with:

# TODO: Select players for this session (4 per session) first four in partners

PARTNERS_LINK = "(//a[normalize-space()='Select Player #2'])[1]"


ClickOnPartner= "//span[normalize-space()='Frank, Jordan (12.5)']"


class ForeTeesLocators:

    TEE_TIMES = (By.XPATH, "//div[@id='rwdNav']//ul//li[@class='topnav_item ']//a[@href='#']//span[@class='topnav_item'][normalize-space()='Tee Times']")
    MCV_TEE_TIMES = (By.XPATH, "//div[@id='rwdNav']//ul//li[@class='topnav_item ']//ul//li[@aria-haspopup='false']//a[@href='Member_select']//span[contains(text(),'Make, Change, or View Tee Times')]")
    # I need to figure out how to change the 29 to whatever I want or to todays date + 7
    CALENDAR = (By.XPATH, "(//a[normalize-space()='29'])[1]")
    # I need to figure out how to change the 8:00AM to whatever time is in the config.ini file. and create
    # a function that selects the three time slots after whichever timeslot Kevin Chooses.
    TEE_TIME_LINK = (By.XPATH, "//a[normalize-space()='8:00 AM']")


class ForeTees:
    """This is a action class. The methods are for making specific actions happen on the
    foretees website once logged in"""

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
    def determine_time(self, locator, t, driver):
        """This method picks the tee time"""
        pass



