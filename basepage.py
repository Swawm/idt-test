from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def _click_on_button(self, locator):
        self.driver.find_element(*locator).click()

    def _move_cursor_to_element(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def _go_on_site(self, url):
        self.driver.get(url)

    def _close_page(self):
        self.driver.close()

    def _wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def _wait_until_clickable(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print("Element not found. " + str(locator))
        return True


    def _quit(self):
        self.driver.close()