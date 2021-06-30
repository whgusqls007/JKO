from DongaDriver import Donga
import time


class test:
    def __init__(self) -> None:
        self.donga = Donga()
        self.time = 20

    def run(self) -> None:
        while True:
            crawlingResult = self.donga.run()
            if crawlingResult[1]:
                # DB 저장?
                dosometing = 0

            time.sleep(self.time)


if __name__ == "__main__":
    t = test()
    t.run()
