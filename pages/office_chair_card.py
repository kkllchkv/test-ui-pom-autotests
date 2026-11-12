from locators.office_chair_card import (card_add_to_cart_button,
                                        successful_add_to_cart_tag,
                                        added_product_and_amount_tag, remove_one_button, selected_quantity,
                                        terms_and_conditions_link)
from pages.base_page import BasePage


class OfficeChairCard(BasePage):
    page_path = '/shop/furn-7777-office-chair-5'

    def add_to_cart(self):
        add_to_cart = self.find(card_add_to_cart_button)
        add_to_cart.click()

    def assert_successful_add_to_cart(self):
        self.wait_for_element_to_appear(successful_add_to_cart_tag)
        add_to_cart_text = self.find(successful_add_to_cart_tag).text

        assert add_to_cart_text == 'Item(s) added to your cart', \
            f"Toast text did not match: {add_to_cart_text}"

    def assert_amount_add_to_cart(self, amount):
        self.wait_for_element_to_appear(added_product_and_amount_tag)
        amount_text = self.find(added_product_and_amount_tag).text

        assert amount_text == f'{amount} x Office Chair',\
            f'Toast text did not match: {amount_text}'

    def decrease_amount_by_one(self):
        self.find(remove_one_button).click()

    def assert_selected_quantity(self, expected_quantity):
        quantity_element = self.find(selected_quantity)
        quantity = quantity_element.get_attribute('value')
        assert quantity == expected_quantity, \
            f"Selected quantity didn't match expected quantity and = '{quantity}'"

    def open_terms_and_conditions(self):
        self.find(terms_and_conditions_link).click()
        self.assure_page_has_loaded(expected_path='/terms')