import allure
from helpers.service_urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DEFAULT_WAIT_TIME = 10

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=None):
        wait_time = time if time is not None else self.DEFAULT_WAIT_TIME
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )

    def find_elements(self, locator, time=None):
        wait_time = time if time is not None else self.DEFAULT_WAIT_TIME
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не удалось найти элементы по локатору {locator}"
        )

    @allure.step('Переход по указанному URL')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.scooter_home_url
        try:
            self.driver.get(url)
        except Exception as e:
            raise RuntimeError(f"Не удалось перейти по адресу {url}: {str(e)}")

    @allure.step('Вернуть текущий URL браузера')
    def current_url(self):
        return self.driver.current_url