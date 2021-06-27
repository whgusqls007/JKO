import time
from selenium import webdriver

# https://pypi.org/project/webdriver-manager/
from webdriver_manager.microsoft import EdgeChromiumDriverManager as Edge


class Crawling:
    def __init__(self) -> None:
        self.driver = webdriver.Edge(Edge().install())
        self.time: int = 100

    def crawlingTimer(self) -> None:
        while True:
            # time 마다 한 사이트씩 크롤링을 진행
            # time 은 실제 동작 시간을 측정후 적절한 값을 선택해야할듯
            time.sleep(self.time)
            # Call
            time.sleep(self.time)
            # Call
            time.sleep(self.time)
            # Call
