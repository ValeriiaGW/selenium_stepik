from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def open_link(link):
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.first")
    first_name.send_keys("test")
    last_name = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.second")
    last_name.send_keys("test")
    email_field = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.third")
    email_field.send_keys("test@test.com")
    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(by=By.CSS_SELECTOR, value="h1")
    welcome_text = welcome_text_elt.text
    return welcome_text


class TestReg(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(open_link("http://suninjuly.github.io/registration1.html"), \
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_link2(self):
        self.assertEqual(open_link("http://suninjuly.github.io/registration2.html"), \
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__":
    unittest.main()


