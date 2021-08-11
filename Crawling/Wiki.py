from CrawlingModule import CrawlingDriver
import time


class Wiki(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "https://www.wikitree.co.kr/categories/4",
            "economy": "https://www.wikitree.co.kr/categories/68",
            "society": "https://www.wikitree.co.kr/categories/55",
            "sport": "https://www.wikitree.co.kr/categories/11",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 8):
                self.getSite(self.url[category])
                article = None
                if category == "economy":
                    try:
                        article = self.getElement(
                            f"//*[@id='content']/section[3]/ul/div[1]/li[{i}]/a/span[2]/span"
                        )
                    except:
                        continue
                else:
                    try:
                        article = self.getElement(
                            f"//*[@id='content']/section[2]/ul/div[1]/li[{i}]/a/span[2]/span"
                        )
                    except:
                        continue
                title = article.text
                article.click()
                time.sleep(2)

                try:
                    date = self.getElement(
                        "//*[@id='content']/div/div[1]/div/div/p[1]"
                    ).text
                except:
                    print("날짜시간 에러")
                    continue

                try:
                    reporter = self.getElement(
                        "//*[@id='content']/div/div[2]/div[1]/div[3]/div[1]/span[1]"
                    ).text
                except:
                    print("기자이름 에러")
                    continue

                mainText = ""
                j = 1
                while True:
                    try:
                        mainText += self.getElement(f"//*[@id='wikicon']/p[{j}]").text
                        mainText += "\n"
                        j += 1
                    except:
                        break

                url = self.driver.current_url

                mainText = mainText.replace("\n", " ")

                self.articles.append(
                    {
                        "_id": None,
                        "title": title,
                        "mainText": mainText,
                        "category": category,
                        "url": url,
                        "reporter": reporter,
                        "date": date,
                    }
                )
                print(
                    {
                        "_id": None,
                        "title": title,
                        "mainText": mainText,
                        "category": category,
                        "url": url,
                        "reporter": reporter,
                        "date": date,
                    }
                )
        return self.articles
