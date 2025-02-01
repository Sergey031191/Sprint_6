import pytest
import allure
from selenium import webdriver
from locators import main_page_locators
from pages.main_page import MainPage
from data import main_page_data
from data.urls import PagesUrls


class TestFaqQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Firefox()

    @allure.title("Тест открытия ответов в FAQ")
    @allure.description("Клик по вопросам в FAQ по очереди -> проверяем, что появляющийся ответ соответствует "
                        "ожидаемому")
    @pytest.mark.parametrize("text,button, popup_text",
                             [
                                 [main_page_data.FaqAnswersData.COST_ANSWER,
                                  main_page_locators.BUTTON_COST,
                                  main_page_locators.TEXT_COST],
                                 [main_page_data.FaqAnswersData.FEW_ANSWER,
                                  main_page_locators.BUTTON_FEW,
                                  main_page_locators.TEXT_FEW],
                                 [main_page_data.FaqAnswersData.TIME_ANSWER,
                                  main_page_locators.BUTTON_TIME,
                                  main_page_locators.TEXT_TIME],
                                 [main_page_data.FaqAnswersData.TODAY_ANSWER,
                                  main_page_locators.BUTTON_TODAY,
                                  main_page_locators.TEXT_TODAY],
                                 [main_page_data.FaqAnswersData.DELAY_OR_EARLY_ANSWER,
                                  main_page_locators.BUTTON_DELAY_OR_EARLY,
                                  main_page_locators.TEXT_DELAY_OR_EARLY],
                                 [main_page_data.FaqAnswersData.CHARGE_ANSWER,
                                  main_page_locators.BUTTON_CHARGE,
                                  main_page_locators.TEXT_CHARGE],
                                 [main_page_data.FaqAnswersData.CANCEL_ORDER_ANSWER,
                                  main_page_locators.BUTTON_CANCEL_ORDER,
                                  main_page_locators.TEXT_CANCEL_ORDER],
                                 [main_page_data.FaqAnswersData.MKAD_ANSWER,
                                  main_page_locators.BUTTON_MKAD,
                                  main_page_locators.TEXT_MKAD],
                             ])
    def test_faq_list_click_on_questions_check_answer_true(self, text, button, popup_text):
        self.driver.get(PagesUrls.MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        main_page.click_question(button)
        main_page.wait_for_visibility_of_element(popup_text)

        assert text == main_page.get_element_text(popup_text)


    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
