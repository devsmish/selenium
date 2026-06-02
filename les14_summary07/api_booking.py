import requests

BASE_URL = 'https://restful-booker.herokuapp.com'
SITE_USER = 'admin'
SITE_PASSWORD = 'password123'


class ApiBooking:

    def __init__(self, url):
        self.url = url if url else BASE_URL

    def get_token(self, user, password):
        creds = {"username": user, "password": password}
        resp = requests.post(self.url + '/auth', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["token"]

    def create_booking(self):
        data = {
            "firstname": "John",
            "lastname": "Snow",
            "totalprice": 520,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-07-02",
                "checkout": "2026-07-04"
            },
            "additionalneeds": "Breakfast"
        }
        resp = requests.post(self.url + '/booking', json=data)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["bookingid"]

    def update_booking(self, booking_id, token):
        data = {
            "firstname": "John",
            "lastname": "Snow",
            "totalprice": 340,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-07-01",
                "checkout": "2026-07-02"
            },
            "additionalneeds": "Late Checkout"
        }

        headers = {
            "Cookie": f"token={token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        resp = requests.put(f"{self.url}/booking/{booking_id}", json=data, headers=headers)
        assert resp.status_code == 200, f"Ошибка PUT: ожидался статус 200, получен {resp.status_code}"
        return resp.json()
