from selenium import webdriver
import time


class CrawlingDriver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("disable-gpu")
        self.options.add_argument("headless")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        )
        self.driver = webdriver.Chrome("Crawling/chromedriver", options=self.options)
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
