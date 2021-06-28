from selenium import webdriver

# https://pypi.org/project/webdriver-manager/
from webdriver_manager.microsoft import EdgeChromiumDriverManager as Edge


class CrawlingDriver:
    def __init__(self) -> None:
        self.driver = webdriver.Edge(Edge().install())
        self.category: list = ["politics", "economy", "inter", "society", "sports"]
