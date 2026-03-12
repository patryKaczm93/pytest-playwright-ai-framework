import pytest
import os
import time
from framework.browser.browser_manager import BrowserManager
from framework.pages.login_page import LoginPage


@pytest.fixture
def page(request):

    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    manager = BrowserManager(browser_name, headless)
    page = manager.start()

    yield page

    manager.stop()

def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chromium",
                     help="Browser to use: chromium, firefox")

    parser.addoption("--headless",
                     action="store_true",
                     help="Run in headless mode")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("reports/screenshots", exist_ok=True)
            worker = getattr(item.config, "workerinput", {"workerid": "main"})["workerid"]
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"reports/screenshots/{item.name}_{worker}_{timestamp}.png"
            page.screenshot(path=screenshot_path)

@pytest.fixture
def login_page(page):
    return LoginPage(page)
