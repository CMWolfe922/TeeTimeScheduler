import os
from decorators import logger, timer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config.secrets import CHROMEDRIVER  # PATH TO CHROME DRIVER

# a Few Test urls here
google = 'https://google.com'
yahoo = 'https://yahoo.com'
cnn = 'https://cnn.com'
URLs = [google, yahoo, cnn]


class BasicWebScraper(unittest.TestCase):

    def __init__(self, urls=URLs, driver_path=CHROMEDRIVER, **kwargs):
        self.driver_path = driver_path
        self.url = os.random.choice(urls)
        self.driver = webdriver.Chrome(CHROMEDRIVER)

    def close(self):
        self.driver.close()

    def get_page_source(self):
        page_source = self.driver.page_source
        return page_source

    def get_page_title(self):
        title = self.driver.page_title
        return title

    def get_all_links(self):
        links = self.driver.find_elements(By.TAG_NAME)
        return links


def main(driver_instance):
    title = scraper.get_page_title()
    page_source = scraper.page_source()
    links = scraper.get_all_links()

    data = {'title': title, 'page source': page_source, 'links': links}

    for k, v in data.items():
        print(f"{k} => {v}")


if __name__ == '__main__':
    scraper = BasicWebScraper()
    main(scraper)
