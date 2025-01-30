import allure
from pages.base_page import BasePage
from locators import main_page_locators


class MainPage(BasePage):

    @allure.step("Клик на вопрос")
    def click_question(self, locator):
        self.scroll_to_element(locator)
        self.wait_for_element_to_be_clickable(locator)
        self.click_on_element(locator)

    @allure.step("Клик по лого Яндекса")
    def yandex_logo_click(self):
        self.wait_for_element_to_be_clickable(main_page_locators.YANDEX_LOGO)
        self.click_on_element(main_page_locators.YANDEX_LOGO)

    @allure.step("Клик по кнопке Заказать")
    def order_button_click(self, locator):
        self.scroll_to_element(locator)
        self.wait_for_element_to_be_clickable(locator)
        self.click_on_element(locator)

    @allure.step("Переход на страницу 'Дзен'")
    def go_to_dzen_page(self):
        self.switch_to_window()



