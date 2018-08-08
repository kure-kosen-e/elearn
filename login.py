import time
import argparse

from selenium import webdriver



def login(driver, username, password):
    login_page = 'https://e-mdl.kure-nct.ac.jp/login/index.php'

    driver.get(login_page)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('loginbtn').click()


def logout(driver):
    logout_page = 'https://e-mdl.kure-nct.ac.jp/login/logout.php?sesskey='
    sesskey = driver.find_element_by_name('sesskey').get_attribute('value')

    driver.get(logout_page + sesskey)


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-u', '--username', required=True)
    parse.add_argument('-p', '--password', required=True)
    args = parse.parse_args()
    
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    login(driver, args.username, args.password)
    logout(driver)

    time.sleep(10)

    driver.close()
    driver.quit()
    
