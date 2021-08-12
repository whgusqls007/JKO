from CrawlingModule import CrawlingDriver
import time


class Yeonhap(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "https://www.yna.co.kr/politics/index?site=navi_politics_depth01",
            "economy": "https://www.yna.co.kr/economy/index?site=navi_economy_depth01",
            "society": "https://www.yna.co.kr/society/index?site=navi_society_depth01",
            "sport": "https://www.yna.co.kr/sports/index?site=navi_sports_depth01",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 10):
                self.getSite(self.url[category])
                try:
                    article = self.getElement(
                        f"//*[@id='majorList']/li[{i}]/div/div[2]/a"
                    )
                except:
                    continue

                title = article.text
                try:
                    date = self.getElement(
                        f"//*[@id='majorList']/li[{i}]/div/div[1]/span[2]"
                    ).text
                except:
                    continue

                article.click()
                time.sleep(2)

                try:
                    reporter = self.getElement(
                        "//*[@id='articleWrap']/div[2]/div/div/article/div[1]/a/div/strong"
                    ).text
                except:
                    continue

                url = self.driver.current_url

                mainText = ""
                j = 1

                while True:
                    try:
                        mainText += self.getElement(
                            f"//*[@id='articleWrap']/div[2]/div/div/article/p[{j}]"
                        ).text
                        j += 1
                    except:
                        break

                mainText = mainText.replace("\n", "")

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
