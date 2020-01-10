'''pytest -s -v -m "not smoke" 3_5_Test_fixture_8.py'''
'''pytest -s -v -m "smoke or regression" 3_5_Test_fixture_8.py'''
'''pytest -s -v -m "smoke and win10" 3_5_Test_fixture_8.py'''
'''pytest.ini'''

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")