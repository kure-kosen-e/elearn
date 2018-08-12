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


    def select_element(self, elements, attribute, value):
        for e in elements:
            if e.get_attribute(attribute) == value:
                return e
        return None


    def select_elements(self, elements, attribute, value):
        correct_elems = []
        for e in elements:
            if e.get_attribute(attribute) == value:
                elems += e,
        return elems


    def req_post(self, url, data=None):
        moodle_session = self.driver.get_cookie('MoodleSession')['value']
        user_agent = self.driver.execute_script('return navigator.userAgent')
        print(user_agent)
        return requests.post(url, data=data, headers={'User-Agent': user_agent}, cookies={'MoodleSession': moodle_session}) 


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

