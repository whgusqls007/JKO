from selenium import webdriver

# https://pypi.org/project/webdriver-manager/
from webdriver_manager.firefox import GeckoDriverManager as Firefox
from webdriver_manager.chrome import ChromeDriverManager as Chrome
from webdriver_manager.microsoft import EdgeChromiumDriverManager as Edge


class CrawlingDriver:
    def __init__(self) -> None:
        # 어떤 브라우저를 쓸지 정해야함
        # Chrome
        # self.driver = webdriver.Chrome(Chrome().install())
        # Edge
        self.driver = webdriver.Edge(Edge().install())
        # Firefox
        # self.driver = webdriver.Firefox(Firefox().install())
        # 기다리는 시간 설정
        self.driver.implicitly_wait(20)

        # 자바 스크립트 끄기
        # 꺼도 HTML 읽어 오는덴 상관 없음
        self.driver.get("edge://settings/content/javascript")
        self.driver.find_element_by_xpath("//*[@id='permission-toggle-row']").click()

        # 하위 드라이버들의 카테고리 묶음
        self.category: list = ["politics", "economy", "inter", "society", "sports"]
