from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.request # 이미를 받기위한 라이브러리

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

URL = 'https://www.zara.com/kr/ko/%ED%8E%98%EC%9D%B4%ED%81%AC-%EB%A0%88%EB%8D%94-%ED%8C%A8%EB%94%A9-%EC%A0%90%ED%8D%BC-p03427804.html'
driver.get(url=URL)
driver.implicitly_wait(5)
time.sleep(3)

name = driver.find_element(By.CLASS_NAME,'product-detail-info__header-name')
print('name=', name.text)
 