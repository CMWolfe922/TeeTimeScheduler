from locators import LoginPageLocators
from element import BasePageElement
from config.secrets import COURSE_URL, MEMBER_ID, PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.secrets import CHROMEDRIVER


class SearchForElements(BasePageElement):
    """This class confirms elements exist or are showing up"""

    # Home Page:
    dropdown_menu = ".humburger" # css selector

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    # Declares a variable that will contain the retrieved text
    search_text_element = SearchForElements()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Burl Oaks Golf Club" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*LoginPageLocators.BTN)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
