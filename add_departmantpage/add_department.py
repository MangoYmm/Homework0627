import allure
from selenium.webdriver.common.by import By

from LearningTestDevelop.learningWebAuto.addDepartHomework.base.base import Base


class Add_Department_Page(Base):
    _INPUTNAME=(By.XPATH,'//form[@class="form"]/div[1]/input')
    _CHOOSEDEPARTBOX=(By.XPATH, '//form[@class="form"]/div[3]/a/span[text()="选择所属部门"]')
    _CHOOSEDEPART=(By.XPATH, '//form[@class="form"]/div[3]/div//a[text()="BaiBai"]')
    _ADDSUBMIT=(By.CSS_SELECTOR, 'a.qui_btn.ww_btn[d_ck="submit"]')
    def add_department_page(self,name):
        from LearningTestDevelop.learningWebAuto.addDepartHomework.contactpage.contact_page import Contact_page
        with allure.step("输入部门名称"):
            self.find_and_sendkeys(*self._INPUTNAME,name)
        with allure.step("点击部门框"):
            self.find_and_click(*self._CHOOSEDEPARTBOX)
        with allure.step("选择部门"):
            self.find_and_click(*self._CHOOSEDEPART)
        with allure.step("点击添加部门确认按钮"):
            self.find_and_click(*self._ADDSUBMIT)
        with allure.step("截图"):
            #切记这里的地址要用双引号，否则截的图在报告中看不到
            path="../data/{}.png".format(name)
            self.driver.save_screenshot(path)
            allure.attach.file(path,attachment_type=allure.attachment_type.PNG,name=f'添加{name}的截图')
        return  Contact_page(self.driver)