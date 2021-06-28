from CrawlingDriver import CrawlingDriver as CD
from DongaDriver import Donga
import time


class test:
    def __init__(self) -> None:
        self.donga = Donga()
        self.time = 100

    def run(self) -> None:
        while True:
            self.donga.startCrawling()
            time.sleep(self.time)


if __name__ == "__main__":
    t = test()
    t.run()
