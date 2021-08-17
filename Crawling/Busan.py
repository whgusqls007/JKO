from CrawlingModule import CrawlingDriver
import time


class Busan(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "http://www.busan.com/politics/all/",
            "economy": "http://www.busan.com/economy/all/",
            "society": "http://www.busan.com/society/all/",
            "sport": "http://www.busan.com/sport/all/",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 10):
                self.getSite(self.url[category])
                try:
                    article = self.getElement(f"//*[@id='article_list']/li[{i}]/p[1]/a")
                except:
                    continue
                title = article.text
                try:
                    date = self.getElement(f"//*[@id='article_list']/li[{i}]/p[3]").text
                except:
                    continue

                if "포토뉴스" in title or "알림" in title:
                    continue

                article.click()

                time.sleep(2)

                j = 1
                mainText = ""

                while True:
                    try:
                        mainText += self.getElement(
                            f"//*[@id='container']/div[1]/div[1]/div[4]/p[{j}]"
                        ).text
                        j += 1
                    except:
                        break

                url = self.driver.current_url

                try:
                    reporter = self.getElement(
                        "//*[@id='container']/div[1]/div[1]/div[3]/div[1]/div[1]"
                    ).text
                except:
                    continue

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
