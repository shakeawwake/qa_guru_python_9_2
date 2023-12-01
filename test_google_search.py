import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def browser_size():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    yield
    browser.quit()
def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))

def test_google_search_not_found():
    browser.open('https://www.google.ru/')
    browser.element('[name="q"]').should(be.blank).type('sfddfsfsfswedfwfewef').press_enter()
    browser.element('[class="mnr-c"]').should(have.text('По запросу sfddfsfsfswedfwfewef ничего не найдено.'))


