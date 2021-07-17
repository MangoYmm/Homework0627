import ast

import pytest
from selenium.webdriver.common.by import By
from LearningTestDevelop.learningWebAuto.addDepartHomework.base.base import Base
from LearningTestDevelop.learningWebAuto.addDepartHomework.contactpage.contact_page import Contact_page


class Main_Page(Base):
    _CONTACT=(By.XPATH,'//span[text()="通讯录"]')
    #@pytest.mark.parametrize('_CONTACT',*maineles[0])
    def go_to_contactpage(self):
        self.find_and_click(*self._CONTACT)
        return Contact_page(self.driver)