from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
service = Service(r'../chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)
chains = ActionChains(driver)


def main():
    if driver.get("https://www.bilibili.com/") is None:
        print('Connect Successfully!\n')

    # print(driver.page_source)
    driver.set_page_load_timeout(3)
    # Login
    # //*[@id="i_cecream"]/div/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div
    # /html/body/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="i_cecream"]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div')
    login_button.click()

    driver.implicitly_wait(2)

    username_string = "15039502467"
    # username
    # /html/body/div[3]/div/div[2]/div[3]/div[2]/div[1]/input
    input_username = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div[3]/div[2]/div[1]/input')
    input_username.click()
    input_username.send_keys(username_string)

    password_string = 'zhlX2186369'
    # password
    # /html/body/div[3]/div/div[2]/div[3]/div[2]/div[2]/div[1]/input
    input_password = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div[3]/div[2]/div[2]/div[1]/input')
    input_password.click()
    input_password.send_keys(password_string)

    # user_login_button_click
    # /html/body/div[3]/div/div[2]/div[3]/div[3]/div[2]
    user_login_button = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div[3]/div[3]/div[2]')
    user_login_button.click()


    '''
    Test case
    
    # //*[@id="nav-searchform"]/div[1]/input
    input_text = driver.find_element(by=By.XPATH, value='//*[@id="nav-searchform"]/div[1]/input')
    input_text.click()
    input_text.send_keys("俺妹")
    # //*[@id="nav-searchform"]/div[2]
    search_button = driver.find_element(by=By.XPATH, value='//*[@id="nav-searchform"]/div[2]')
    search_button.click()
    '''


if __name__ == "__main__":
    main()

