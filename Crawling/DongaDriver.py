from selenium import webdriver
from bs4 import BeautifulSoup


class Donga:
    def __init__(self) -> None:
        self.driverdir: str = "C:/msedgedriver.exe"
        # Local임 -> 나중에 바꿔야함
        self.catecory: dict = {
            "politics": "https://www.donga.com/news/Politics",
            "economy": "https://www.donga.com/news/Economy",
            "inter": "https://www.donga.com/news/Inter",
            "society": "https://www.donga.com/news/Society",
            "sports": "https://www.donga.com/news/Sports"
        }

    def test(self, str):
        print(self.catecory[str])


if __name__ == "__main__":
    D = Donga()
    D.test("politics")
