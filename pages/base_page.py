from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(*locator).click()

    def open(self, url):
        return self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        return self.driver.find_element(locator).text

    def get_title(self):
        return self.driver.title

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_all_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(locator)
        )
