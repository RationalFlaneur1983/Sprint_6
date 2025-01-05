from selenium.webdriver.common.by import By


class BasePageLocator:
    accept_cookies_button_locator = [By.XPATH, ".//button[text()='да все привыкли']"]
    yandex_logo_link_locator = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]
    check_order_status_button_locator = [By.XPATH, ".//button[text()='Статус заказа']"]
    order_number_input_field_locator = [By.XPATH, ".//input[@placeholder='Введите номер заказа']"]
    go_to_order_status_button_locator = [By.XPATH, ".//button[text()='Go!']"]

class YandexScooterHomePageLocator:
    top_order_button_locator = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    bottom_order_button_locator = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]
    faq_question_buttons_locator = [By.XPATH, ".//div[@class='accordion__button']"]
    faq_answer_paragraphs_locator = [By.CSS_SELECTOR, ".accordion__panel > p"]
    order_status_button_locator = [By.XPATH, ".//button[text()='Статус заказа']"]

    @staticmethod
    def get_faq_question_button_locator(question_number):
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]

    @staticmethod
    def get_faq_answer_locator(answer_number):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p"]


class YandexScooterOrderPageLocator:
    first_name_input_field_locator = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    last_name_input_field_locator = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    address_input_field_locator = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    subway_input_field_locator = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]
    telephone_number_field = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]
    next_button_locator = [By.XPATH, ".//button[text()='Далее']"]
    back_button_locator = [By.XPATH, ".//button[text()='Назад']"]
    date_field_locator = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    rental_period_dropdown_locator = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    rental_period_options_locator = [By.XPATH, ".//div[@class='Dropdown-option']"]
    color_options_checkboxes_locator = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    courier_comment_locator = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    order_button_locator = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    confirm_order_button_locator = [By.XPATH, ".//button[text()='Да']"]
    order_confirmation_message_locator = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    show_status_button_locator = [By.XPATH, ".//button[text()='Посмотреть статус']"]

    @staticmethod
    def subway_hint_button(subway_name: str):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]
