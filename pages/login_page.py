from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPageLocators:
    LOGIN_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    INVALID_CREDENTIALS = (By.XPATH, "//div[@role='alert']")
    REQUIRED_USERNAME = (By.XPATH, "(//span[text()='Required'])[1]")
    REQUIRED_PASSWORD = (By.XPATH, "(//span[text()='Required'])[2]")
    LINKEDIN_LINK = (By.XPATH, "//a[contains(@href,'linkedin.com')]")
    FACEBOOK_LINK = (By.XPATH, "//a[contains(@href,'facebook.com')]")
    TWITTER_LINK = (By.XPATH, "//a[contains(@href,'twitter.com')]")
    YOUTUBE_LINK = (By.XPATH, "//a[contains(@href,'youtube.com')]")


class LoginPage(BasePage):
    LOGIN_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        return self.open(self.LOGIN_URL)

    def enter_username(self, username):
        self.wait_for_element(LoginPageLocators.LOGIN_INPUT).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.wait_for_element(LoginPageLocators.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_required_message_for_username(self):
        return self.wait_for_element(LoginPageLocators.REQUIRED_USERNAME).text

    def get_required_message_for_password(self):
        return self.wait_for_element(LoginPageLocators.REQUIRED_USERNAME).text

    def get_invalid_credentials(self):
        return self.wait_for_element(LoginPageLocators.INVALID_CREDENTIALS).text

    def click_linkedin_link(self):
        self.wait_for_element(LoginPageLocators.LINKEDIN_LINK).click()

    def click_facebook_link(self):
        self.wait_for_element(LoginPageLocators.FACEBOOK_LINK).click()

    def click_twitter_link(self):
        self.wait_for_element(LoginPageLocators.TWITTER_LINK).click()

    def click_youtube_link(self):
        self.wait_for_element(LoginPageLocators.YOUTUBE_LINK).click()
