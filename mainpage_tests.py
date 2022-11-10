import pytest
from basepage import BasePage
from selenium import webdriver
import locators
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


# Test-case 1. Check all pages from top menu/submenu and make sure that pages appears correctly
@pytest.mark.parametrize("menu,locator,expected", [(locators.WOMEN_MENU, locators.T_SHIRTS, "T-shirts"),
                                                   (locators.WOMEN_MENU, locators.BLOUSES, "Blouses"),
                                                   (locators.WOMEN_MENU, locators.CASUAL_DRESSES, "Casual Dresses"),
                                                   (locators.WOMEN_MENU, locators.EVENING_DRESSES, "Evening Dresses"),
                                                   (locators.WOMEN_MENU, locators.SUMMER_DRESSES, "Summer Dresses"),
                                                   (locators.DRESSES_MENU, locators.CASUAL_DRESSES_FROM_DRESS_MENU,
                                                    "Casual Dresses"),
                                                   (locators.DRESSES_MENU, locators.EVENING_DRESSES_FROM_DRESS_MENU,
                                                    "Evening Dresses"),
                                                   (locators.DRESSES_MENU, locators.SUMMER_DRESSES_FROM_DRESS_MENU,
                                                    "Summer Dresses")
                                                   ])
def test_menu_buttons(menu, locator, expected):
    url = "http://automationpractice.com/"
    page = BasePage(driver, url)
    page._go_on_site(url)
    page._wait_until_clickable(menu)
    page._move_cursor_to_element(menu)
    page._wait_until_clickable(locator)
    page._click_on_button(locator)
    assert expected in driver.title
    page._quit()
