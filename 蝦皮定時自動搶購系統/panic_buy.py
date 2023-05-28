from logging import error
import tkinter as tk  # 使用Tkinter前需要先匯入
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import keyboard
import configparser
from urllib.parse import unquote

config = configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')

# 監控時間下訂單
def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        # 對比時間，時間到的話就點選結算
        if now > times:
            break
    print(browser.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'))
    # 點選結算按鈕
    while True:
        browser.refresh()
        time.sleep(2)
        try:
            if browser.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'):
                browser.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]').click()
                print(f"結算成功，準備提交訂單")
                break
        except Exception:
            continue
    # WebDriverWait(browser, 900).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn btn-solid-primary btn--l iFo-rx']"))).click()


    while True:
        time.sleep(0.3)
        try:
            while True:
                if browser.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div/div[3]/div[2]/div[6]/button[2]'):
                    browser.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div/div[3]/div[2]/div[6]/button[2]').click()
                    print(f"提交成功，準備下訂單")
                    # 繼續下訂單
        except Exception:
            continue

    # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='shopee-button-solid shopee-button-solid--primary']"))).click()

# 登入
# def login():
#     time.sleep(100)
#     if browser.find_element(By.LINK_TEXT, "登入"):
#         browser.find_element(By.LINK_TEXT, "登入").click()
#         time.sleep(2)
#         search_Id = browser.find_element_by_name('loginKey')
#         search_Id.send_keys(config['user']['username'])  # 輸入帳號
#         search_password = browser.find_element_by_name('password')
#         search_password.send_keys(config['user']['password'])  # 輸入密碼
#         time.sleep(0.3)
#         search_password.send_keys(Keys.CONTROL, '\ue007')
#         print("程式暫停中...")
#         print("登入完成後，按 k 鍵繼續")

#         while True:
#             if keyboard.read_key() == "k":
#                 print("開始買")
#                 break
#         buy("2021-01-01 12:00:00")  # 執行下訂單程式


# 主程式
# 開啟Chrome瀏覽器
# 到C:\Program Files\Google\Chrome\Application下指令
# chrome.exe --remote-debugging-port=9453 --user-data-dir="C:\Users\Anonymous\Desktop\PanicBuy-shopee-\蝦皮定時自動搶購系統"
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9453") #這樣你就能控制已經登入的蝦皮
# browser = webdriver.Chrome()
browser = webdriver.Chrome(options=options)
# 開啟蝦皮商品頁
browser.get(config['commodity']['url'])
time.sleep(3)
# login()
buy("2021-01-01 12:00:00")
