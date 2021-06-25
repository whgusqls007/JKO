from selenium import webdriver
from bs4 import BeautifulSoup


class Choseon:
    def __init__(self) -> None:
        self.driverdir: str = "C:/msedgedriver.exe"
        # Local임 -> 나중에 바꿔야함
        self.catecory:list = [
            ""
        ]
