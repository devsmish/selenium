import constants
import time
import random


def test_create_employee_success(api, clean_company_id):
    employee_payload = constants.NEW_EMPLOYEE_PAYLOAD.copy()
    employee_payload["company_id"] = clean_company_id

    unique_email = f"qa_{int(time.time())}_{random.randint(1000, 9999)}_{constants.NEW_EMPLOYEE_PAYLOAD['email']}"
    employee_payload["email"] = unique_email

    response = api.create_employee(employee_payload)
    assert response.status_code in [200], f"Ошибка создания сотрудника: {response.text}"


def test_get_employee_info_by_id(api, clean_employee_id):
    info_response = api.get_employee_info(clean_employee_id)

    assert info_response.status_code == 200
    assert info_response.json()['first_name'] == constants.NEW_EMPLOYEE_PAYLOAD['first_name']


def test_update_employee_info(api, clean_employee_id, auth_token):
    patch_response = api.update_employee(clean_employee_id, auth_token, constants.UPDATE_EMPLOYEE_PAYLOAD)
    assert patch_response.status_code == 200, f"Ошибка изменения данных: {patch_response.text}"

    final_info = api.get_employee_info(clean_employee_id).json()
    assert final_info['last_name'] == constants.UPDATE_EMPLOYEE_PAYLOAD['last_name'], "Фамилия не изменилась"
