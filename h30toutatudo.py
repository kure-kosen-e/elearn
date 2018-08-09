import time
import elearndriver
from selenium import webdriver


class H30Toutatudo(elearndriver.ELearn):
    def __init__(self, driver):
        self.driver = driver
        

    def __call__(self, max_loop, ans_sec_per_questions):
        n_questions = len(self.get_contents())
        for i in range(n_questions):
            content = self.get_contents(i)
            imgs = content.find_elements_by_tag_name('img')
            inputs = content.find_elements_by_tag_name('input')
            inputs = self.exclude_hidden_type(inputs)
            ans_boxes, check_btn = inputs[:-1], inputs[-1]

            for ans_box in ans_boxes:
                ans_box.clear()
                ans_box.send_keys('1')
            check_btn.click()

        self.driver.find_element_by_name('next').click()
        self.get_element_value_of(self.driver.find_elements_by_tag_name('input'), 'すべてを送信して終了する').click()
        self.get_elements_value_of(self.driver.find_elements_by_tag_name('input'), 'すべてを送信して終了する')[1].click()
        time.sleep(5)

    
    def get_contents(self, index=None):
        contents = self.driver.find_element_by_id('responseform').find_element_by_tag_name('div').find_elements_by_class_name('content')
        if index is None:
            return contents
        else:
            return contents[index]

    def exclude_hidden_type(self, elements):
        return elements[1:]

    
    def get_element_value_of(self, elements, value):
        for e in elements:
            if e.get_attribute('value') == value:
                return e
        return None


    def get_elements_value_of(self, elements, value):
        correct_elems = []
        for e in elements:
            if e.get_attribute('value') == value:
                correct_elems += e,
        return correct_elems

