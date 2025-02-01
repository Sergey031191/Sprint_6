from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class DzenPage(BasePage):

    DZEN_LOGO = (By.XPATH, ".//button[text()='Найти']")

    @allure.step("Ожидание загрузки главной страницы 'Дзен'")
    def wait_for_dzen_page_loading(self):
        self.wait_for_visibility_of_element(self.DZEN_LOGO)

