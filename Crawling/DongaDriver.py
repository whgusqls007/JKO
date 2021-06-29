import selenium
import time
from CrawlingDriver import CrawlingDriver


class Donga(CrawlingDriver):
    def __init__(self) -> None:
        CrawlingDriver.__init__(self)
        # 각 카테고리별 링크
        self.initialize = False
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
        self.lastArticle: dict = {
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
                self.getMainSite(category)

                # 마지막 기사부터 몇개의 새로운 기사가 있는지 검사
                newArticles = self.getAllTitle(category)

                if newArticles == -1:
                    # -1일때 기사 제목 초기화
                    self.lastTitle[category] = ""
                    continue

                for newArticle in range(newArticles, 0, -1):
                    self.getSite(category, newArticle)
                    # 기사 제목
                    try:
                        title: str = self.driver.find_element_by_xpath(
                            "//*[@id='container']/div[2]/h1"
                        ).text
                    except:
                        title = ""

                    # 기사 내용
                    try:
                        articleText = self.driver.find_element_by_xpath(
                            "//*[@id='content']/div/div[1]"
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

                    print(title + "-" + category)
                    self.lastTitle[category] = title
                    self.lastArticle[category] = articleText
                    print("\n")
                    # print(articleText)
                    # print("\n")
                    # for des in articlePhoto:
                    #     print(des.text, "\n")
                    # print(relationArticle)

            for a in self.lastTitle:
                print(a, self.lastTitle[a])
            print("\n")
        except Exception as e:
            print(e)
        finally:
            dosometing = 0
            # 여기서 디비에 저장?

        return

    def getAllTitle(self, category: str) -> int:
        # 초기값일때는 가장 최근 기사를 받아옴
        if self.lastTitle[category] == "":
            return 1

        # 리스트가 총 12개
        for i in range(12):
            title = self.driver.find_element_by_xpath(
                f"//*[@id='content']/div[3]/div[1]/div/div/ul/li[{i+1}]/div/a[2]"
            )
            # 마지막 기사와 제목이 같은것을 찾고
            # 그 기사가 최근기사부터 몇번째 뒤에있는지 리턴
            if title.text == self.lastTitle[category]:
                return i

        # 제목이 같은걸 못찾았을때 기사를 하나하나 비교해봄
        # 제목이 바꼈을 경우가 있음.
        photoDes = []
        for i in range(12):
            self.driver.find_element_by_xpath(
                f"//*[@id='content']/div[3]/div[1]/div/div/ul/li[{i+i}]/div/a[2]"
            ).click()

            try:
                title: str = self.driver.find_element_by_xpath(
                    "//*[@id='container']/div[2]/h1"
                ).text
            except:
                title = ""

            # 기사 내용
            try:
                articleText = self.driver.find_element_by_xpath(
                    "//*[@id='content']/div/div[1]"
                ).text
            except:
                articleText = ""

            # 사진이 있을때
            try:
                articlePhoto = self.driver.find_elements_by_class_name("articlePhotoC")
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

            if (
                title == self.lastTitle[category]
                or articleText == self.lastArticle[category]
            ):
                return i

        # 마지막 기사를 못찾았으면 -1 리턴
        return -1

    def getMainSite(self, category: str) -> None:
        # 메인사이트
        self.driver.get(self.catecoryDir[category])
        return

    def getSite(self, category: str, newArticle: int) -> None:
        self.driver.get(self.catecoryDir[category])
        # 각 기사들 클릭
        self.driver.find_element_by_xpath(
            f"//*[@id='content']/div[3]/div[1]/div/div/ul/li[{newArticle}]/div/a[2]"
        ).click()
        return
