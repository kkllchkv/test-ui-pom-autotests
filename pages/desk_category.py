from locators.desk_category import (inactive_steel_legs_checkbox, active_steel_legs_checkbox,
                                    product_cards, search_input, price_range_right_thumb_parent,
                                    price_range_right_thumb, dynamic_price, product_cards_prices)
from pages.base_page import BasePage


class DeskCategory(BasePage):
    page_path = '/shop/category/desks-1'

    def find_steel_checkbox(self):
        return self.find(inactive_steel_legs_checkbox)

    def wait_for_active_checkbox(self):
        self.wait_for_element_to_appear(active_steel_legs_checkbox)

    def find_all_product_cards(self):
        return self.find_all(product_cards)

    def find_search_input(self):
        return self.find(search_input)

    def drag_right_thumb(self, target_price: float):
        """метод двигает тумблер до нужного диапазона"""
        target_price = target_price
        if not isinstance(target_price, float):
            raise TypeError(f'Target price must be a float. Got {type(target_price)} instead')

        in_range = False

        while not in_range:
            thumb_parent = self.find(price_range_right_thumb_parent)
            thumb_shadow_root = thumb_parent.shadow_root
            thumb = self.find_at_shadow_root(thumb_shadow_root, price_range_right_thumb)
            self.actions.move_to_element(thumb).click_and_hold().move_by_offset(-50, 0).release().perform()
            raw_thumb_price = self.find(dynamic_price).text
            thumb_price_normalized = float(raw_thumb_price.replace(',', '').lstrip('$ '))
            in_range = self.check_if_is_in_range("right", thumb_price_normalized, target_price)

    def check_if_is_in_range(self, tumbler_position, current_point, goal_point):
        """проверка входа позиции тумблера в нужный диапазон"""
        match tumbler_position:
            case "right":
                # двигаемся справа налево
                if current_point > goal_point:
                    return False
                else:
                    return True
            case "left":
                # двигаемся слева направо
                if current_point < goal_point:
                    return False
                else:
                    return True
            case _:
                raise ValueError('Недопустимая позиция для тумблера. '
                                 'Допустимы:"right" или "left"')

    def get_product_card_processed_prices(self):
        prices = self.find_all(product_cards_prices)
        assert len(prices) > 0, "couldn't find any product card prices"

        return [float(price.text) for price in prices]
