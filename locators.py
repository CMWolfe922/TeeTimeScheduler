from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')
    LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, "Foretees")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass
