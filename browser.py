from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config.secrets import COURSE_URL


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

    def open(self):
        self.browser.get(self.url)

    def close(self):
        self.browser.close()


# Create a class for user interface
class UserInterface:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        print(self.args, self.kwargs)


# ================================================================================ #

# create a Browser instance to import into the main file.
browser = Browser(COURSE_URL)
