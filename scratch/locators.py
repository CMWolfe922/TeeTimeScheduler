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

class ForeTeesLocators:
    """A class for search results locators. All search results locators should
    come here"""

    TEE_TIMES = (By.XPATH, "//div[@id='rwdNav']//ul//li[@class='topnav_item ']//a[@href='#']//span[@class='topnav_item'][normalize-space()='Tee Times']")
    MCV_TEE_TIMES = (By.XPATH, "//div[@id='rwdNav']//ul//li[@class='topnav_item ']//ul//li[@aria-haspopup='false']//a[@href='Member_select']//span[contains(text(),'Make, Change, or View Tee Times')]")
    # I need to figure out how to change the 29 to whatever I want or to todays date + 7
    CALENDAR = (By.XPATH, "(//a[normalize-space()='29'])[1]")
    # I need to figure out how to change the 8:00AM to whatever time is in the config.ini file. and create
    # a function that selects the three time slots after whichever timeslot Kevin Chooses.
    TEE_TIME_LINK = (By.XPATH, "//a[normalize-space()='8:00 AM']")
    ClickOnPartner = "//span[normalize-space()='Frank, Jordan (12.5)']"
    PARTNERS_LINK = (By.XPATH, "(//a[normalize-space()='Select Player #2'])[1]")
