from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'../chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)


def main():
    url = 'https://plato.pusan.ac.kr/'
    driver.get(url)

    username_string = '201924628'
    username_input = driver.find_element(by=By.XPATH, value='//*[@id="input-username"]')
    username_input.click()
    username_input.send_keys(username_string)

    password_string = 'zhlX682075+*+'
    password_input = driver.find_element(by=By.XPATH, value='//*[@id="input-password"]')
    password_input.click()
    password_input.send_keys(password_string)

    login_button = driver.find_element(by=By.XPATH, value='//*[@id="page-header"]/div[1]/div/div[2]/form/div/input[3]')
    login_button.click()

    cookies = driver.get_cookies()
    print(cookies)


if __name__ == "__main__":
    main()
