import allure
from selenium import webdriver
from locators import main_page_locators, order_page_locators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.dzen_page import DzenPage
from data.main_page_data import MAIN_PAGE_URL


class TestClickToLogo:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Firefox()

    @allure.title("Тест перехода на страницу 'Яндекс Самокат'")
    @allure.description("Клик на лого 'Самокат'  -> переход на главную страницу 'Яндекс Самокат'")
    def test_go_to_scooter_home_page_by_clicking_on_scooter_logo(self):
        self.driver.get(MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        main_page.order_button_click(main_page_locators.BUTTON_ORDER_TOP)
        order_page = OrderPage(self.driver)
        order_page.click_on_element(order_page_locators.ORDER_SCOOTER_LOGO_BUTTON)
        assert MAIN_PAGE_URL == main_page.get_current_url()

    @allure.title('Тест перехода на страницу "Dzen"')
    @allure.description('Клик по лого "Яндекс" > переход на страницу "Dzen"')
    def test_go_to_dzen_click_yandex_logo(self):
        self.driver.get(MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        main_page.yandex_logo_click()
        main_page.go_to_dzen_page()
        dzen_page = DzenPage(self.driver)
        dzen_page.wait_for_dzen_page_loading()
        assert dzen_page.DZEN_PAGE_URL == dzen_page.get_current_url()

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
