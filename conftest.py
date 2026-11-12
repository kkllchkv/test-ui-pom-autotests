import pytest

from selenium import webdriver

from pages.cart import Cart
from pages.desk_category import DeskCategory
from pages.main_page import MainPage
from pages.office_chair_card import OfficeChairCard


@pytest.fixture
def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument(
        "--unsafely-treat-insecure-origin-as-secure=http://testshop.qa-practice.com"
    )
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(chrome_options)
    yield driver
    driver.close()


@pytest.fixture
def desk_category_page(driver):
    return DeskCategory(driver)


@pytest.fixture
def desk_cart_page(driver):
    return Cart(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def prepare_cart(main_page):
    main_page.open_page()
    main_page.add_first_product_to_cart()


@pytest.fixture
def office_chair_card(driver):
    return OfficeChairCard(driver)
