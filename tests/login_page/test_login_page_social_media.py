from pages.login_page import LoginPage


def test_opening_page_linkedin(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.click_linkedin_link()
    login_page.switch_to_new_tab()
    assert "https://ru.linkedin.com/company/orangehrm" in login_page.current_url()


def test_opening_page_facebook(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.click_facebook_link()
    login_page.switch_to_new_tab()
    assert "https://www.facebook.com/OrangeHRM/" in login_page.current_url()


def test_opening_page_twitter(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.click_twitter_link()
    login_page.switch_to_new_tab()
    assert login_page.current_url() == "https://twitter.com/orangehrm?lang=en"


def test_opening_page_youtube(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.click_youtube_link()
    login_page.switch_to_new_tab()
    assert "www.youtube.com/c/OrangeHRMInc" in login_page.current_url()
