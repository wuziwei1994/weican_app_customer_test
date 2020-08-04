# author:吴紫葳
# times:2020/8/4 10:45
# # coding:-*- utf-8 -*-

from drivers.driver import Driver


class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()
