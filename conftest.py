from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    lng = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lng})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()