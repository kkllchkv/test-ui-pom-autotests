def test_steel_checkbox(desk_category_page):
    # тест нажимает чекбокс и убеждается, что после фильтрации остался 1 элемент
    desk_category_page.open_page()
    desk_category_page.wait_until_window_is_ready()

    checkbox = desk_category_page.find_steel_checkbox()
    checkbox.click()
    desk_category_page.wait_for_active_checkbox()

    product_cards = desk_category_page.find_all_product_cards()
    desk_category_page.assert_len(product_cards, 1)


def test_search_input(desk_category_page):
    # тест проверяет отстутвие лишних КТ после фильтрации по тексту
    desk_category_page.open_page()
    desk_category_page.wait_until_window_is_ready()

    search_input = desk_category_page.find_search_input()
    search_word = "Desk"
    search_input.send_keys(search_word)
    search_input.submit()
    product_cards = desk_category_page.find_all_product_cards()

    desk_category_page.assert_elements_text(search_word, product_cards)


def test_drag_price_thumb(desk_category_page):
    desk_category_page.open_page()
    desk_category_page.wait_until_window_is_ready()
    target_price = 2000.00

    desk_category_page.drag_right_thumb(target_price=target_price)

    product_cards_prices = desk_category_page.get_product_card_processed_prices()
    desk_category_page.assert_price_less(target_price, product_cards_prices)
