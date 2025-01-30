from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_element_text(self, locator):
        element_text = self.driver.find_element(*locator).text
        return element_text
