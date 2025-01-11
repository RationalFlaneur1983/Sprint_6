import allure
from page_objects.base_page import BasePage
from helpers.locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import YandexScooterHomePageLocator as Locators
from selenium.webdriver.support import expected_conditions as EC


class YandexScooterHomePage(BasePage):
    @allure.step('Нажать на кнопку "Заказать" вверху главной страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.top_order_button_locator).click()

    @allure.step('Нажать на кнопку "Заказать" внизу главной страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.bottom_order_button_locator).click()

    @allure.step('Нажать на вопрос в разделе "Вопросы о важном"')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.faq_question_buttons_locator, 10)
        return elems[question_number].click()

    @allure.step('Нажать на лого Яндекса вверху')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.yandex_logo_link_locator).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.accept_cookies_button_locator).click()