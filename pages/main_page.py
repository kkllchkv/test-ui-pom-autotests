from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.main_page import add_to_cart_buttons, continue_shopping_button, my_cart_quantity_element


class MainPage(BasePage):
    def open_page(self):
        # переопределение родительского метода; у главной страницы только хост
        self.driver.get(f'{self.base_url}')

    def add_first_product_to_cart(self):
        add_to_cart_elements = self.find_all(add_to_cart_buttons)
        if len(add_to_cart_elements) == 0:
            raise ValueError("Couldn't find any add to cart elements")

        first_product = add_to_cart_elements[0]
        first_product.click()

        self.wait_for_element_to_appear(continue_shopping_button)
        close_button = self.find(continue_shopping_button)
        close_button.click()

        try:
            self.wait_until_element_not_have_text(my_cart_quantity_element, '0')
        except TimeoutException as e:
            raise TimeoutException(f"Failed to setup product before test launch. Error: {e}")

        print('Successfully added first product to cart')
