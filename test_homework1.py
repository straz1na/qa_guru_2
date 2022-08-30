from selene.support.shared import browser, config
from selene import be, have
import pytest

@pytest.fixture()
def configure_browser():
    browser.config.window_width = 400
    browser.config.window_height = 800
    browser.open('https://google.com')
    yield
    browser.close()

def test_positive(configure_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_negative(configure_browser):
    browser.element('[name="q"]').should(be.blank).type('selene gomez').press_enter()
    browser.element('[id="search"]').should(have.text('Что за болезнь волчанка Селена Гомес?'))