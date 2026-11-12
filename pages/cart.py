from selenium.webdriver import Keys

from locators.cart import cart_lines, increase_amount_by_one_button, cart_quantity_element
from pages.base_page import BasePage


class Cart(BasePage):
    page_path = '/shop/cart'

    def assert_empty_cart(self):
        cart_text = self.find(cart_lines).text
        assert cart_text == 'Your cart is empty!'

    def increase_amount_by_one(self):
        increase_button = self.find(increase_amount_by_one_button)
        increase_button.click()

    def assert_amount(self, target_amount):
        amount_element = self.find(cart_quantity_element)
        assert amount_element.get_property('value') == target_amount

    def clear_amount_text(self):
        amount_input = self.find(cart_quantity_element)
        amount_input.clear()

    def manual_change_amount(self, amount):
        amount_input = self.find(cart_quantity_element)
        amount_input.send_keys(amount)
        amount_input.send_keys(Keys.RETURN)

    def reload_to_empty_cart(self):
        cart_data = self.find(cart_lines)
        self.wait_until_reload(cart_data)
