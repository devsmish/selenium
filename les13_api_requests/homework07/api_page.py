import requests

class XClientsAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    # ---------------- AUTH METHODS ----------------
    def login(self, username, password):
        payload = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/auth/login", json=payload)
        print("\nAutorization response:", response.status_code, response.text)
        return response.json().get("user_token")

    # ---------------- COMPANY METHODS ----------------
    def get_company_list(self):
        return requests.get(f"{self.base_url}/company/list")

    def get_company_by_id(self, company_id):
        return requests.get(f"{self.base_url}/company/{company_id}")

    def create_company(self, payload):
        return requests.post(f"{self.base_url}/company/create", json=payload)

    def update_company(self, company_id, payload):
        return requests.patch(f"{self.base_url}/company/update/{company_id}", json=payload)

    def update_company_status(self, company_id, payload):
        return requests.patch(f"{self.base_url}/company/status_update/{company_id}", json=payload)

    def delete_company(self, company_id):
        return requests.delete(f"{self.base_url}/company/{company_id}")

    # ---------------- EMPLOYEE METHODS ----------------
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

    # ---------------- SUPERUSER METHODS ----------------
    def full_refresh(self):
        return requests.get(f"{self.base_url}/magic/delete_create_all")
