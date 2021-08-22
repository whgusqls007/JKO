from CrawlingModule import CrawlingDriver
import time


class Nocut(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "https://www.nocutnews.co.kr/news/politics/list",
            "economy": "https://www.nocutnews.co.kr/news/economy/list",
            "society": "https://www.nocutnews.co.kr/news/society/list",
            "sport": "https://www.nocutnews.co.kr/news/sports/list",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 10):
                self.getSite(self.url[category])
                try:
                    article = self.getElement(
                        f"//*[@id='pnlNewsList']/ul/li[{i}]/dl/dt/a"
                    )
                except:
                    continue

                title = article.text
                if (
                    "[영상]" in title
                    or "[노컷브이]" in title
                    or "[윤태곤의 판]" in title
                    or "[인터뷰]" in title
                ):
                    continue
                article.click()
                time.sleep(2)
                try:
                    mainText = self.getElement("//*[@id='pnlContent']").text
                except:
                    continue

                try:
                    subText = self.getElement("//*[@id='pnlContent']/span").text
                    mainText = mainText.replace(subText, "")
                except:
                    pass

                j = 1
                while True:

                    try:
                        subText = self.getElement(
                            f"//*[@id='pnlContent']/span[{j}]"
                        ).text
                        mainText = mainText.replace(subText, "")
                        j += 1
                    except:
                        break

                j = 1
                while j < 20:
                    try:
                        subText = self.getElement(
                            f"//*[@id='pnlContent']/div[{j}]/span"
                        ).text
                        mainText = mainText.replace(subText, "")
                        j += 1
                    except:
                        j += 1
                        continue

                try:
                    subText = self.getElement("//*[@id='pnlContent']/div[2]").text
                    mainText = mainText.replace(subText, "")
                except:
                    pass

                try:
                    subText = self.getElement("//*[@id='pnlContent']/div[3]").text
                    mainText = mainText.replace(subText, "")
                except:
                    pass

                try:
                    subText = self.getElement("//*[@id='pnlContent']/div[4]").text
                    mainText = mainText.replace(subText, "")
                except:
                    pass

                url = self.driver.current_url

                try:
                    reporter = self.getElement(
                        "//*[@id='pnlViewTop']/div[2]/ul/li[1]/a[1]"
                    ).text
                except:
                    try:
                        reporter = self.getElement(
                            "//*[@id='pnlViewTop']/div[3]/ul/li[1]/a[1]"
                        ).text
                    except:
                        continue

                if reporter == "메일보내기" or reporter == "메일 보내기":
                    try:
                        reporter = self.getElement(
                            "//*[@id='pnlViewTop']/div[2]/ul/li[1]/span"
                        ).text
                    except:
                        reporter = self.getElement(
                            "//*[@id='pnlViewTop']/div[3]/ul/li[1]/span"
                        ).text

                try:
                    date = self.getElement("//*[@id='pnlViewTop']/div[2]/ul/li[2]").text
                except:
                    try:
                        date = self.getElement(
                            "//*[@id='pnlViewTop']/div[3]/ul/li[2]"
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
