import pytest
from constants import BASE_URL, USERNAME, PASSWORD
from api_page import XClientsAPI

@pytest.fixture(scope="session")
def api():
    return XClientsAPI(BASE_URL)

@pytest.fixture(scope="session")
def auth_token(api):
    return api.login(USERNAME, PASSWORD)
