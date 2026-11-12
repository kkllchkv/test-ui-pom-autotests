from selenium.webdriver.common.by import By

# гиперссылка "Terms and Conditions"
terms_and_conditions_link = (By.CSS_SELECTOR, '[href="/terms"]')

# кнопка добавления товара в корзину
card_add_to_cart_button = (By.CSS_SELECTOR, '#add_to_cart')

# тэг, который содержит текст "Item(s) added to your cart"
successful_add_to_cart_tag = (By.CSS_SELECTOR, 'strong')

# тэг, в котором содержится текст типа "3 x Office Chair"
# кол-во товара + товар, добавленные в корзину
added_product_and_amount_tag = (By.CSS_SELECTOR, '.align-items-start > span')

# кнопка '-' для уменьшения кол-ва товара на 1
remove_one_button = (By.CSS_SELECTOR, '[title="Remove one"]')

# окошко с кол-вом товара для добавления
selected_quantity = (By.CSS_SELECTOR, '.form-control.quantity')
