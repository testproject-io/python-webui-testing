"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
  # Initialize ChromeDriver
  driver = Chrome()

  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(10)
  
  # Return the driver object at the end of setup
  yield driver
  
  # For cleanup, quit the driver
  driver.quit()


def test_basic_duckduckgo_search(browser):
  # Set up some test case data
  URL = 'https://www.duckduckgo.com'
  PHRASE = 'panda'

  # Navigate to the DuckDuckGo home page
  browser.get(URL)

  # Find the search input element
  # In the DOM, it has a 'name' attribute of 'q'
  search_input = browser.find_element_by_name('q')

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE + Keys.RETURN)

  # Verify that results appear on the results page
  link_divs = browser.find_elements_by_css_selector('#links > div')
  assert len(link_divs) > 0

  # Verify that at least one search result contains the search phrase
  xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
  phrase_results = browser.find_elements_by_xpath(xpath)
  assert len(phrase_results) > 0

  # Verify that the search phrase is the same
  search_input = browser.find_element_by_name('q')
  assert search_input.get_attribute('value') == PHRASE
