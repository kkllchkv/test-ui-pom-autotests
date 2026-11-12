from selenium.webdriver.common.by import By

# кнопка на КТ для добавления товара в корзину
add_to_cart_buttons = (By.CSS_SELECTOR, "[title='Shopping cart']")

# кнопка "Continue Shopping" в модальном окне после добавления товара в корзину
continue_shopping_button = (By.CSS_SELECTOR, '.btn.btn-secondary')

# элемент, текст которого содержит кол-во добавленных в корзину товаров
my_cart_quantity_element = (By.CSS_SELECTOR, '.my_cart_quantity')
