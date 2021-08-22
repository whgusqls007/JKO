from newspaper import Article, article
from selenium import webdriver

class Busan():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("disable-gpu")
        self.options.add_argument("headless")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        )
        self.options.add_argument("window-size=1920x1080")
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(
            executable_path="/home/whgusqls007/JKO/Crawling/chromedriver",
            options=self.options,
        )
        self.driver.set_page_load_timeout(1800)
        self.url = {
            "politics": "http://www.busan.com/politics/all/",
            "economy": "http://www.busan.com/economy/all/",
            "society": "http://www.busan.com/society/all/",
            "sport": "http://www.busan.com/sport/all/",
        }
        self.pressName = "부산일보"
    
    def getSite(self, url):
        self.driver.get(url)
        return
    
    def getElement(self, Xpath):
        return self.driver.find_element_by_xpath(Xpath)
    
    def quit(self):
        self.driver.quit()
        return

    def run(self):
        for category in self.url:
            for i in range(1, 11):
                
                self.getSite(self.url[category])

                # 뉴스 날짜 얻기
                date = self.getElement(f'//*[@id="article_list"]/li[{i}]/p[3]').text
                date = date.replace("[", "").replace("]", "")
                
                # 해당 뉴스 클릭
                self.getElement(f'//*[@id="article_list"]/li[{i}]/p[1]/a').click()
                
                # 뉴스의 URL
                currentUrl = self.driver.current_url
                
                # 뉴스의 제목과 본문 얻기
                article = Article(currentUrl, language='ko')
                article.download()
                article.parse()
                
                # 기자 얻기
                reporter = self.getElement('//*[@id="container"]/div[1]/div[1]/div[3]/div[1]/div[1]').text
                
                
                # print(article.title)
                # print()
                # print(article.text)
                # print("------------------------\n")
    

a = Busan()
a.run()