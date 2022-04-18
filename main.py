from browser import Browser
from config.secrets import COURSE_URL
from selenium.webdriver.common.keys import Keys

# Create a Browser Instance with the COURSE_URL > This is also a selenium object
# so it will work with all the same selenium methods.
course_browser = Browser(COURSE_URL)

# Step 1: Open Browser
course_browser.open()

# Step 2: Click Member Login


# Final Step: Close Browser
course_browser.close()
