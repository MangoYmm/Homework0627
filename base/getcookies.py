import time

import yaml
from selenium import webdriver

class GetCookies:
    def get_cookies(self):
        opts=webdriver.ChromeOptions()
        opts.debugger_address='127.0.0.1:9222'
        self.driver=webdriver.Chrome(options=opts)
        #self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        time.sleep(8)
        cookies = self.driver.get_cookies()
        with open('../data/cookies.yaml', 'w') as f:
            yaml.safe_dump(cookies, f)
        #self.driver.close()