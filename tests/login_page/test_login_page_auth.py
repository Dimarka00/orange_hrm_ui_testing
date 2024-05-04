from config.data import Data
from pages.login_page import LoginPage


def test_login_with_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(Data.USERNAME, Data.PASSWORD)
    assert 'dashboard/index' in driver.current_url


def test_login_with_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login("", "")
    assert login_page.get_required_message_for_username() == "Required"
    assert login_page.get_required_message_for_password() == "Required"


def test_login_with_empty_username_and_valid_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.enter_password(Data.PASSWORD)
    login_page.click_login_button()
    assert login_page.get_required_message_for_username() == "Required"


def test_login_with_empty_password_and_valid_username(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.enter_username(Data.USERNAME)
    login_page.click_login_button()
    assert login_page.get_required_message_for_password() == "Required"


def test_login_with_invalid_username_and_valid_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(Data.INVALID_USERNAME, Data.PASSWORD)
    assert login_page.get_invalid_credentials() == "Invalid credentials"


def test_login_with_valid_username_and_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(Data.USERNAME, Data.INVALID_PASSWORD)
    assert login_page.get_invalid_credentials() == "Invalid credentials"
