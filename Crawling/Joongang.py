from CrawlingModule import CrawlingDriver
import time


class Joongang(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "https://news.joins.com/politics?cloc=joongang-section-gnb2",
            "economy": "https://news.joins.com/money?cloc=joongang-section-gnb3",
            "society": "https://news.joins.com/society?cloc=joongang-section-gnb4",
            "sport": "https://news.joins.com/sports?cloc=joongang-section-gnb7",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 10):
                self.getSite(self.url[category])
                try:
                    article = self.getElement(
                        f"//*[@id='content']/div[3]/ul/li[{i}]/h2/a"
                    )
                except:
                    continue
                title = article.text
                try:
                    date = self.getElement(
                        f"//*[@id='content']/div[3]/ul/li[{i}]/span[3]"
                    ).text
                except:
                    continue

                article.click()

                time.sleep(2)

                try:
                    mainText = self.getElement("//*[@id='article_body']").text
                except:
                    continue

                j = 1
                while True:
                    try:
                        subText = self.getElement(
                            "//*[@id='article_body']/div[{j}]"
                        ).text
                        mainText = mainText.replace(subText, "")
                        j += 1
                    except:
                        break
                try:
                    reporter = self.getElement(
                        "//*[@id='content']/div[1]/div/dl/dd/span/strong/a"
                    ).text
                except:
                    continue

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
