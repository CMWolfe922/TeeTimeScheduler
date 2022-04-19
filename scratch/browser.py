from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a browser object that can open and close a url that is passed
# to it that way you can name the object whatever the name of the
# webA


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
