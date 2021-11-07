from logging import error
import tkinter as tk  # 使用Tkinter前需要先匯入
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime
import keyboard


# 監控時間下訂單


def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        # 對比時間，時間到的話就點選結算
        if now > times:
            break

    # 點選結算按鈕
    while True:
        browser.refresh()
        time.sleep(1)
        try:
            if browser.find_element_by_xpath('//*[@id = "main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'):
                browser.find_element_by_xpath(
                    '//*[@id = "main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]').click()
                print(f"結算成功，準備提交訂單")
                break
        except Exception:
            continue

    while True:
        time.sleep(0.3)
        try:
            while True:
                if browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[2]'):
                    browser.find_element_by_xpath(
                        '//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[2]').click()
                    print(f"提交成功，準備下訂單")
                    # 繼續下訂單
        except Exception:
            continue

# 登入


def login():
    if browser.find_element_by_link_text("登入"):
        browser.find_element_by_link_text("登入").click()
        time.sleep(2)
        search_Id = browser.find_element_by_name('loginKey')
        search_Id.send_keys('你的帳號')  # 輸入帳號
        search_password = browser.find_element_by_name('password')
        search_password.send_keys('你的密碼')  # 輸入密碼
        time.sleep(0.3)
        search_password.send_keys(Keys.CONTROL, '\ue007')
        print("程式暫停中...")
        print("登入完成後，按 k 鍵繼續")

        while True:
            if keyboard.read_key() == "k":
                print("開始買")
                break
        buy("2021-01-01 12:00:00")  # 執行下訂單程式


# 主程式
# 開啟Chrome瀏覽器
# browser = webdriver.Chrome()
browser = webdriver.Chrome('chromedriver.exe', options=Options())
# 開啟蝦皮商品頁
browser.get("https://shopee.tw/商品頁")
time.sleep(2)
login()
