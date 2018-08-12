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


    def __call__(self, max_loop, ans_sec_per_questions):
        n_question = len(self.get_contents())
        for i in range(n_question):
            content = self.get_contents(i)
            #imgs = content.find_elements_by_tag_name('img')
            key = self.toHash(questionAndImgs)

            inputs = content.find_elements_by_tag_name('input')
            inputs = self.exclude_hidden_type(inputs)
            ans_forms, check_btn = inputs[:-1], inputs[-1]

            self.solve(ans_forms, checkbtn)

            for ans_box in ans_boxes:
                self.solve()
            check_btn.click()



    def solve(self):
        ans_box.clear()
        ans_box.send_keys('1')
    

    def submit(self):
        self.driver.find_element_by_name('next').click()
        self.get_element_value_of(self.driver.find_elements_by_tag_name('input'), 'すべてを送信して終了する').click()
        self.get_elements_value_of(self.driver.find_elements_by_tag_name('input'), 'すべてを送信して終了する')[1].click()

