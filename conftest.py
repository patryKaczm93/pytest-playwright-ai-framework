import pytest
import os
from framework.browser.browser_manager import BrowserManager

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
            screenshot_path = f"reports/screenshots/{item.name}_FAILED.png"
            page.screenshot(path=screenshot_path)