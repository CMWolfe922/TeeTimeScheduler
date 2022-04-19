
from config.secrets import COURSE_URL, PASSWORD, MEMBER_ID
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Path to Chrome Driver
CHROMEDRIVER_PATH = r"C:\\Users\\charl\\webdriver\\chromedriver_win32\\chromedriver.exe"


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


# Create a webdriver instance
driver = webdriver.Chrome(COURSE_URL)

# open the webpage
browse = browser.browse()

# Create a HomePageLocator object HPL to search for the button
HPL = HomePageLocators()

# Search for the HPL object
homePageElem = browse.find_element_by_css_selector(HPL.MEMBER_LOGIN)

# Click the button
homePageElem.click()

# Close Page
browse.close()
