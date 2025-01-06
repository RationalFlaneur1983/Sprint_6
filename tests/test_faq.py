import pytest
import allure
from page_objects.home_page import YandexScooterHomePage
from helpers.ui_test_data import YandexScooterHomePageFAQ
from helpers.locators import YandexScooterHomePageLocator

class TestYandexScooterFAQPage:

    @pytest.mark.parametrize("question,answer,expected_answer",
        [
            (0, 0, YandexScooterHomePageFAQ.answer_1),
            (1, 1, YandexScooterHomePageFAQ.answer_2),
            (2, 2, YandexScooterHomePageFAQ.answer_3),
            (3, 3, YandexScooterHomePageFAQ.answer_4),
            (4, 4, YandexScooterHomePageFAQ.answer_5),
            (5, 5, YandexScooterHomePageFAQ.answer_6),
            (6, 6, YandexScooterHomePageFAQ.answer_7),
            (7, 7, YandexScooterHomePageFAQ.answer_8),
        ]
    )

    @allure.title('Проверка ответов в блоке "Вопросы о важном".')
    @allure.description('Когда нажимаешь на стрелочку в блоке "Вопросы о важном" открывается соответствующий текст.')
    def test_faq_click_on_question_show_answer(self, driver, question, answer, expected_answer):
        yandex_scooter_home_page = YandexScooterHomePage(driver)
        yandex_scooter_home_page.go_to_site()
        yandex_scooter_home_page.click_cookie_accept()
        yandex_scooter_home_page.click_faq_question(question_number=question)
        answer = yandex_scooter_home_page.find_element(YandexScooterHomePageLocator.get_faq_answer_locator(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ не совпадает с ОР'