from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a browser object that can open and close a url that is passed
# to it that way you can name the object whatever the name of the
# website is. Plus it can be used like a regular selenium object.


class Browser:

    # Change the actual path to the paths imported from secrets.py
    CHROMEDRIVER_PATH = r"C:\\Users\\charl\\webdriver\\chromedriver_win32\\chromedriver.exe"
    EDGEDRIVER_PATH = ""
    FIREFOXDRIVER_PATH = ""
    SAFARIDRIVER_PATH = ""

    def __init__(self, url, driver="Chrome"):
        self.url = url
        if driver == "FireFox":
            self.browser = webdriver.Chrome(Browser.FIREFOXDRIVER_PATH)
        elif driver == "Edge":
            self.browser = webdriver.Chrome(Browser.EDGEDRIVER_PATH)
        elif driver == "Safari":
            self.browser = webdriver.Chrome(Browser.SAFARIDRIVER_PATH)
        elif driver == "Chrome":
            self.browser = webdriver.Chrome(Browser.CHROMEDRIVER_PATH)

    def __repr__(self):
        return f"Browser Object Created: Using {self.driver} to open {self.url}"

    def browse(self):
        self.browser.get(self.url)

    def close(self):
        self.browser.close()

# ===========================


class HomePageLocators(object):
    """This class is for locators on the Home Page"""
    MEMBER_LOGIN = 'a#dnn_ctr354_HtmlModule_lblContent > a:nth-child(1)'


class LoginPageLocators(object):
    """This class is for locators on the Login Page"""
    MEMBER_ID_INPUT = "input#_58_login"
    MEMBER_PASSWORD_INPUT = "input#_58_password"
    MEMBER_LOGIN_BUTTON = "button#yui_patched_v3_11_0_1_1650332440143_231"


class LoggedInHomePageLocators:
    """This class is for locators on the members home page after logging in"""
    FORETEES_BUTTON = "#textured-cssmenu > ul > li:nth-child(5) > a > span"
