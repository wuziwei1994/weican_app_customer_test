# author:吴紫葳
# times:2020/8/4 10:29
# # coding:-*- utf-8 -*-

from pubilc.basePage import BasePage


class Home(BasePage):
    def __init__(self):
        super(Home, self).__init__()

        self.judgment_language_box = 'com.weicantimes.weican.customer:id/z6'
        self.choose_languages_box = 'com.weicantimes.weican.customer:id/g2'
        self.assert_choose_languages_box = 'com.weicantimes.weican.customer:id/xi'

    def judgment_language_ele(self):
        return self.driver.find_element_by_id(self.judgment_language_box)

    def choose_languages_ele(self):
        return self.driver.find_element_by_id(self.choose_languages_box)

    def assert_choose_languages_ele(self):
        return self.driver.find_element_by_id(self.assert_choose_languages_box)


Home = Home()


