from NLP import NLP
import difflib
import copy
import random


class MakeArticle(NLP):
    def __init__(self):
        NLP.__init__(self)
        self.differ = difflib.Differ()

    def makeNewArticle(self):
        clusteredArticles = self.startClustering()
        col = self.db["api_clustering"]
        for articles in clusteredArticles:
            newArticleTitle = ""
            newArticleMainText = ""
            for i in range(len(articles) - 1):
                titleDifferences = (
                    self.differ.compare(articles[i]["title"], articles[i + 1]["title"])
                    if i == 0
                    else self.differ.compare(newArticleTitle, articles[i + 1]["title"])
                )
                mainTextDifferences = (
                    self.differ.compare(
                        articles[i]["mainText"], articles[i + 1]["mainText"]
                    )
                    if i == 0
                    else self.differ.compare(
                        newArticleMainText, articles[i + 1]["mainText"]
                    )
                )
                newArticleTitle = ""
                newArticleMainText = ""
                for diff in titleDifferences:
                    if diff[0] == "+" or diff[0] == " ":
                        newArticleTitle += diff[2]

                for diff in mainTextDifferences:
                    if diff[0] == "+" or diff[0] == " ":
                        newArticleMainText += diff[2]

            keyList = []
            for article in articles:
                keyList.append(article["_id"])

            fastestDate = "0"
            select_category = {
                "politics": 0,
                "economy": 0,
                "society": 0,
                "sport": 0
            }
            for article in articles:
                if article["date"] > fastestDate:
                    fastestDate = article["date"]
                select_category[article["category"]] += 1
            
            mincnt = 0
            category = ""
            for categories in select_category:
                if select_category[categories] > mincnt:
                    mincnt = select_category[categories]
                    category = categories

            isExist = None

            for key in keyList:
                isExist = col.find_one({"keys": key})
                if isExist:
                    break

            if isExist:
                tempList = copy.deepcopy(keyList)
                id = isExist["_id"]
                for key1 in isExist["keys"]:
                    for key2 in tempList:
                        if key1 == key2:
                            keyList.remove(key2)
                if len(keyList) != 0:
                    col.update_one(
                        {"_id": id},
                        {
                            "$set": {
                                "title": newArticleTitle,
                                "mainText": newArticleMainText,
                                "keys": tempList,
                                "articles": articles,
                                "date": fastestDate,
                                "category" : category
                            }
                        },
                    )
            else:
                id = random.randint(1, 9223372036854775807)
                flag = None
                flag = col.find_one({"_id": id})

                if flag:
                    while True:
                        id = random.randint(1, 9223372036854775807)
                        flag = col.find_one({"_id": id})
                        if not flag:
                            col.insert_one(
                                {
                                    "_id": id,
                                    "title": newArticleTitle,
                                    "mainText": newArticleMainText,
                                    "keys": keyList,
                                    "articles": articles,
                                    "date": fastestDate,
                                    "category" : category
                                }
                            )
                            break
                else:
                    col.insert_one(
                        {
                            "_id": id,
                            "title": newArticleTitle,
                            "mainText": newArticleMainText,
                            "keys": keyList,
                            "articles": articles,
                            "date": fastestDate,
                            "category" : category
                        }
                    )


aaa = MakeArticle()
while True:
    aaa.makeNewArticle()
