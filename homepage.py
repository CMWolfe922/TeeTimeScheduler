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

from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decorators import base_logger


class HomePage:
    """Locators on Logged in home page"""

    @base_logger()
    def wait_for_element(self, driver, locator:tuple, wait:int=60):
        """Wait for element to show up on page"""
        try:
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
            driver.implicitly_wait(wait / 3)