"pytest -v --tb=line --reruns 1 3_6_Test_fixture_14.py"
"https://docs.pytest.org/en/latest/usage.html#modifying-python-traceback-printing"

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")