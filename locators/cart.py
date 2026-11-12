from selenium.webdriver.common.by import By

# элемент, который содержит все блоки КТ в корзине (либо отбивку о пустой корзине)
cart_lines = (By.CSS_SELECTOR, '.js_cart_lines')

# кнопка '+' в корзине
increase_amount_by_one_button = (By.CSS_SELECTOR, '[title="Add one"]')

# элемент, который содержит кол-во товара
cart_quantity_element = (By.CSS_SELECTOR, '.js_quantity')
