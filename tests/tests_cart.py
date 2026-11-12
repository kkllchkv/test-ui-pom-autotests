def test_empty_cart(desk_cart_page):
    desk_cart_page.open_page()
    desk_cart_page.assert_empty_cart()


def test_change_amount_at_cart(desk_cart_page, prepare_cart):
    desk_cart_page.open_page()
    desk_cart_page.increase_amount_by_one()

    desk_cart_page.assert_amount(target_amount='2')


def test_change_amount_to_zero(desk_cart_page, prepare_cart):
    desk_cart_page.open_page()
    desk_cart_page.clear_amount_text()
    desk_cart_page.manual_change_amount(amount='0')

    desk_cart_page.reload_to_empty_cart()
    desk_cart_page.assert_empty_cart()
