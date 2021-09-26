from CrawlingModule import CrawlingDriver
import time


class Herald(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "http://biz.heraldcorp.com/list.php?ct=010108000000",
            "economy": "http://biz.heraldcorp.com/list.php?ct=010104000000",
            "society": "http://biz.heraldcorp.com/list.php?ct=010109000000",
            "sport": "http://biz.heraldcorp.com/list.php?ct=010400000000",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(0, 10):
                self.getSite(self.url[category])
                if i == 0:
                    try:
                        article = self.getElement(
                            "/html/body/div/div[3]/div[2]/div[1]/a/div[2]/div[1]"
                        )
                        date = self.getElement("/html/body/div/div[3]/div[2]/div[1]/div").text
                    except:
                        continue
                else:
                    try:
                        article = self.getElement(
                            f"/html/body/div/div[3]/div[2]/div[3]/ul/li[{i}]/a/div[2]/div[1]"
                        )
                        date = self.getElement(
                            f"/html/body/div/div[3]/div[2]/div[3]/ul/li[{i}]/div"
                        ).text
                    except:
                        continue

                title = article.text
                article.click()
                time.sleep(2)

                mainText = ""
                j = 1

                while True:
                    try:
                        mainText += self.getElement(f"//*[@id='articleText']/p[{j}]").text
                        mainText += "\n"
                        j += 1

                    except:
                        break

                url = self.driver.current_url
                reporter = ""

                mainText = mainText.replace("\n", " ")

                date = date.replace(".", "-")

                img_src = ""
                try:
                    img_src = self.driver.find_element_by_css_selector(
                        "#heraldbizimg01"
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
                        "press": "헤럴드경제",
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
                        "press": "헤럴드경제",
                        "img": img_src,
                    }
                )

        return self.articles
