from pages.login_page import LoginPage


def test_login_with_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(username="Admin", password="admin123")
    assert 'dashboard/index' in driver.current_url


def test_login_with_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(username="", password="")
    assert login_page.get_required_message_for_username() == "Required"
    assert login_page.get_required_message_for_password() == "Required"


def test_login_with_empty_username_and_valid_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.enter_password(password="admin123")
    login_page.click_login_button()
    assert login_page.get_required_message_for_username() == "Required"


def test_login_with_empty_password_and_valid_username(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.enter_username(username="Admin")
    login_page.click_login_button()
    assert login_page.get_required_message_for_password() == "Required"
