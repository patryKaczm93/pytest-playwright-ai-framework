from playwright.sync_api import sync_playwright

class Browser_Manager:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        return self.page

    def stop(self):
        self.playwright.stop()
        self.browser.close()
