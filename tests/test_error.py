def test_error(page):

    page.goto("https://automationpractice.org")

    assert "ERROR" in page.text_content("h1")