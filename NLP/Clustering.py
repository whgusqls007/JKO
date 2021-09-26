from sklearn.feature_extraction.text import CountVectorizer as CV, _preprocess
from pymongo import MongoClient as MC
from konlpy.tag import Okt
import scipy as sp
import random
import copy
import json


with open("/home/whgusqls007/JKO/Crawling/secret.json", "r") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    return secrets[setting]


class NLP:
    def __init__(self):
        self.db = self.connectDB()
        self.colList = [
            "api_busan",
            "api_herald",
            "api_nocut",
            "api_ohmynews",
            "api_wikitree",
            "api_donga",
            "api_hangook",
            "api_joseon",
            "api_yeonhap",
            "api_joongang",
        ]
        self.Threshold = 1.7
        self.data = []
        self.newData = []
        self.okt = Okt()
        self.vectorizer = CV(min_df=1)
        self.contents_all = []

    def connectDB(self):
        db = MC(get_secret("DBURI"))["Donga"]
        return db

    def dist_raw(self, v1, v2):
        delta = v1 - v2
        return sp.linalg.norm(delta.toarray())

    def getDataFromDB(self, collection):
        col = self.db[collection]
        posts = col.find({}).sort("date", -1).limit(60)
        contents_title = []
        contents_all = []

        for post in posts:
            dic = {
                "_id": post["_id"],
                "title": post["title"],
                "mainText": post["mainText"],
                "category": post["category"],
                "url": post["url"],
                "reporter": post["reporter"],
                "date": post["date"],
                "press": post["press"],
                "img": post["img"],
                "emotion": post["emotion"],
            }
            contents_all.append(dic)
            print(dic)
            print("\n\n")
            contents_title.append(post["title"])
            if not dic in self.contents_all:
                self.contents_all.append(dic)

        return contents_all, contents_title

    def getToken(self, contents, flag=True):
        if flag:
            return [self.okt.morphs(content) for content in contents]
        else:
            return [self.okt.morphs(contents)]

    def vectorize(self, tokens):
        contents_for_vectorize = []

        for token in tokens:
            sentence = ""
            for word in token:
                sentence = sentence + " " + word
            contents_for_vectorize.append(sentence)

        return contents_for_vectorize

    def getDistance(self):
        self.data = []
        for i in range(len(self.colList)):
            for j in range(i + 1, len(self.colList)):
                print(self.colList[i])
                contents_all, contents_title = self.getDataFromDB(self.colList[i])

                if contents_all == []:
                    continue

                contents_token = self.getToken(contents_title)
                contents_for_vectorize = self.vectorize(contents_token)
                X = self.vectorizer.fit_transform(contents_for_vectorize)
                num_samples, num_feature = X.shape
                X.toarray().transpose()

                newContents_all, newContents_title = self.getDataFromDB(self.colList[j])
                for k in range(len(newContents_title)):
                    newContents_token = self.getToken(newContents_title[k], flag=False)
                    newContents_for_vectorize = self.vectorize(newContents_token)
                    Y = self.vectorizer.transform(newContents_for_vectorize)
                    Y.toarray()

                    for l in range(num_samples):
                        d = self.dist_raw(X.getrow(l), Y)
                        if d < self.Threshold:
                            self.data.append([contents_all[l], newContents_all[k]])
                            print(contents_all[l])
                            print(newContents_all[k])
                            print("\n\n")

    def clustring(self):
        self.newData.clear()
        for i in range(len(self.data)):
            flag1 = False
            for j in range(i + 1, len(self.data)):
                flag2 = False
                for k in range(len(self.data[i])):
                    for l in range(len(self.data[j])):
                        if self.data[i][k] == self.data[j][l]:
                            flag2 = True
                            break
                    if flag2:
                        break

                if flag2:
                    flag1 = True
                    tempData = []
                    for data in self.data[i]:
                        tempData.append(data)
                    for data in self.data[j]:
                        if not data in tempData:
                            tempData.append(data)

                    index = -1
                    for k in range(len(self.newData)):
                        for data in tempData:
                            if data in self.newData[k]:
                                index = k
                                break
                        if index != -1:
                            break

                    if index != -1:
                        for data in tempData:
                            if not data in self.newData[index]:
                                self.newData[index].append(data)
                    else:
                        self.newData.append(tempData)

            if not flag1:
                index = -1
                for k in range(len(self.newData)):
                    for data in self.data[i]:
                        if data in self.newData[k]:
                            index = k
                            break
                    if index != -1:
                        break

                if index != -1:
                    for data in self.data[i]:
                        if not data in self.newData[index]:
                            self.newData[index].append(data)

                else:
                    self.newData.append(self.data[i])

    def insertDB(self):
        col = self.db["api_clustering"]
        print(self.contents_all)
        for newData in self.newData:
            newData = sorted(newData, key=lambda x: x["date"])
            keyList = []
            press = []
            for article in newData:
                keyList.append(article["_id"])
                press.append(article["press"])

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
                                "title": newData[0]["title"],
                                "mainText": newData[0]["mainText"],
                                "keys": tempList,
                                "articles": newData,
                                "date": newData[0]["date"],
                                "category": newData[0]["category"],
                                "reporter": newData[0]["reporter"],
                                "press": press,
                                "img": newData[0]["img"],
                                "mainPress": newData[0]["press"],
                                "emotion": newData[0]["emotion"],
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
                                    "title": newData[0]["title"],
                                    "mainText": newData[0]["mainText"],
                                    "keys": keyList,
                                    "articles": newData,
                                    "date": newData[0]["date"],
                                    "category": newData[0]["category"],
                                    "reporter": newData[0]["reporter"],
                                    "press": press,
                                    "img": newData[0]["img"],
                                    "mainPress": newData[0]["press"],
                                    "emotion": newData[0]["emotion"],
                                }
                            )
                            break
                else:
                    col.insert_one(
                        {
                            "_id": id,
                            "title": newData[0]["title"],
                            "mainText": newData[0]["mainText"],
                            "keys": keyList,
                            "articles": newData,
                            "date": newData[0]["date"],
                            "category": newData[0]["category"],
                            "reporter": newData[0]["reporter"],
                            "press": press,
                            "img": newData[0]["img"],
                            "mainPress": newData[0]["press"],
                            "emotion": newData[0]["emotion"],
                        }
                    )

        for originalData in self.contents_all:
            isClustered = False
            for newData in self.newData:
                if originalData in newData:
                    isClustered = True
                    break
            if not isClustered:
                isExist = None
                isExist = col.find_one({"_id": originalData["_id"]})
                if isExist:
                    continue
                col.insert_one(originalData)

    def startClustering(self):
        while True:
            self.contents_all.clear()
            self.getDistance()
            self.clustring()
            self.insertDB()

    def deleteAll(self):
        col = self.db["api_clustering"]
        col.delete_many({})
        return


aaa = NLP()
aaa.startClustering()
