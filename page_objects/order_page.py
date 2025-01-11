import re
from page_objects.base_page import BasePage
from helpers.locators import YandexScooterOrderPageLocator as Locators
import allure

class YandexScooterOrderPage(BasePage):
    @allure.step('Страница "Для кого самокат": ввести фамилию')
    def input_last_name(self, last_name: str):
        return self.find_element(Locators.last_name_input_field_locator).send_keys(last_name)

    @allure.step('Страница "Для кого самокат": ввести имя')
    def input_first_name(self, first_name: str):
        return self.find_element(Locators.first_name_input_field_locator).send_keys(first_name)

    @allure.step('Страница "Для кого самокат": ввести адрес')
    def input_address(self, address: str):
        return self.find_element(Locators.address_input_field_locator).send_keys(address)

    @allure.step('Страница "Для кого самокат": выбрать метро')
    def choose_subway(self, subway_name: str):
        self.find_element(Locators.subway_input_field_locator).click()
        return self.find_element(Locators.subway_hint_button(subway_name)).click()

    @allure.step('Страница "Для кого самокат": ввести номера телефона')
    def input_telephone_number(self, telephone_number: str):
        return self.find_element(Locators.telephone_number_field).send_keys(telephone_number)

    @allure.step('Перейти страницу "Про аренду" по клику на кнопку "Далее"')
    def go_next(self):
        return self.find_element(Locators.next_button_locator).click()

    @allure.step('Страница "Про аренду": ввести дату')
    def input_date(self, date: str):
        return self.find_element(Locators.date_field_locator).send_keys(date)

    @allure.step('Страница "Про аренду": выбрать период аренды')
    def choose_rental_period(self, option: int):
        self.find_element(Locators.rental_period_dropdown_locator).click()
        return self.find_elements(Locators.rental_period_options_locator)[option].click()

    @allure.step('Страница "Про аренду": выбрать цвет')
    def choose_color(self, option: int):
        return self.find_elements(Locators.color_options_checkboxes_locator)[option].click()

    @allure.step('Страница "Про аренду": добавить комментарий для курьера')
    def input_comment(self, comment_text):
        return self.find_element(Locators.courier_comment_locator).send_keys(comment_text)

    @allure.step('Страница "Про аренду": нажать на кнопку "Заказать"')
    def click_order(self):
        return self.find_element(Locators.order_button_locator).click()

    @allure.step('Страница "Про аренду": нажать на кнопку "Подтвердить заказ"')
    def click_accept_order(self):
        return self.find_element(Locators.confirm_order_button_locator).click()

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        about_order_text = self.find_element(Locators.order_confirmation_message_locator).text
        return ''.join(re.findall('[0-9]', about_order_text))

    @allure.step('Перейти к статусу заказа')
    def click_go_to_status(self):
        return self.find_element(Locators.show_status_button_locator).click()

    @allure.step('Заполнить данные на странице "Для кого самокат"')
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.choose_subway(data_set['subway_name'])
        self.input_telephone_number(data_set['telephone_number'])

    @allure.step('Заполнить данные на странице "Про аренду"')
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rent_period'])
        for option in data_set['color']:
            self.choose_color(option)
        self.input_comment(data_set['comment_for_courier'])