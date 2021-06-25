from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QGridLayout,
    QLineEdit,
    QFileDialog,
    QCalendarWidget,
    QDateEdit,
)
from PyQt5.QtCore import QDate
import time
from datetime import datetime
import sys
from urllib import parse as uparse
import threading

# class QtGUI(QWidget):


class QtGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.ID = "12701600"
        self.PW = "ggat3766!!"
        self.driverdir = "C:/chromedriver.exe"
        # self.driverdir = "C:/msedgedriver.exe"
        self.login_url = "https://www.nobelcc.co.kr/html/member/login.asp"
        self.main_url = "https://www.nobelcc.co.kr/index.asp"
        self.reserve_url = (
            "https://www.nobelcc.co.kr/html/reservation/reservation_01_01_01.asp"
        )
        self.year = None
        self.month = None
        self.date = None
        self.day = None
        self.course = None
        self.course_num = None
        self.reserve_time = None

        self.setWindowTitle("골프 예약 매크로")

        # 레이아웃
        self.resize(400, 300)
        self.Lgrid = QGridLayout()
        self.Lgrid.setRowStretch(0 | 1 | 2 | 3 | 4, 25)
        self.setLayout(self.Lgrid)

        # 라벨
        self.Label_ymd = QLabel("날짜 선택", self)
        self.Label_course = QLabel("코스 선택", self)
        self.Label_time = QLabel("시간 선택", self)

        # 콤보박스
        self.QCB = QComboBox(self)
        self.QCB.addItem("")
        self.QCB.addItem("공룡")
        self.QCB.addItem("가야")
        self.QCB.addItem("충무")
        self.QCB.activated[str].connect(self.getCourse)
        self.QCB2 = QComboBox(self)
        self.QCB2.addItem("")
        self.QCB2.addItem("06")
        self.QCB2.addItem("07")
        self.QCB2.addItem("08")
        self.QCB2.addItem("09")
        self.QCB2.addItem("10")
        self.QCB2.addItem("11")
        self.QCB2.addItem("12")
        self.QCB2.addItem("13")
        self.QCB2.addItem("14")
        self.QCB2.addItem("15")
        self.QCB2.addItem("16")
        self.QCB2.addItem("17")
        self.QCB2.addItem("18")
        self.QCB2.activated[str].connect(self.getTime)

        # 버튼
        self.startbutton = QPushButton(self)
        self.startbutton.setText("시작")
        self.startbutton.clicked.connect(self.start)

        # 날짜선택
        self.cal = QDateEdit(self)
        self.cal.setCalendarPopup(True)
        self.cal.setDate(QDate.currentDate())
        self.cal.dateChanged.connect(lambda: self.getDate(self.cal))

        # 원소 배치
        self.Lgrid.addWidget(self.Label_ymd, 0, 0)
        self.Lgrid.addWidget(self.cal, 0, 1)
        self.Lgrid.addWidget(self.Label_course, 1, 0)
        self.Lgrid.addWidget(self.QCB, 1, 1)
        self.Lgrid.addWidget(self.Label_time, 2, 0)
        self.Lgrid.addWidget(self.QCB2, 2, 1)
        self.Lgrid.addWidget(self.startbutton, 100, 1)

        self.show()

    def getTime(self, text):
        self.reserve_time = text
        print(self.reserve_time)

    def getCourse(self, text):
        if text == "가야":
            self.course = "%EA%B0%80%EC%95%BC"
            self.course_num = "1"
        elif text == "충무":
            self.course = "%EC%B6%A9%EB%AC%B4"
            self.course_num = "2"
        else:
            self.course = "%EA%B3%B5%EB%A3%A1"
            self.course_num = "3"

    def getDate(self, cal):
        d = cal.date()
        self.year = str(d.year())
        if d.month() < 10:
            self.month = "0" + str(d.month())
        else:
            self.month = str(d.month())
        if d.day() < 10:
            self.date = "0" + str(d.day())
        else:
            self.date = str(d.day())
        if d.dayOfWeek() == 1:
            self.day = "%EC%9B%94"  # 월
        elif d.dayOfWeek() == 2:
            self.day = "%ED%99%94"  # 화
        elif d.dayOfWeek() == 3:
            self.day = "%EC%88%98"  # 수
        elif d.dayOfWeek() == 4:
            self.day = "%EB%AA%A9"  # 목
        elif d.dayOfWeek() == 5:
            self.day = "%EA%B8%88"  # 금
        elif d.dayOfWeek() == 6:
            self.day = "%ED%86%A0"  # 토
        else:
            self.day = "%EC%9D%BC"  # 일

    def start(self):
        self.driver = webdriver.Chrome(self.driverdir)
        # self.driver = webdriver.Edge(self.driverdir)
        self.driver.implicitly_wait(10)
        self.driver.get(self.login_url)
        self.driver.find_element_by_id("loginId").send_keys(self.ID)
        self.driver.find_element_by_id("loginPw").send_keys(self.PW)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/" +
            "div[3]/div/div/form/fieldset/button"
        ).click()

        if (
            self.day == "%EC%9B%94"
            or self.day == "%ED%99%94"
            or self.day == "%EC%88%98"
            or self.day == "%EB%AA%A9"
            or self.day == "%EA%B8%88"
        ):
            while True:
                now = datetime.now()
                if now.hour == 0 and now.minute == 0 and now.second == 0:
                    break
            self.driver.get(self.reserve_url)
            select_date = self.driver.find_elements_by_tag_name("a")
            for element in select_date:
                html = element.get_attribute("href")
                if html == None:
                    continue
                if (
                    html
                    == "javascript:Date_Click('"
                    + self.year
                    + "','"
                    + self.month
                    + "','"
                    + self.date
                    + "');"
                ):
                    element.click()
                    break

            select_T = self.driver.find_elements_by_tag_name("a")

            for element in select_T:
                html = str(element.get_attribute("href"))
                if (
                    "javascript:Book_Confirm('"
                    + self.year
                    + self.month
                    + self.date
                    + "','"
                    + self.day
                    + "','"
                    + self.course_num
                    + "', '"
                    + self.course
                    + "','"
                    + self.reserve_time
                    in html
                ):
                    element.click()
                    break

            self.driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div[3]/div[2]/a[2]"
            ).click()
            self.driver.switch_to_alert().accept()

        else:
            while True:
                now = datetime.now()
                print(now.microsecond)
                if now.hour == 14 and now.minute == 0 and now.second == 0:
                    break
            self.driver.get(self.reserve_url)
            select_date = self.driver.find_elements_by_tag_name("a")
            for element in select_date:
                html = element.get_attribute("href")
                if html == None:
                    continue
                if (
                    html
                    == "javascript:Date_Click('"
                    + self.year
                    + "','"
                    + self.month
                    + "','"
                    + self.date
                    + "');"
                ):
                    element.click()
                    break

            select_T = self.driver.find_elements_by_tag_name("a")

            for element in select_T:
                html = str(element.get_attribute("href"))
                if (
                    "javascript:Book_Confirm('"
                    + self.year
                    + self.month
                    + self.date
                    + "','"
                    + self.day
                    + "','"
                    + self.course_num
                    + "', '"
                    + self.course
                    + "','"
                    + self.reserve_time
                    in html
                ):
                    element.click()
                    break

            self.driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div[3]/div[2]/a[2]"
            ).click()
            self.driver.switch_to_alert().accept()


app = QApplication(sys.argv)
ex = QtGUI()
app.exec_()
