import pytest
import requests
import qase  # Swapped from 'import allure'

from booker_api import BookerApi

base_url = "https://restful-booker.herokuapp.com"
api = BookerApi(base_url)

# Note: In Qase, IDs are integers matching your Qase repository case IDs
@qase.id(2)
@qase.title("авторизация")
def test_authentication():
    api.authenticate()


# @qase.id()
# @qase.title("получение всех броней")
# @pytest.mark.skip(reason="Skipping for demo")
# def test_get_booking_ids():
#     api.get_booking_ids()


@qase.id(3)
@qase.title("создание брони")
def test_create_booking():
    booking = {
        "firstname": "Roman",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    resp = api.create_booking(booking)
    assert resp["bookingid"] != "", "Нет id"


@qase.id(4)
@qase.title("получение брони по id")
def test_get_booking():
    with qase.step("step one — generate test data"):
        booking = {
            "firstname": "Rom",
            "lastname": "White",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    with qase.step(f"step three — verify booking with {booking_id}"):
        resp = api.get_booking(booking_id)
        assert resp["firstname"] == "Roman"


@qase.id(5)
@qase.title("полное обновление брони (PUT)")
def test_update_booking():
    token = api.authenticate()

    with qase.step("step one — generate test data"):
        booking = {
            "firstname": "Tom",
            "lastname": "Smith",
            "totalprice": 150,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-01-01",
                "checkout": "2023-01-10"
            },
            "additionalneeds": "Dinner"
        }

    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    updated_booking = {
        "firstname": "Tommy",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-02",
            "checkout": "2023-01-12"
        },
        "additionalneeds": "Lunch"
    }

    updated_resp = api.update_booking(booking_id, updated_booking, token)

    assert updated_resp["firstname"] == "Tommy", "Имя не обновилось"
    assert updated_resp["totalprice"] == 200, "Цена не обновилась"
    assert updated_resp["depositpaid"] is False, "Статус депозита не обновился"


@qase.id(6)
@qase.title("частичное обновление брони (PATCH)")
@qase.comment("Привет, ITCH!") # Used comment instead of allure.description
def test_patch_booking():
    token = api.authenticate()

    booking = {
        "firstname": "Anna",
        "lastname": "Taylor",
        "totalprice": 300,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-05-01",
            "checkout": "2023-05-10"
        },
        "additionalneeds": "Dinner"
    }
    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    patch_data = {
        "firstname": "Anastasia",
        "lastname": "Ivanova"
    }

    patched_resp = api.patch_booking(booking_id, patch_data, token)

    assert patched_resp["firstname"] == "Anastasia", "Имя не обновилось"
    assert patched_resp["lastname"] == "Ivanova", "Фамилия не обновилась"
    assert patched_resp["totalprice"] == 300, "Цена не должна была измениться"


@qase.id(7)
@qase.title("удаление бронирования (DELETE)")
# For tickets/features, Qase uses fields. You can also append them to ignore or track execution tracking.
def test_delete_booking():
    token = api.authenticate()

    booking = {
        "firstname": "DeleteMe",
        "lastname": "Now",
        "totalprice": 123,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2022-10-01",
            "checkout": "2022-10-05"
        },
        "additionalneeds": "None"
    }
    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    result = api.delete_booking(booking_id, token)
    assert result is True, "Удаление не удалось"

    resp = requests.get(f"{api.url}/booking/{booking_id}")
    assert resp.status_code == 404, "Бронирование не удалено (ожидался 404)"