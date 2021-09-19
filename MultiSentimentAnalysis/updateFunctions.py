# connecting to DB
import pymongo
from pymongo import MongoClient
from predictFunctions import predictFunctions

class updateFunctions:

    def __init__(self):

        #dotenvFile로 해야함
        self.client = MongoClient('mongodb+srv://admin:admin@clustertutorial.cxa5s.mongodb.net/Donga?retryWrites=true&w=majority')
        #self.client = MongoClient('<몽고디비URL>')
        self.db = self.client['Donga']
        '''
          collection list를 사용해 인덱스만으로 반복문 돌릴 예정
        '''
        self.col_list = ['api_busan','api_donga','api_hangook',
                    'api_joongang','api_joseon','api_nocut',
                    'api_ohmynews','api_wikitree','api_yeonhap',
                    'api_herald'
                    ]
        '''
        predictFunction을 쓰기위한 생성자
        '''
        self.PF = predictFunctions()

    def update(self, news_class=None):
        '''
        몽고디비에서 타이틀을 가져온 뒤 타이틀을 모델에 넣고 emotion 이 결정되면 수정해서 넣어줌

        _id, title, emotion 을 사용

        1. emotion=""인 collection 을 모두 찾음
        2. _id,title 각각 list에 저장
        3. title을 for문을 돌면서 emotion 저장
        4. _id 와 title 인덱스 값을 사용한다.
            _id 를 find_one 함수를 사용해서 emotion field를 수정한다.
        '''
        for pressIndex, pressName in enumerate(self.col_list):

            id_list = []
            title_list = []
            emotion_list = []
            cnt = 0

            collection = self.db[pressName]  # 지금은 0 : api_busan
            for x in collection.find():
                # print(x) # 확인용

                # 카테고리 마다 모델이 다르기 때문에 필터링 && emotion 없는 것만
                if x['category'] == news_class:
                    id_list.append(x['_id'])
                    title_list.append(x['title'])
                    #cnt += 1

            #print(cnt)  # 확인용
            print( pressName + "의"+ news_class + "면 " + "시작합니다.")
            for i, title in enumerate(title_list):
                print("(", i, ",", title, ",", self.PF.predict(title, news_class=news_class), ")")  # 확인용

                # 모델에 적용시킴
                emotion_list.append(self.PF.predict(title, news_class= news_class))

                # 이제 몽고디비 넣자.
                collection.update_one({'_id': id_list[i]}, {'$set': {'emotion': emotion_list[i]}})


            #print(emotion_list)  # 확인용