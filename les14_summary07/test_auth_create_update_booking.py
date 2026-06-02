def test_create_booking(api):
    booking_id = api.create_booking()
    assert booking_id is not None, "ID брони не должен быть пустым"
    assert isinstance(booking_id, int), "ID брони должен быть числом"

def test_update_booking(api, booking_id, token):
    updated_booking = api.update_booking(booking_id, token)

    assert updated_booking["totalprice"] == 340, "Цена не обновилась"
    assert updated_booking["additionalneeds"] == "Late Checkout", "Доп. требования не обновились"
