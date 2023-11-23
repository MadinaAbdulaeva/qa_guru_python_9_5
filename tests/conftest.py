import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options
    browser.config.window_width = 1024
    browser.config.window_height = 768

    yield
    browser.quit()
