import time
import elearndriver
from selenium import webdriver


class H30Toutatudo(elearndriver.ELearn):
    def __init__(self, driver):
        self.driver = driver
        

    def get_contents(self, index=None):
        contents = self.driver.find_element_by_id('responseform').find_element_by_tag_name('div').find_elements_by_class_name('content')
        if index is None:
            return contents
        else:
            return contents[index]

    def exclude_hidden_type(self, elements):
        return elements[1:]


    def parse_content(self, content):
        inputs = self.exclude_hidden_type(content.find_elements_by_tag_name('input'))
        ans_forms, check_btn = inputs[:-1], inputs[-1]
        key = self.toHash(questionAndImgs)


    def has_passed(self):
        return True


    def __call__(self, max_loop, ans_sec_per_questions):
        n_question = len(self.get_contents())
        for _ in range(max_loop):
            for i in range(n_question):
                content = self.get_contents(i)
                self.solve(content)
            self.submit()

            if self.has_passed():
                return 


    def solve(self, content):
        ans_box.clear()
        ans_box.send_keys('1')
    

    def submit(self):
        self.driver.find_element_by_name('next').click()
        self.select_element(self.driver.find_elements_by_tag_name('input'), 'value', 'すべてを送信して終了する').click()
        self.select_elements(self.driver.find_elements_by_tag_name('input'), 'value', 'すべてを送信して終了する')[1].click()

