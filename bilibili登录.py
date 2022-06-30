from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'../chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)


def main():
    url = 'https://passport.bilibili.com/login'
    driver.get(url)

    username_string = '15039502467'
    username_input = driver.find_element(by=By.XPATH, value='//*[@id="login-username"]')
    username_input.click()
    username_input.send_keys(username_string)

    password_string = 'zhlX2186369'
    password_input = driver.find_element(by=By.XPATH, value='//*[@id="login-passwd"]')
    password_input.click()
    password_input.send_keys(password_string)

    login_button = driver.find_element(by=By.XPATH, value='//*[@id="geetest-wrap"]/div/div[5]/a[1]')
    login_button.click()


if __name__ == "__main__":
    main()
