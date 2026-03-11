from framework.pages.login_page import LoginPage

def test_login_page(page):

    login_page = LoginPage(page)

    login_page.open("https://practice.expandtesting.com/login")

    login_page.login("abs", "abs")

    assert "Test Login Page for Automation Testing Practice" in page.title()

