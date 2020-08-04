# author:吴紫葳
# times:2020/8/4 11:05
# # coding:-*- utf-8 -*-

from pages.homePage import Home


class TestHome:
    def test_judgment_language(self):
        assert '语言选择' in Home.judgment_language_ele().text

    def test_choose_language(self):
        Home.choose_languages_ele().click()
        assert '确认菜品' in Home.assert_choose_languages_ele().text
