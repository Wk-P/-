from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r'../chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)


def main():
    url = 'https://www.bilibili.com'
    driver.get(url)
    time.sleep(20000)


if __name__ == "__main__":
    main()