import requests

class XClientsAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        payload = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/auth/login", json=payload)
        return response.json().get("user_token")

    def create_company(self, payload):
        return requests.post(f"{self.base_url}/company/create", json=payload)

    def get_company_list(self):
        return requests.get(f"{self.base_url}/company/list")

    def create_employee(self, payload):
        return requests.post(f"{self.base_url}/employee/create", json=payload)

    def get_employee_list(self, company_id):
        return requests.get(f"{self.base_url}/employee/list/{company_id}")

    def get_employee_info(self, employee_id):
        return requests.get(f"{self.base_url}/employee/info/{employee_id}")

    def update_employee(self, employee_id, token, payload):
        params = {"client_token": token}
        return requests.patch(
            f"{self.base_url}/employee/change/{employee_id}",
            json=payload,
            params=params
        )

    def find_employee_id_by_email(self, target_email, start_id=1):
        possible_id = start_id
        consecutive_empty = 0

        while consecutive_empty < 3:
            response = self.get_employee_info(possible_id)

            if response.status_code == 200:
                consecutive_empty = 0
                data = response.json()
                if data.get("email") == target_email:
                    return possible_id
            else:
                consecutive_empty += 1

            possible_id += 1

        raise RuntimeError(
            f"Не удалось найти сотрудника с email {target_email}. "
            f"Поиск остановлен на ID {possible_id}, так как получено 3 пустых ответа подряд."
        )
