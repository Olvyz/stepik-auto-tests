import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link_opc', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_feedback(browser, link_opc):
    link = f"{link_opc}/"
    browser.get(link)
    input1 = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@placeholder='Напишите ваш ответ здесь...']")))
    input1.send_keys(str(math.log(int(time.time()))))

    button = browser.find_element_by_xpath('//button[text()="Отправить"]')
    button.click()

    asert_eror = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    assert asert_eror == "Correct!", asert_eror





