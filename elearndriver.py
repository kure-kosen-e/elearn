import time
import argparse
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By




class ELearn:
    def __init__(self, driver=webdriver.Firefox()):
        self.driver = driver
        self.driver.implicitly_wait(60)

    
    def get_sesskey(self):
        return self.driver.find_element_by_name('sesskey').get_attribute('value')


    def req_post(self, url, data=None):
        moodle_session = self.driver.get_cookie('MoodleSession')['value']
        return requests.post(url, data=data, cookies={'MoodleSession': moodle_session}) 


    def login(self, username, password):
        login_page = 'https://e-mdl.kure-nct.ac.jp/login/index.php'
    
        self.driver.get(login_page)
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('loginbtn').click()
    
    
    def logout(self):
        logout_page = 'https://e-mdl.kure-nct.ac.jp/login/logout.php?sesskey='
    
        self.driver.get(logout_page + self.get_sesskey())


    def take_exam(self, id):
        problems_page = 'https://e-mdl.kure-nct.ac.jp/mod/quiz/startattempt.php'

        res = self.req_post(problems_page, data={'cmid': id, 'sesskey': self.get_sesskey()})
        self.driver.get(res.url)
    

    def solve(self, max_loop=100, ans_sec_per_questions=20):
        import h30toutatudo
        h30toutatudo.H30Toutatudo(self.driver)(max_loop, ans_sec_per_questions)


    def quit(self):
        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-u', '--username', required=True)
    parse.add_argument('-p', '--password', required=True)
    args = parse.parse_args()
    
    driver = webdriver.Firefox()
    elearn = ELearn(driver)

    elearn.login(args.username, args.password)
    elearn.logout()

    time.sleep(10)

    driver.close()
    driver.quit()
    
