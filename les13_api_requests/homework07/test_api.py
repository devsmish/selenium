import pytest
import constants


def test_employee_full_lifecycle(api, auth_token):
    companies_res_before = api.get_company_list()
    assert companies_res_before.status_code == 200, "Не удалось получить список компаний"

    companies_before = companies_res_before.json()
    max_id_before = max([c.get('id') for c in companies_before if c.get('id') is not None], default=0)

    create_company_res = api.create_company(constants.NEW_COMPANY_PAYLOAD)
    assert create_company_res.status_code == 201, "Сервер отклонил создание компании"

    companies_res_after = api.get_company_list()
    assert companies_res_after.status_code == 200

    companies_after = companies_res_after.json()
    new_company_id = max([c['id'] for c in companies_after])

    assert new_company_id > max_id_before, "ID новой компании не превышает предыдущий максимум"

    employee_payload = constants.NEW_EMPLOYEE_PAYLOAD.copy()
    employee_payload["company_id"] = new_company_id

    create_emp_res = api.create_employee(employee_payload)
    assert create_emp_res.status_code == 201, "Не удалось создать сотрудника"

    emp_list_res = api.get_employee_list(new_company_id)
    assert emp_list_res.status_code == 200, "Ошибка при запросе списка сотрудников компании"

    employee_list = emp_list_res.json()

    if not employee_list:
        raise ValueError(f"Ошибка логики: Компания с ID {new_company_id} пуста после добавления сотрудника!")

    assert len(employee_list) == 1, "В изолированной тест-компании должен находиться ровно один сотрудник"

    target_employee_id = employee_list[0]['id']

    emp_info_res = api.get_employee_info(target_employee_id)
    assert emp_info_res.status_code == 200, "Не удалось получить карточку сотрудника"
    assert emp_info_res.json()['first_name'] == constants.NEW_EMPLOYEE_PAYLOAD['first_name']

    patch_res = api.update_employee(target_employee_id, auth_token, constants.UPDATE_EMPLOYEE_PAYLOAD)
    assert patch_res.status_code == 200, "Сервер вернул ошибку при попытке изменить фамилию сотрудника"

    final_info_res = api.get_employee_info(target_employee_id)
    assert final_info_res.status_code == 200

    final_data = final_info_res.json()
    assert final_data['last_name'] == constants.UPDATE_EMPLOYEE_PAYLOAD['last_name'], "Фамилия не обновилась"
