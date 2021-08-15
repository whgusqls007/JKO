from Busan import Busan
from Herald import Herald
from Nocut import Nocut
from Ohmynews import Ohmynews
from Wiki import Wiki
from Donga import Donga
from Hangook import Hangook
from Joseon import Joseon
from Yeonhap import Yeonhap
from Joongang import Joongang

from pymongo import MongoClient
import random

import os
import json

with open("Crawling/secret.json", "r") as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

class Crawling:
    def __init__(self):
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
        self.db = self.connectDB()
        self.col = None
        self.articles = []

    def connectDB(self):
        client = MongoClient(get_secret("DBURI"))
        db = client["Donga"]
        return db

    def start(self):
        subClass = None
        while True:
            for col in self.colList:
                self.articles.clear()

                if col == "api_busan":
                    subClass = Busan()
                    print("부산")
                elif col == "api_herald":
                    subClass = Herald()
                    print("헤럴드")
                elif col == "api_nocut":
                    subClass = Nocut()
                    print("노컷")
                elif col == "api_ohmynews":
                    subClass = Ohmynews()
                    print("오마이")
                elif col == "api_wikitree":
                    subClass = Wiki()
                    print("위키")
                elif col == "api_donga":
                    subClass = Donga()
                    print("동아")
                elif col == "api_hangook":
                    subClass = Hangook()
                    print("한국")
                elif col == "api_joseon":
                    subClass = Joseon()
                    print("조선")
                elif col == "api_yeonhap":
                    subClass = Yeonhap()
                    print("연합")
                elif col == "api_joongang":
                    subClass = Joongang()
                    print("중앙")

                self.articles = subClass.crawling()
                subClass.quit()

                self.col = self.db[col]
                self.insertDB()

    def insertDB(self):
        for article in self.articles:
            result1 = self.col.find_one({"title": article["title"]})
            result2 = self.col.find_one({"mainText": article["mainText"]})
            if result1 == None and result2 == None:
                while True:
                    id = random.randint(1, 999999999999)
                    result3 = self.col.find_one({"_id": id})
                    if result3 == None:
                        article["_id"] = id
                        self.col.insert_one(article)
                        break
            elif result1 == None and result2 != None:
                self.col.update_one(
                    {"mainText": article["mainText"]},
                    {"$set": {"title": article["title"]}},
                )
            elif result1 != None and result2 == None:
                self.col.update_one(
                    {"title": article["title"]},
                    {"$set": {"mainText": article["mainText"]}},
                )
            elif result1 != None and result2 != None:
                continue

    def deleteAll(self):
        for i in range(8):
            self.col = self.db[self.colList[i]]
            self.col.delete_many({})


a = Crawling()
a.start()
# a.deleteAll()
