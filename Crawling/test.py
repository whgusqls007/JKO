from DongaDriver import Donga
import time


class test:
    def __init__(self) -> None:
        self.donga = Donga()
        self.time = 20

    def run(self) -> None:
        while True:
            crawlingResult = self.donga.run()
            print(crawlingResult[0]["politics"].refer(0))
            time.sleep(self.time)


if __name__ == "__main__":
    t = test()
    t.run()
