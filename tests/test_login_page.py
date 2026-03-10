from framework.pages.login_page import LoginPage

def test_login_page(page):

    login_page = LoginPage(page)

    login_page.open("https://practice.expandtesting.com/login")

    assert "Login" in page.title()

