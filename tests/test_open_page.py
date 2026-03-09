def test_open_page(page):

    page.goto("http://www.google.com")

    assert "Google" in page.title()

