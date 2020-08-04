# author:吴紫葳
# times:2020/8/4 10:02
# # coding:-*- utf-8 -*-

from appium import webdriver
from config.settings import weican_customer


class Driver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', weican_customer)

            cls.driver.implicitly_wait(3)

        return cls.driver
