def test_login_page(login_page):

    login_page.open("https://practice.expandtesting.com/login")

    login_page.login("practice", "SuperSecretPassword!")

    assert login_page.is_logged_in()

