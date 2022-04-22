"""
This is the home page script that will be in control of the
functions and methods to find and click on the foretees
button.

It is proving to be extremely difficult due to the fact that
the element does not show up on the screen the way it's supposed to
or the way it is written in the code.

I need to create a way to resize the page to make sure the element
I am looking for shows up under the tag I am looking for. And make sure
the element is active.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from decorators import base_logger


class HomePageDropDown:
    """This class is for locators on the Home Page"""
    DROP_DOWN_MENU = ".ui-link"
    DD_BTN_ATTEMPT_1 = "//a[contains(@href, '#menu']"
    DD_FORETEES_BTN_XPATH = "//span[@class='smartphone-nav-heading'][normalize-space()='Foretees']"
    DD_BUTTON = "//div[@id='mm-menu-link']"
    FORETEES_DD_XPATH = "//span[@class='smartphone-nav-heading'][normalize-space()='Foretees']"


class HomePageLocators:
    """This class is for locators on the members home page after logging in"""
    FORETEES_BUTTON_PARTIAL = "Foretees"
    FORETEES_BUTTON_XPATH = "//span[text()[normalize-space()='Foretees']]"
    FORETEES_XPATH_LONG = "//div[@id='textured-cssmenu']/ul[1]/li[5]/a[1]/span[1]"
    FORETEES_BUTTON_CSS_SELECTOR = "div#textured-cssmenu>ul>li:nth-of-type(5)>a>span"
    FORETEES_BUTTON_PAGE_ID = "//*[@data-pageid='53']"
    # Error Message: selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
    FORETEES_BUTTON_XPATH_1 = "//span[@class='textured-nav-heading textured-nav-heading-unselected'][normalize-space()='Foretees']"
    FORETEES_BUTTON_XPATH_2 = "//a/span[contains(@class,'textured-nav-heading textured-nav-heading-unselected')][normalize-space()='Foretees']"


@base_logger()
def click_foretees(driver):
    locator = HomePageLocators.FORETEES_BUTTON_XPATH_2
    try:
        element = driver.find_element(By.XPATH, locator)
        element.click()
        return element

    except exceptions.ElementNotInteractableException as ni:
        print(f"Exception Raised {ni}")

    except exceptions.NoSuchElementException as ne:
        print(f"Exception Raised {ne}")

    except exceptions.ElementNotVisibleException as nv:
        print(f"Exception Raised {nv}")

    except AttributeError as ae:
        print(f"Error Raised {ae}")


@base_logger()
def click_drop_down(driver):
    locator = HomePageDropDown.DD_BUTTON
    foretees = HomePageDropDown.FORETEES_DD_XPATH
    try:
        element = driver.find_element(By.XPATH, locator)
        print(element)
        hover = ActionChains(driver).move_to_element(element).click()
        hover.move_to_element(foretees)
        hover.click()
        return hover
    except exceptions.ElementNotInteractableException as se:
        print(f"Exception Raised {se}")

    except AttributeError as ae:
        print("Element doesn't have that attribute ")


@base_logger()
def home_page(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.DROP_DOWN_MENU).click_and_hold()
        driver.implicitly_wait(10)
    except exceptions.ElementNotInteractableException as se:
        print(se)

class HomePageLocators:
    """Locators on Logged in home page"""

    DROP_DOWN_MENU_XPATH = "//div[@id='mm-menu-link']"
