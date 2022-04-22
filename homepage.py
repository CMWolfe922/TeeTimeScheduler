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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decorators import Timer, Log
from config.secrets import DROPDOWN_LINK, DROPDOWN_DIV, FORETEES_DROPDOWN_BTN, FORETEES_TOP_BTN
from config.secrets import CHROMEDRIVER, FIREFOXDRIVER, SAFARIDRIVER, EDGEDRIVER

@Timer()
@Log(level="TRACE").catch()
def click_foretees(driver):
    locator = FORETEES_TOP_BTN
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


@Timer()
@Log(level="TRACE").catch()
def click_drop_down(driver):
    locator = DROPDOWN_DIV
    foretees = DROPDOWN_LINK
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


@Timer()
@Log(level="TRACE").catch()
def home_page(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, DROPDOWN_DIV).click()
        driver.implicitly_wait(10)
    except exceptions.ElementNotInteractableException as se:
        print(se)


class HomePage:
    """Locators on Logged in home page"""

    def __init__(self, url, driver_name="Chrome"):
        self.url = url
        if driver_name == "FireFox":
            self.driver = webdriver.Chrome(FIREFOXDRIVER)
        elif driver_name == "Edge":
            self.driver = webdriver.Chrome(EDGEDRIVER)
        elif driver_name == "Safari":
            self.driver = webdriver.Chrome(SAFARIDRIVER)
        elif driver_name == "Chrome":
            self.driver = webdriver.Chrome(CHROMEDRIVER)

    def __repr__(self):
        return f"Browser Object Created: Using {self.driver} to open {self.url}"

    @Timer()
    @Log()
    def wait_for_element(self, locator:tuple, wait:int=60):
        """Wait for element to show up on page"""
        try:
            driver = self.driver
            driver.maximize_window()
            driver.get(self.url)
            element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(locator))
            text = element.text
            if text:
                print(text)
                element.click()

            else:
                raise exceptions.NoSuchElementException

        except exceptions.ElementNotInteractableException as ni:
            print(f"Exception: {ni}")

        except exceptions.NoSuchElementException as ne:
            print(f"Exception: {ne}")

        except exceptions.ElementNotVisibleException as nv:
            print(f"Exception: {nv}")

        except AttributeError as ae:
            print(f"Error: {ae}")

        finally:
            self.driver.implicitly_wait(wait / 3)