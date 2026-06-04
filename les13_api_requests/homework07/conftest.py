import pytest
import constants
import time
import random
from api_page import XClientsAPI


@pytest.fixture(scope="session")
def api():
    return XClientsAPI(constants.BASE_URL)


@pytest.fixture(scope="session")
def auth_token(api):
    return api.login(constants.USERNAME, constants.PASSWORD)


@pytest.fixture(scope="session")
def clean_company_id(api):
    response = api.create_company(constants.NEW_COMPANY_PAYLOAD)
    assert response.status_code == 201, f"Не удалось создать компанию: {response.text}"
    return response.json().get("id")


@pytest.fixture(scope="session")
def clean_employee_id(api, clean_company_id):
    employee_payload = constants.NEW_EMPLOYEE_PAYLOAD.copy()
    employee_payload["company_id"] = clean_company_id
    unique_email = f"qa_{int(time.time())}_{random.randint(1000, 9999)}_{constants.NEW_EMPLOYEE_PAYLOAD['email']}"
    employee_payload["email"] = unique_email
    api.create_employee(employee_payload)
    target_id = api.find_employee_id_by_email(unique_email)
    return target_id
