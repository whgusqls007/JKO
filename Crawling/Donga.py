from CrawlingModule import CrawlingDriver
import time


class Donga(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "https://www.donga.com/news/Politics",
            "economy": "https://www.donga.com/news/Economy",
            "society": "https://www.donga.com/news/Society",
            "sport": "https://www.donga.com/news/Sports",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 10):
                self.getSite(self.url[category])
                try:
                    article = self.getElement(
                        f"//*[@id='content']/div[3]/div[1]/div/div/ul/li[{i}]/div/a[2]"
                    )
                except:
                    continue

                title = article.text
                article.click()
                time.sleep(2)

                try:
                    mainText = self.getElement("//*[@id='content']/div/div[1]").text
                except:
                    continue

                if mainText == "":
                    continue

                j = 1
                while True:
                    try:
                        subText = self.getElement(f"//*[@id='content']/div/div[1]/div[{j}]").text
                        mainText = mainText.replace(subText, "")
                        j += 1
                    except:
                        break

                url = self.driver.current_url

                try:
                    reporter = self.getElement("//*[@id='container']/div[2]/div[2]/span[1]").text
                except:
                    continue

                try:
                    date = self.getElement("//*[@id='container']/div[2]/div[2]/span[2]").text[3:]
                except:
                    continue

                mainText = mainText.replace("\n", " ")

                img_src = ""
                try:
                    img_src = self.driver.find_element_by_css_selector(
                        "#content > div > div.article_txt > div.articlePhotoC > span.thumb > img"
                    ).get_attribute("src")
                except:
                    img_src = ""
                    pass

                self.articles.append(
                    {
                        "_id": None,
                        "title": title,
                        "mainText": mainText,
                        "category": category,
                        "url": url,
                        "reporter": reporter,
                        "date": date,
                        "press": "동아일보",
                        "img": img_src,
                        "emotion": "",
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
                        "press": "동아일보",
                        "img": img_src,
                    }
                )
        return self.articles
