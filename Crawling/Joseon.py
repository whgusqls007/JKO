from CrawlingModule import CrawlingDriver
import time
import json

with open("/home/whgusqls007/JKO/Crawling/secret.json", "r") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    return secrets[setting]


ID = get_secret("JoseonID")
PW = get_secret("JoseonPW")


class Joseon(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "https://www.chosun.com/politics/",
            "economy": "https://www.chosun.com/economy/",
            "society": "https://www.chosun.com/national/",
            "sport": "https://www.chosun.com/sports/",
        }
        self.login()

    def login(self):
        self.driver.get("https://www.chosun.com/subscribe/signin/")

        time.sleep(3)

        self.driver.find_element_by_xpath("//*[@id='username']").send_keys(ID)
        self.driver.find_element_by_xpath("//*[@id='subsPassword']").send_keys(PW)
        self.driver.find_element_by_xpath(
            "//*[@id='fusion-app']/div[2]/div/div/div[5]/div[1]/label"
        ).click()
        self.driver.find_element_by_xpath("//*[@id='subsSignIn']").click()

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 10):
                self.getSite(self.url[category])
                try:
                    article = self.getElement(
                        f"//*[@id='main']/div[3]/section/div/div/div/div[{i}]/div/div/div/div[1]/div[2]/div[1]/a"
                    )
                except:
                    continue

                title = article.text

                article.click()

                time.sleep(2)

                try:
                    reporter = self.getElement(
                        "//*[@id='fusion-app']/div[1]/div[2]/div/section/article/div[1]/div/a"
                    ).text
                except:
                    continue

                try:
                    date = self.getElement(
                        "//*[@id='fusion-app']/div[1]/div[2]/div/section/article/div[2]/span"
                    ).text[3:]
                except:
                    continue
                mainText = ""
                j = 1
                while True:
                    try:
                        mainText += self.getElement(
                            f"//*[@id='fusion-app']/div[1]/div[2]/div/section/article/section/p[{j}]"
                        ).text
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
