import json

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import requests


def make_driver():
    service = Service(r'../chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    return driver


def get_cookies_dictionary(_driver):
    time.sleep(3)
    return _driver.get_cookies()


def save_cookies_to_json_file(cookies_dictionary):
    json_cookies = json.dumps(cookies_dictionary)
    with open('cookies.txt', 'w') as f:
        f.write(json_cookies)


def read_cookies():
    cookies_file_path = r'cookies.txt'
    cookies_file = open(cookies_file_path, 'r')
    return json.loads(cookies_file.read())


def add_cookies(_driver, cookies_list):
    for cookie in cookies_list:
        _driver.add_cookie(cookie)


def find_elements_by_xpath(_driver, xpath):
    return _driver.find_elements(by=By.XPATH, value=xpath)


def find_element_by_xpath(parent, xpath):
    return parent.find_element(by=By.XPATH, value=xpath)


def main():
    """ 第一次 手动登录获取cookies """
    # driver = make_driver()
    # url = "https://www.bilibili.com"
    # driver.get(url)
    #
    # time.sleep(10)
    #
    # save_cookies_to_json_file(get_cookies_dictionary(driver=driver))
    # driver.quit()
    # print('cookies is ok')

    """ 自动登录 """
    main_url = 'https://www.bilibili.com'
    driver.get(main_url)

    add_cookies(driver, read_cookies())
    driver.refresh()
    print('登录成功!')
    driver.implicitly_wait(2)

    """ 打开我的追番标签页 """
    drama_url = 'https://space.bilibili.com/44629592/bangumi'
    js = 'window.open("' + drama_url + '")'
    driver.execute_script(js)

    """ 获取所有标签页 """
    window_handles = driver.window_handles

    """ 获取当前标签页 """
    """ 
        current_url : 默认为第一个标签页
        并不随新标签页打开， 即使前台程序已经切换，后台数据依然是默认第一个标签页
    """
    current_handle = driver.current_url
    # print(current_handle)

    """ 切换标签页 """
    driver.switch_to.window(window_handles[-1])
    # print(driver.current_url)

    """  """
    # print(driver.page_source)
    # //*[@id="page-bangumi"]/div/div[2]/div/div/ul

    """ 番剧标题爬取 """
    with open("我的追番.txt", 'w', encoding='utf-8') as drama_file:
        count = 1
        print("正在爬取...")
        while True:
            time.sleep(1)
            try:
                page_option = find_element_by_xpath(driver, '//*[@id="page-bangumi"]/div/div[2]/div/div/div')
                page_options = find_elements_by_xpath(page_option, 'a')
                next_page = page_options[-1]
            except StaleElementReferenceException:
                print("element is not attached to the page document")
                break
            dramas_ul = find_element_by_xpath(driver, '//*[@id="page-bangumi"]/div/div[2]/div/div/ul')
            lis = find_elements_by_xpath(dramas_ul, 'li')
            for i, li in zip(range(0, len(lis)), lis):
                try:
                    _as = find_elements_by_xpath(li, 'a')
                    title = find_element_by_xpath(_as[1], 'h4')
                except IndexError:
                    # print('index out of list')
                    break
                # print(title.text)
                """ 写入文件 """
                index = ""
                if count + i < 10:
                    index = '0' + str(count + i)
                else:
                    index = str(count + i)
                drama_file.write(index + '. ' + title.text + '\n')
            count += len(lis)
            # print(next_page.text)
            if next_page.text != "下一页":
                # print('已到达最后一页')
                break
            else:
                next_page.click()
    print('爬取完毕，写入文件成功!')


if __name__ == "__main__":
    driver = make_driver()
    main()

