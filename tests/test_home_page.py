import allure
from helpers.service_urls import Urls
from page_objects.home_page import YandexScooterHomePage

class TestYandexScooterHomePage:

    @allure.title('Переход к форме "Оформление заказа" по кнопке "Заказать" вверху домашней страницы')
    def test_click_top_order_button_show_order_page(self, driver):
        yandex_scooter_home_page = YandexScooterHomePage(driver)
        yandex_scooter_home_page.go_to_site()
        yandex_scooter_home_page.click_cookie_accept()
        yandex_scooter_home_page.click_top_order_button()
        assert yandex_scooter_home_page.current_url() == Urls.scooter_order_url

    @allure.title('Переход к форме "Оформление заказа" по кнопке "Заказать" внизу домашней страницы')
    def test_click_bottom_order_button_show_order_page(self, driver):
        yandex_scooter_homepage = YandexScooterHomePage(driver)
        yandex_scooter_homepage.go_to_site()
        yandex_scooter_homepage.click_cookie_accept()
        yandex_scooter_homepage.click_bottom_order_button()

        assert yandex_scooter_homepage.current_url() == Urls.scooter_order_url

    @allure.title('При нажатии на лого "ЯндексСамокат" происходит редирект на страницу "ЯндексДзен"')
    def test_click_yandex_button_go_to_yandex(self, driver):
        yandex_scooter_home_page = YandexScooterHomePage(driver)
        yandex_scooter_home_page.go_to_site()
        yandex_scooter_home_page.click_cookie_accept()
        yandex_scooter_home_page.click_yandex_button()
        yandex_scooter_home_page.switch_window(1)
        yandex_scooter_home_page.wait_url_until_not_about_blank()
        current_url = yandex_scooter_home_page.current_url()

        assert (Urls.yandex_search in current_url) or (Urls.dzen_domain in current_url) or (Urls.yandex_domain in current_url)
