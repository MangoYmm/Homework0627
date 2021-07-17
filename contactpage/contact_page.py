import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from LearningTestDevelop.learningWebAuto.addDepartHomework.add_departmantpage.add_department import Add_Department_Page
from LearningTestDevelop.learningWebAuto.addDepartHomework.base.base import Base


class Contact_page(Base):
    _ADD=(By.XPATH,'//div[@class="member_colLeft_cntWrap"]/div/a')
    _ADDDEPARTMENT=(By.XPATH,'//a[@class="js_create_party"]')
    _DEPARTMENTS=(By.XPATH,'//div[@class="member_colLeft_bottom"]/div[2]/ul/li/ul/li/a')
    #_POINTTHREE=(By.XPATH,'//div[@class="member_colLeft_bottom"]/div[2]/ul/li/ul/li/a/span')
    _DELETE=(By.XPATH,'//li/a[text()="删除"]')
    _DELETESUBMIT=(By.CSS_SELECTOR,'#__dialog__MNDialog__ a.qui_btn.ww_btn[d_ck="submit"]')
    def go_to_addDepertpage(self):
        time.sleep(5)
        with allure.step("点击加号"):
            self.find_and_click(*self._ADD)
        with allure.step("点击添加部门"):
            self.find_and_click(*self._ADDDEPARTMENT)
        return Add_Department_Page(self.driver)

    def get_alldepart_name(self):
        with allure.step("获得当前的所有的部门名称"):
            texts=self.get_eles_attribute(*self._DEPARTMENTS)
            return texts


    def delete_new_depart_name(self,name):
        if name in self.get_alldepart_name():
            #ActionChains(self.driver).click()
            with allure.step("点击刚新增的部门"):
                self.find_and_click(By.XPATH,f'//div[@class="member_colLeft_bottom"]/div[2]/ul/li/ul/li/a[text()="{name}"]')
            with allure.step("点击右侧的点点点"):
                self.find_and_click(By.XPATH,'//div[@class="member_colLeft_bottom"]/div[2]/ul/li/ul/li/a[text()="{}"]/span'.format(name))
            with allure.step("点击删除按钮"):
                self.find_and_click(*self._DELETE)
            with allure.step("点击确定按钮"):
                self.find_and_click(*self._DELETESUBMIT)
