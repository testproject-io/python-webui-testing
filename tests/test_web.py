"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import json
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

from selenium.webdriver import Chrome, Firefox


@pytest.fixture(scope='session')
def config():
  # Read the JSON config file and returns it as a parsed dict
  with open('tests/config.json') as config_file:
    data = json.load(config_file)
  return data


@pytest.fixture
def browser(config):
  # Initialize WebDriver
  if config['browser'] == 'chrome':
    driver = Chrome()
  elif config['browser'] == 'firefox':
    driver = Firefox()
  else:
    raise Exception(f'"{config["browser"]}" is not a supported browser')

  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(config['wait_time'])
  
  # Return the driver object at the end of setup
  yield driver
  
  # For cleanup, quit the driver
  driver.quit()


def test_basic_duckduckgo_search(browser):
  # Set up test case data
  PHRASE = 'panda'

  # Search for the phrase
  search_page = DuckDuckGoSearchPage(browser)
  search_page.load()
  search_page.search(PHRASE)

  # Verify that results appear
  result_page = DuckDuckGoResultPage(browser)
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE
