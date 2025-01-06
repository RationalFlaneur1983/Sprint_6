import pytest
import allure
from helpers.service_urls import Urls
from page_objects.home_page import YandexScooterHomePage
from page_objects.order_page import YandexScooterOrderPage
from helpers.ui_test_data import YandexScooterOrderForm as order_data


class TestYaScooterOrderPage:

    @allure.title('Оформление заказа и переход на страницу с заказом')
    @allure.description('Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа"')
    @pytest.mark.parametrize('data_set', ['data_set_1', 'data_set_2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        yandex_scooter_order_page = YandexScooterOrderPage(driver)
        yandex_scooter_order_page.go_to_site(Urls.scooter_order_url)
        yandex_scooter_home_page = YandexScooterHomePage(driver)
        yandex_scooter_home_page.click_cookie_accept()
        yandex_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        yandex_scooter_order_page.go_next()
        yandex_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        yandex_scooter_order_page.click_order()
        yandex_scooter_order_page.click_accept_order()
        order_number = yandex_scooter_order_page.get_order_number()
        yandex_scooter_order_page.click_go_to_status()
        current_url = yandex_scooter_order_page.current_url()
        assert (Urls.scooter_status_url in current_url) and (order_number in current_url)