from CrawlingModule import CrawlingDriver
import time


class Ohmynews(CrawlingDriver):
    def __init__(self):
        CrawlingDriver.__init__(self)
        self.url = {
            "politics": "http://www.ohmynews.com/NWS_Web/ArticlePage/Total_Article.aspx?PAGE_CD=C0400",
            "economy": "http://www.ohmynews.com/NWS_Web/ArticlePage/Total_Article.aspx?PAGE_CD=C0300",
            "society": "http://www.ohmynews.com/NWS_Web/ArticlePage/Total_Article.aspx?PAGE_CD=C0200",
            "sport": "http://star.ohmynews.com/NWS_Web/OhmyStar/at_list.aspx?STAR_KND=95",
        }

    def crawling(self):
        self.articles.clear()
        for category in self.url:
            for i in range(1, 12):
                self.getSite(self.url[category])
                if category == "sport":
                    try:
                        article = self.getElement(
                            f"//*[@id='aspnetForm']/div[5]/section/div[2]/ul/li[{i}]/div/div/p[1]/a"
                        )
                    except:
                        continue
                    title = article.text
                    if "만평" in title or "오마이포토" in title or "오마이스타" in title:
                        continue
                    try:
                        reporterAndDate = self.getElement(
                            f"//*[@id='aspnetForm']/div[5]/section/div[2]/ul/li[{i}]/div/div/p[3]/a"
                        ).text
                        print(reporterAndDate)
                    except:
                        continue
                    reporter = reporterAndDate.split(" 21.")[0]
                    date = "2021." + reporterAndDate.split(" 21.")[1]
                    try:
                        article.click()
                    except:
                        continue
                    time.sleep(2)
                    try:
                        mainText = self.getElement(
                            "//*[@id='aspnetForm']/div[3]/section[1]/section[2]/div[2]/div[1]"
                        ).text
                    except:
                        continue
                    try:
                        subText = self.getElement(
                            "//*[@id='aspnetForm']/div[3]/section[1]/section[2]/div[2]/div[1]/div"
                        ).text
                        mainText = mainText.replace(subText, "")
                    except:
                        pass

                    j = 1
                    while True:
                        try:
                            subText = self.getElement(
                                f"//*[@id='aspnetForm']/div[3]/section[1]/section[2]/div[2]/div[1]/div[{j}]"
                            ).text
                            mainText = mainText.replace(subText, "")
                            j += 1
                        except:
                            break

                    try:
                        subText = self.getElement(
                            "//*[@id='aspnetForm']/div[3]/section[1]/section[2]/div[2]/div[1]/a"
                        ).text
                        mainText = mainText.replace(subText, "")
                    except:
                        pass

                    j = 1
                    while True:
                        try:
                            subText = self.getElement(
                                f"//*[@id='aspnetForm']/div[3]/section[1]/section[2]/div[2]/div[1]/a[{j}]"
                            ).text
                            mainText = mainText.replace(subText, "")
                            j += 1
                        except:
                            break

                    if "[관련 기사]" in mainText:
                        mainText = mainText.replace("[관련 기사]", "")

                else:
                    try:
                        article = self.getElement(
                            f"//*[@id='content_wrap']/div[1]/ul/li[{i}]/div/div/dl/dt/a"
                        )
                    except:
                        continue
                    title = article.text
                    if "만평" in title or "오마이포토" in title or "[사진]" in title:
                        continue
                    try:
                        reporterAndDate = self.getElement(
                            f"//*[@id='content_wrap']/div[1]/ul/li[{i}]/div/div/p"
                        ).text
                    except:
                        continue
                    print(reporterAndDate)
                    reporter = reporterAndDate.split("l21.")[0]
                    date = "2021." + reporterAndDate.split("l21.")[1]

                    try:
                        article.click()
                    except:
                        continue
                    time.sleep(2)
                    try:
                        mainText = self.getElement(
                            "//*[@id='content_wrap']/div[1]/div[3]/div[1]/div[1]/div[1]/div"
                        ).text
                    except:
                        continue
                    try:
                        subText = self.getElement(
                            "//*[@id='content_wrap']/div[1]/div[3]/div[1]/div[1]/div[1]/div/table"
                        ).text
                        mainText = mainText.replace(subText, "")
                    except:
                        pass

                    j = 1
                    while True:
                        try:
                            subText = self.getElement(
                                f"//*[@id='content_wrap']/div[1]/div[3]/div[1]/div[1]/div[1]/div/table[{j}]"
                            ).text
                            mainText = mainText.replace(subText, "")
                            j += 1
                        except:
                            break

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
