from CrawlingModule import CrawlingDriver
import time


class Hangook(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "https://www.hankookilbo.com/News/Politics",
            "economy": "https://www.hankookilbo.com/News/Economy",
            "society": "https://www.hankookilbo.com/News/Society",
            "sport": "https://www.hankookilbo.com/Sports",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 10):
                self.getSite(self.url[category])
                try:
                    article = self.getElement(
                        f"//*[@id='section-bottom-article-list']/li[{i}]/div[1]/h4/a"
                    )
                except:
                    continue

                title = article.text

                try:
                    date = self.getElement(
                        f"//*[@id='section-bottom-article-list']/li[{i}]/div[1]/div[1]/span"
                    ).text
                except:
                    continue

                try:
                    mainText = self.getElement(
                        f"//*[@id='section-bottom-article-list']/li[{i}]/div[1]/div[2]/a"
                    ).text
                except:
                    continue
                try:
                    while True:
                        try:
                            article.click()
                            if self.driver.current_url != self.url[category]:
                                break
                        except:
                            self.driver.execute_script(
                                "window.scrollTo(0, document.body.scrollHeight);"
                            )
                            self.getSite(self.url[category])
                            self.driver.execute_script(
                                "window.scrollTo(0, document.body.scrollHeight);"
                            )
                            article = self.getElement(
                                f"//*[@id='section-bottom-article-list']/li[{i}]/div[1]/h4/a"
                            )
                except:
                    continue

                time.sleep(2)

                try:
                    reporter = self.driver.find_element_by_class_name("writer").text
                except:
                    continue

                url = self.driver.current_url

                mainText = mainText.replace("\n", " ")

                date = date.replace(".", "-")

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
