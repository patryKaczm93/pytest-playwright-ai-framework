import pytest
from framework.browser.browser_manager import Browser_Manager

@pytest.fixture
def page():

    manager = Browser_Manager()
    page = manager.start()

    yield page

    manager.stop()