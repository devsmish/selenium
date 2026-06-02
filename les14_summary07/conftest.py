import pytest
from les14_summary07.api_booking import ApiBooking, BASE_URL, SITE_USER, SITE_PASSWORD


@pytest.fixture(scope="session")
def api():
    return ApiBooking(BASE_URL)

@pytest.fixture(scope="session")
def token(api):
    return api.get_token(SITE_USER, SITE_PASSWORD)

@pytest.fixture()
def booking_id(api):
    return api.create_booking()
