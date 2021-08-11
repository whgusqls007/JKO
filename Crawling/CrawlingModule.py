from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager as Firefox
from webdriver_manager.chrome import ChromeDriverManager as Chrome
from webdriver_manager.microsoft import EdgeChromiumDriverManager as Edge

import time


class CrawlingDriver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("Window-size=1920x1080")
        self.options.add_argument("headless")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        )
        self.driver = webdriver.Chrome(Chrome().install(), options=self.options)
        self.articles = []

    def getSite(self, url):
        self.driver.get(url)
        time.sleep(2)
        return

    def getElement(self, Xpath):
        return self.driver.find_element_by_xpath(Xpath)

    def quit(self):
        self.driver.quit()
        return
