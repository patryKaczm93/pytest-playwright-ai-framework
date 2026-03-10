from framework.pages.base_page import BasePage

class LoginPage(BasePage):

    def login(self, username, password):

        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("#login")
