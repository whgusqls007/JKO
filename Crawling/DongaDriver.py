import selenium
from CrawlingDriver import CrawlingDriver


class Donga(CrawlingDriver):
    def __init__(self) -> None:
        CrawlingDriver.__init__(self)
        # 각 카테고리별 링크
        self.catecoryDir: dict = {
            "politics": "https://www.donga.com/news/Politics",
            "economy": "https://www.donga.com/news/Economy",
            "inter": "https://www.donga.com/news/Inter",
            "society": "https://www.donga.com/news/Society",
            "sports": "https://www.donga.com/news/Sports",
        }
        self.lastTitle: dict = {
            "politics": "",
            "economy": "",
            "inter": "",
            "society": "",
            "sports": "",
        }

    def startCrawling(self) -> None:
        articlePhoto: selenium
        relationArticle: str
        articleText: str
        photoDes: list = []
        title: str

        try:
            for category in self.category:
                # 사이트 접근
                self.getSite(category)

                # 기사 제목
                try:
                    title: str = self.driver.find_element_by_xpath(
                        '//*[@id="container"]/div[2]/h1'
                    ).text
                except:
                    title = ""

                # 기사 내용
                try:
                    articleText = self.driver.find_element_by_xpath(
                        '//*[@id="content"]/div/div[1]'
                    ).text
                except:
                    articleText = ""

                # 사진이 있을때
                try:
                    articlePhoto = self.driver.find_elements_by_class_name(
                        "articlePhotoC"
                    )
                    for i in articlePhoto:
                        photoDes.append(i.text)

                    # 사진 description 지우기
                    for des in photoDes:
                        articleText = articleText.replace(des, "")
                except:
                    articlePhoto = None

                # 관련 기사 지우기
                try:
                    relationArticle = self.driver.find_element_by_class_name(
                        "article_relation"
                    ).text

                    articleText = articleText.replace(relationArticle, "")
                except:
                    relationArticle = ""

                print(title)
                print("\n")
                print(articleText)
                # print("\n")
                # for des in articlePhoto:
                #     print(des.text, "\n")
                # print(relationArticle)

        except:
            print("ERROR")

        finally:
            self.driver.quit()
            # self.driver.close()

        return

    def getSite(self, catecory: str) -> None:
        self.driver.get(self.catecoryDir[catecory])
        title: str = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[3]/div[1]/div/div/ul/li[1]/div/a[2]'
        )
        title.click()
        return
