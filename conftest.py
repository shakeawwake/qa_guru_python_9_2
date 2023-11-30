import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.window_width = 1200
    browser.config.window_height = 1080
    browser.config.browser_name = 'chrome'
    yield
    browser.quit()
