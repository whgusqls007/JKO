from CrawlingDriver import CrawlingDriver
from Queue import Queue as Q
import selenium


class Donga(CrawlingDriver):
    def __init__(self) -> None:
        CrawlingDriver.__init__(self)
        self._listSize: int = 8
        self._catecoryDir: dict = {
            "politics": "https://www.donga.com/news/Politics",
            "economy": "https://www.donga.com/news/Economy",
            "inter": "https://www.donga.com/news/Inter",
            "society": "https://www.donga.com/news/Society",
            "sports": "https://www.donga.com/news/Sports",
        }
        self._articleList: dict = {
            "politics": Q(8),
            "economy": Q(8),
            "inter": Q(8),
            "society": Q(8),
            "sports": Q(8),
        }

    def run(self) -> dict:
        updated: bool = False
        for category in self._category:
            for index in range(self._listSize):
                self.getSite(URI=self._catecoryDir[category])

                self.findElement(
                    xpath=f"//*[@id='content']/div[3]/div[1]/div/div/ul/li[{index + 1}]/div/a[2]"
                ).click()

                title: str = self.getTitle(xpath="//*[@id='container']/div[2]/h1")
                title.strip()

                mainText: str = self.getMainText(xpath="//*[@id='content']/div/div[1]")
                mainText.strip()

                article: dict = self.makeArticleDict(title, mainText, category)

                exist: dict = self.isExist(category, article)

                if exist["find"] == 1:
                    continue
                elif exist["find"] == 2 or exist["find"] == 3:
                    self.updateArticle(article, exist["index"], category)
                    updated = True
                else:
                    self._articleList[category].push_back(article)
                    updated = True

        return (self._articleList, updated)

    def updateArticle(self, article: dict, index: int, category: str) -> None:
        self._articleList[category].update(index, article)
        return

    def isExist(self, category, article) -> dict:
        return self._articleList[category].isExist(article)

    def makeArticleDict(self, title: str, mainText: str, category: str) -> dict:
        return {
            "title": title,
            "mainText": mainText,
            "category": category,
        }

    def getMainText(self, xpath) -> str:
        photoDes = []
        try:
            mainText = self.findElement(xpath=xpath).text
        except:
            mainText = ""

        try:
            articlePhotoC = self.findElement(name="articlePhotoC", many=True)
            for i in articlePhotoC:
                photoDes.append(i.text)
            for des in photoDes:
                mainText = mainText.replace(des, "")
        except:
            articlePhotoC = []

        try:
            relationArticle = self.findElement(name="article_relation").text
            mainText = mainText.replace(relationArticle, "")
        except:
            relationArticle = ""

        try:
            href = self.findElement(name="btn_page", many=True)
            for i in href:
                mainText = mainText.replace(i.text, "")
        except:
            href = None

        return mainText

    def getTitle(self, xpath) -> str:
        return self.findElement(xpath).text

    def findElement(
        self, xpath: str = "", name: str = "", many: bool = False
    ) -> selenium:
        if not xpath == "":
            if not many:
                return self._driver.find_element_by_xpath(xpath)
            else:
                return self._driver.find_elements_by_xpath(xpath)
        else:
            if not many:
                return self._driver.find_element_by_class_name(name)
            else:
                return self._driver.find_elements_by_class_name(name)

    def getSite(self, URI: str) -> None:
        self._driver.get(URI)
        return
