from selenium import webdriver
import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import order_page_data
from data.urls import PagesUrls
from locators import main_page_locators, order_page_locators


class TestScooterOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Firefox()

    @allure.title("Тест заказа доставки самоката")
    @allure.description("Клик по кнопке заказать -> заполнение формы правильными данными -> подтверждение заказа -> "
                        "Появляется окно с возможностью посмотреть статус")
    @pytest.mark.parametrize("order_button, fio_pack, date, rent_time, scooter_color, comment", [
        [main_page_locators.BUTTON_ORDER_TOP,
         order_page_data.FIO_PACK_1,
         order_page_data.DATE_1,
         order_page_locators.ONDE_DAY_RENT,
         order_page_locators.SCOOTER_BLACK,
         order_page_data.COMMENT_1
         ],
        [main_page_locators.BUTTON_ORDER_DOWN,
         order_page_data.FIO_PACK_2,
         order_page_data.DATE_2,
         order_page_locators.FOUR_DAY_RENT,
         order_page_locators.SCOOTER_GRAY,
         order_page_data.COMMENT_2
         ]
    ])
    def test_scooter_order(self, order_button, fio_pack, date, rent_time, scooter_color, comment):
        self.driver.get(PagesUrls.MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        main_page.wait_for_element_to_be_clickable(main_page_locators.YANDEX_LOGO)
        main_page.order_button_click(order_button)
        order_page = OrderPage(self.driver)
        order_page.user_info_input(fio_pack[0],
                                   fio_pack[1],
                                   fio_pack[2],
                                   fio_pack[3])
        order_page.click_next_button()
        order_page.wait_for_page_loading()
        order_page.about_rent_form_input(date, rent_time, scooter_color, comment)
        order_page.order_button_click()
        order_page.order_approve_window_wait()
        order_page.order_yes_button_click()
        order_page.wait_for_success_window()
        assert "Посмотреть статус" == order_page.get_element_text(order_page_locators.ORDER_POPUP_STATUS_BUTTON)


    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
