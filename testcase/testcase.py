import ast
import time

import allure
import pytest
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from LearningTestDevelop.learningWebAuto.addDepartHomework.base.base import Base
from LearningTestDevelop.learningWebAuto.addDepartHomework.contactpage.contact_page import Contact_page
from LearningTestDevelop.learningWebAuto.addDepartHomework.mainpage.main_page import Main_Page


def get_yamldata():
    with open('../data/data.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas["name"]


@allure.feature("测试添加部门")
class TestAddDepartment:
    #name='部门1'
    def setup(self):
        self.main=Main_Page()
    def teardown(self):
        pass

    @allure.story("添加部门成功")
    @pytest.mark.parametrize('name',get_yamldata())
    @allure.title("添加部门成功")
    def test_add_department_success(self,name):
        """
        登录进入首页
        点击通讯录，进入通讯录页
        点击添加部门，进入添加窗口
        填写添加信息，点击保存，回到通讯录页
        断言
        """
        result=self.main.go_to_contactpage().go_to_addDepertpage().add_department_page(name).get_alldepart_name()
        assert name in result

    @allure.story("删除添加的部门")
    @pytest.mark.parametrize('name', get_yamldata())
    @allure.title("删除添加的部门")
    def test_delete_department(self,name):
        self.main.go_to_contactpage().delete_new_depart_name(name)
        time.sleep(3)
        assert name not in self.main.go_to_contactpage().get_alldepart_name()