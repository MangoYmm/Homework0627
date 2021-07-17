import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from LearningTestDevelop.learningWebAuto.addDepartHomework.base.getcookies import GetCookies


class Base(GetCookies):
    def __init__(self,driver_base:WebDriver=None):

        if driver_base is None:
            self.get_cookies()
            opts=webdriver.ChromeOptions()
            opts.debugger_address='127.0.0.1:9222'
            self.driver=webdriver.Chrome(options=opts)
            #self.driver=webdriver.Chrome()
            # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            # with open('../data/cookies.yaml') as f:
            #     data=yaml.safe_load(f)
            # for i in data:
            #     self.driver.add_cookie(i)
            # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            print("实例化driver")
        else:
            self.driver=driver_base

    def  find_ele(self,by,locator):
        ele=self.driver.find_element(by,locator)
        return ele

    def find_eles(self, by, locator):
        eles=self.driver.find_elements(by, locator)
        return eles

    def find_and_click(self,by,locator):
        self.driver.find_element(by,locator).click()

    def find_and_sendkeys(self,by,locator,value):
        self.driver.find_element(by,locator).send_keys(value)

    def get_ele_attribute(self,by,locator):
        text=self.driver.find_element(by,locator).text()
        return text

    def get_ele_attribute(self,by,locator):
        text=self.find_ele(by,locator).text()
        return text

    def get_eles_attribute(self,by,locator):
        texts=[]
        for i in self.find_eles(by,locator):
            texts.append(i.text)
        return texts