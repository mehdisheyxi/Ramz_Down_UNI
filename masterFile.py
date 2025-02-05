from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
import sys
import requests
from bs4 import BeautifulSoup
import random
import string
import re
import os
from urllib.parse import urlparse
class Login(QtWidgets.QMainWindow):
    """ کلاس برای صفحه اول """
    def __init__(self):
        super().__init__()
        loadUi('UI_ha/login.ui', self)  # فایل ui در اینجا مشخص میشود
        self.prepare_ui() # ایکون صفحه
        self.show()

    def prepare_ui(self):
        self.setWindowTitle('ramz down')
        self.setWindowIcon(QIcon('icon/arrows_16569302.png'))
        # اتصال سیگنال‌ها به اسلات‌ها برای مدیریت رویدادهای کاربر (مثلاً کلیک روی دکمه‌ها)
        self.gotodown.clicked.connect(self.opendown)
        self.actionabout.triggered.connect(self.about)
        self.gotopass.clicked.connect(self.openpass)
    def openpass(self):
        self.openpase = openpas()
        self.openpase.show()
    def opendown(self):
        self.download_window = Download()
        self.download_window.show()
    def about(self):
        self.about = About()
        self.about.show()
class openpas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi('UI_ha/passaz.ui', self)
        self.show()
        self.paperui()
        self.cdf.clicked.connect(self.createdefpas)
        self.cc.clicked.connect(self.createcoustom)
        self.chek.clicked.connect(self.chekpas)



    def paperui(self):
        self.setWindowTitle('ramz saz')
        self.setWindowIcon(QIcon('icon/padlock_3256783.png'))
    def createdefpas(self):
        a = ''
        special = string.punctuation
        digits = string.digits
        lower = string.ascii_letters.lower()
        upper = string.ascii_letters.upper()

        # اضافه کردن کاراکترهای تصادفی به رشته a
        a += ''.join(random.choices(lower, k=2))
        a += ''.join(random.choices(upper, k=2))
        a += ''.join(random.choices(digits, k=2))
        a += ''.join(random.choices(special, k=2))

        # تبدیل رشته به لیست و مخلوط کردن عناصر
        b = list(a)
        random.shuffle(b)

        # تبدیل لیست به رشته و چاپ
        self.textBrowser.setText(f'{"".join(b)}')
    def createcoustom(self):
        number = self.spinBox.value()
        a = ""
        special = string.punctuation
        digits = string.digits
        lower = string.ascii_letters.lower()
        upper = string.ascii_letters.upper()
        if number <= 4:
            a += ''.join(random.choices(lower, k=1))
            a += ''.join(random.choices(upper, k=1))
            a += ''.join(random.choices(digits, k=1))
            a += ''.join(random.choices(special, k=1))
            b = list(a)
            random.shuffle(b)
            self.textBrowser.setText(f'{"".join(b)}')
        elif number % 4 == 0:
            ls = number / 4
            ls = int(ls)
            a += ''.join(random.choices(lower, k=ls))
            a += ''.join(random.choices(upper, k=ls))
            a += ''.join(random.choices(digits, k=ls))
            a += ''.join(random.choices(special, k=ls))
            b = list(a)
            random.shuffle(b)
            self.textBrowser.setText(f'{"".join(b)}')
        else:
            ss = number * 0.25
            ls = int(ss)
            a += ''.join(random.choices(lower, k=ls))
            a += ''.join(random.choices(upper, k=ls))
            a += ''.join(random.choices(digits, k=ls))
            a += ''.join(random.choices(special, k=ls))
            b = list(a)
            random.shuffle(b)
            self.textBrowser.setText(f'{"".join(b)}')
        #self.textBrowser.setText(str(number))
    def chekpas(self):
            password = self.textEdit.toPlainText()
            """
            این تابع قدرت رمز عبور را در چهار سطح ارزیابی می‌کند.

            Args:
                password (str): رمز عبور وارد شده توسط کاربر

            Returns:
                str: سطح قدرت رمز عبور (خیلی ضعیف، ضعیف، متوسط، قوی)
            """

            # تعریف عبارات منظم برای بررسی انواع کاراکترها و الگوهای رایج
            has_upper = re.search(r'[A-Z]', password)
            has_lower = re.search(r'[a-z]', password)
            has_digit = re.search(r'\d', password)
            has_special = re.search(r'[^A-Za-z0-9]', password)
            has_sequence = re.search(r'(\w)\1{2,}', password)  # بررسی دنباله‌های تکراری
            has_common_pattern = re.search(r'(password|123456|qwerty)', password, re.IGNORECASE)  # بررسی الگوهای رایج

            # محاسبه امتیاز بر اساس معیارهای مختلف
            score = 0
            if len(password) >= 12:
                score += 2
            elif len(password) >= 8:
                score += 1
            if has_upper:
                score += 1
            if has_lower:
                score += 1
            if has_digit:
                score += 1
            if has_special:
                score += 1
            if not has_sequence:
                score += 1
            if not has_common_pattern:
                score += 1

            # تعیین سطح قدرت رمز عبور بر اساس امتیاز
            if score <= 3:
                text =  "خیلی ضعیف"
            elif score <= 5:
                text =  "ضعیف"
            elif score <= 7:
                text =  "متوسط"
            else:
                text =  "قوی"

        # مثال استفاده از تابع
            self.label_2.setText(f"{text}")
class About(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi('UI_ha/about.ui', self)
        self.prepare_ui()
        self.show()

    def prepare_ui(self):
        self.setWindowTitle('about')
        self.setWindowIcon(QIcon('icon/info_5553077.png'))
class Download(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi('UI_ha/downUI.ui', self)
        self.video_links = []
        self.prepare_ui()
        self.show()
        self.pushButton.clicked.connect(self.getURl)
        self.pushButton_2.clicked.connect(self.oneDown)

    def getURl(self):
        try:
            url = self.lineEdit.text()
            mdoe = self.comboBox.currentText()
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            video_links = []
            for link in links:
                if 'href' in link.attrs and link['href'].endswith(mdoe):
                    video_links.append(link['href'])
            self.textBrowser.setText(str(video_links))
            self.video_links = video_links

        except requests.exceptions.RequestException as e:
            self.textBrowser.setText(f'Eror is {e}')
    def oneDown(self):
        url = self.lineEdit_2.text()
        response = requests.get(url)
        n_url = urlparse(url)
        file_name = (os.path.basename(n_url.path))
        with open(file_name, 'wb') as file:
            file.write(response.content)
    def prepare_ui(self):
        self.setWindowTitle('download')
        self.setWindowIcon(QIcon('icon/download_4439518.png'))
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Login()
    window.show()
    sys.exit(app.exec_())