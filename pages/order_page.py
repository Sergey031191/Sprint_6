import allure
from pages.base_page import BasePage
from selenium.webdriver import Keys
from locators import order_page_locators


class OrderPage(BasePage):

    @allure.step("Ввод имени в поле Имя")
    def set_name(self, name):
        self.send_keys(order_page_locators.NAME_FIELD, name)

    @allure.step("Ввод фамилии в поле Фамилия")
    def set_surname(self, surname):
        self.send_keys(order_page_locators.SURNAME_FIELD, surname)

    @allure.step("Ввод адреса в поле Адрес")
    def set_adres(self, adres):
        self.send_keys(order_page_locators.ADRES_FIELD, adres)

    @allure.step("Ввод телефона в поле Телефон")
    def set_phone(self, phone):
        self.send_keys(order_page_locators.PHONE_FIELD, phone)

    @allure.step("Клик по полю Метро")
    def click_on_metro_list(self):
        self.click_on_element(order_page_locators.METRO_FIELD)

    @allure.step("Выбор станции Речной вокзал")
    def click_on_metro_station(self):
        self.scroll_to_element(order_page_locators.STATION)
        self.wait_for_element_to_be_clickable(order_page_locators.STATION)
        self.click_on_element(order_page_locators.STATION)

    @allure.step("Ввод данных пользователя")
    def user_info_input(self, name, surname, adres, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_adres(adres)
        self.click_on_metro_list()
        self.click_on_metro_station()
        self.set_phone(phone)

    @allure.step("Клик на кнопку далее")
    def click_next_button(self):
        self.click_on_element(order_page_locators.NEXT_BUTTON)

    @allure.step("Ожидание загрузки окна 'Про аренду'")
    def wait_for_page_loading(self):
        self.wait_for_visibility_of_element(order_page_locators.RENT_HEADER)

    @allure.step("Заполнение поля Когда Привезти Самокат")
    def rent_date_field_input(self, date):
        self.send_keys(order_page_locators.RENT_DATE_FIELD, date)
        self.send_keys(order_page_locators.RENT_DATE_FIELD, Keys.ENTER)

    @allure.step("Клик на поле Срок Аренды")
    def rent_time_field_click(self):
        self.click_on_element(order_page_locators.RENT_PERIOD_FIELD)

    @allure.step("Выбор срока аренды")
    def rent_time_overall_click(self, rent_period):
        self.click_on_element(rent_period)

    @allure.step("Выбор цвета самоката")
    def scooter_color_click(self, color_button):
        self.click_on_element(color_button)

    @allure.step("Заполнение поля Комментарий для курьера")
    def comment_field_input(self, text):
        self.send_keys(order_page_locators.COMMENT_FIELD, text)

    @allure.step("Заполнение формы Про Аренду")
    def about_rent_form_input(self, date, rent_period, color_button, text):
        self.wait_for_page_loading()
        self.rent_date_field_input(date)
        self.rent_time_field_click()
        self.rent_time_overall_click(rent_period)
        self.scooter_color_click(color_button)
        self.comment_field_input(text)

    @allure.step("Нажатие кнопки заказать")
    def order_button_click(self):
        self.click_on_element(order_page_locators.ORDER_BUTTON)

    @allure.step("Ожидание окна о подтверждении заказа")
    def order_approve_window_wait(self):
        self.wait_for_visibility_of_element(order_page_locators.ORDER_POPUP_HEADER)

    @allure.step("Нажатие кнопки Да в окне о подтвеждении заказа")
    def order_yes_button_click(self):
        self.click_on_element(order_page_locators.ORDER_YES_BUTTON)

    @allure.step("Ожидание окна об успешном заказе самоката")
    def wait_for_success_window(self):
        self.wait_for_visibility_of_element(order_page_locators.ORDER_SUCCESS_HEADER)


