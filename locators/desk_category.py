from selenium.webdriver.common.by import By

# родитель для правого ползунка смены ценового диапозона
price_range_right_thumb_parent = (By.CSS_SELECTOR, '.range-with-input.ghost')

# правый ползунок смены ценового диапозона. находится в shadow root
price_range_right_thumb = (By.CSS_SELECTOR, '#thumb')

# элемент, в котором хранится динамическая цена ползунка
dynamic_price = (By.CSS_SELECTOR, '.multirange-max.position-absolute')

# все цены карточек товаров на странице
product_cards_prices = (By.CSS_SELECTOR, '.oe_currency_value')

# неактивированный чекбокс для выбора материала "Сталь"
inactive_steel_legs_checkbox = (By.CSS_SELECTOR, '[value="1-1"]')

# активированныйчекбокс для выбора материала "Сталь"
active_steel_legs_checkbox = (By.CSS_SELECTOR, '[value="1-1"][checked="checked"]')

# все существующие на странице карточки товара
product_cards = (By.CSS_SELECTOR, '.oe_product')

# строка поиска
search_input = (By.CSS_SELECTOR, '#products_grid [type="search"]')
