from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestSelectors(unittest.TestCase):
    def test_link1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.first")
            first_name.send_keys("test")
            last_name = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.second")
            last_name.send_keys("test")
            email_field = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.third")
            email_field.send_keys("test@test.com")

# Отправляем заполненную форму
            button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
            button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
            time.sleep(1)

    # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(by=By.CSS_SELECTOR, value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "wrong message")
        finally:
            browser.quit()

    def test_link2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.first")
            first_name.send_keys("test")
            last_name = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.second")
            last_name.send_keys("test")
            email_field = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.third")
            email_field.send_keys("test@test.com")

                # Отправляем заполненную форму
            button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
            button.click()

                # Проверяем, что смогли зарегистрироваться
                # ждем загрузки страницы
            time.sleep(1)

                # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(by=By.CSS_SELECTOR, value="h1")
                # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

                # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "wrong message")
        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()


#Попробуйте оформить тесты из первого модуля в стиле unittest.

# Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# Создайте новый файл
# Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# Запустите получившиеся тесты из файла
# Просмотрите отчёт о запуске и найдите последнюю строчку
# Отправьте эту строчку в качестве ответа на это задание
# Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!
#
# Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения.


