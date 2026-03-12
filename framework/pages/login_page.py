from framework.pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    SUCCESS_HEADER = "h1"


    def login(self, username, password):

        self.page.locator(self.USERNAME_INPUT).fill(username)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()

    def is_logged_in(self):

        return "Secure Area" in self.page.locator(self.SUCCESS_HEADER).text_content()
