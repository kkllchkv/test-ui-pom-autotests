def test_add_to_cart(office_chair_card):
    office_chair_card.open_page()
    office_chair_card.add_to_cart()
    office_chair_card.assert_successful_add_to_cart()
    office_chair_card.assert_amount_add_to_cart('1')


def test_decrease_one_from_one(office_chair_card):
    office_chair_card.open_page()
    office_chair_card.decrease_amount_by_one()
    office_chair_card.assert_selected_quantity('1')


def test_redirect_to_terms_and_conditions(office_chair_card):
    office_chair_card.open_page()
    office_chair_card.open_terms_and_conditions()
