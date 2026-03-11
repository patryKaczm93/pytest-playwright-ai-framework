from playwright.sync_api import sync_playwright

class BrowserManager:

    def __init__(self, browser_name="chromium", headless=False):

        self.browser_name = browser_name
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        if self.browser_name == "chromium":
            self.browser = self.playwright.chromium.launch(headless=self.headless)
        elif self.browser_name == "firefox":
            self.browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_name == "webkit":
            self.browser = self.playwright.webkit.launch(headless=self.headless)
        else:
            raise Exception("Unknown browser %s" % self.browser_name)

        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        return self.page

    def stop(self):

        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
