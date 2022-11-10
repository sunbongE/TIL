from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.request # 이미를 받기위한 라이브러리
import json
from collections import OrderedDict
file_path = './test.json'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

URL = "https://www.zara.com/kr/ko/search"
driver.get(url=URL)
driver.implicitly_wait(5)

# 검색창의 아이디를 선택
elem = driver.find_element(By.ID, 'search-products-form-combo-input')
# 원하는 값 입력

elem.send_keys("자켓")
elem.send_keys(Keys.RETURN)
time.sleep(3)

result = {
    'results':[]
}


url_ = driver.find_elements(By.CLASS_NAME,'product-link')
cnt=0
lst = []
for u in url_:
    if cnt % 2 == 0:
        lst.append(u.get_attribute("href"))
        # print(u.get_attribute("href"))
    cnt += 1
# print(lst)
for l in lst[:10]:
    temp = {
        'images':[] ,
        'name': 0,
        'content': 0,
        'price': 0,
        'size':[],
    }
    URL = l
    driver.get(url=URL)
    driver.implicitly_wait(5)

    images = driver.find_elements(
        By.CLASS_NAME,
        "media-image",
    )
    # 이미지 링크 받아옴
    for img in images:
        img = img.find_element(By.TAG_NAME, "source")
        img_list = img.get_attribute("srcset").split()
        temp['images'].append(img_list[-2])
    
    # 상품 이름
    name = driver.find_element(
    By.CLASS_NAME,
    "product-detail-info__header-name",
    )
    temp['name'] = name.text

    # 상품 설명
    try:
        content = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/main/article/div/div[1]/div[2]/div[1]/div[2]/div/div/div/p",
        )
        temp['content'] = content.text
    except: pass

    # 가격
    price = driver.find_element(
        By.CLASS_NAME,
        "money-amount__main",
    )
    temp['price'] = price.text

    # 사이즈 정보
    sizes = driver.find_elements(
        By.CLASS_NAME,
        "product-size-info__main-label",
    )
    for size in sizes:
        temp['size'].append(f"size: {size.text}")

    result['results'].append(temp)

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)