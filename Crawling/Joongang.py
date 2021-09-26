from CrawlingModule import CrawlingDriver
import time


class Joongang(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "https://www.joongang.co.kr/politics",
            "economy": "https://www.joongang.co.kr/money",
            "society": "https://www.joongang.co.kr/society",
            "sport": "https://www.joongang.co.kr/sports",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 10):
                self.getSite(self.url[category])
                try:
                    article = self.getElement(f'//*[@id="story_list"]/li[{i}]/div[2]/h2/a')
                except:
                    continue

                title = article.text

                try:
                    date = self.getElement(f'//*[@id="story_list"]/li[{i}]/div[2]/div/p').text
                except:
                    continue

                article.click()

                time.sleep(2)

                mainText = ""
                j = 1
                while True:
                    try:
                        mainText += self.getElement(f'//*[@id="article_body"]/p[{j}]').text
                        j += 1
                    except:
                        break

                try:
                    reporter = self.getElement(
                        '//*[@id="container"]/section/article/header/div[3]/a'
                    ).text
                except:
                    continue

                url = self.driver.current_url

                img_src = ""
                try:
                    img_src = self.driver.find_element_by_css_selector(
                        "#article_body > div.ab_photo.photo_center > div > img"
                    ).get_attribute("src")
                except:
                    img_src = ""
                    pass

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
                        "press": "중앙일보",
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
                        "press": "중앙일보",
                        "img": img_src,
                    }
                )
        return self.articles
