import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CSS_SELECTOR, value="button.btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, value="input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    browser.find_element(By.ID, value="answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, value="button.btn").click()
    print(browser.switch_to.alert.text)

finally:
    browser.quit()