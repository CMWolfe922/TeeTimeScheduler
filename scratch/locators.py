from selenium.webdriver.common.by import By


class LoginPageLocators:
    """This class is for locators on the Login Page"""

    ID_INPUT = (By.ID, "_58_login")
    PW_INPUT = (By.ID, "_58_password")
    BTN = (By.CSS_SELECTOR, ".mm_login.login-page .background-wrap #content-wrapper-login .login-col-left .button-holder .btn")


class HomePageLocators(object):
    """A class for home page locators. All home page locators come here"""

    DD_MENU = (By.XPATH, "//*[@id='mm-menu-link']")
    BUTTON = (By.XPATH, "/html/body/nav/div[2]/div[1]/ul/li[5]/a/span")


class ForeTeesLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass
