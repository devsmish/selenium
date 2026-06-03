BASE_URL = "http://5.101.50.27:8000"

# Autorization
USERNAME = "harrypotter" # "flash"
PASSWORD = "expelliarmus" # "test"

# Company
NEW_COMPANY_PAYLOAD = {
    "name": "QA Company",
    "description": "Temporary test company"
}

UPDATE_COMPANY_PAYLOAD = {
    "name": "QA update",
    "description": "Updated test company"
}

UPDATE_COMPANY_STATUS_PAYLOAD = {
    "is_active": True
}

# Employee
NEW_EMPLOYEE_PAYLOAD = {
    "first_name": "Frank",
    "last_name": "Erst",
    "middle_name": "vnaorvich",
    "email": "autoqa_worker@ukr.net",
    "phone": "+4901234567890",
    "birthdate": "2005-06-03",
    "is_active": True
}

UPDATE_EMPLOYEE_PAYLOAD = {
    "last_name": "Groß",
    "email": "autoqa_worker@ukr.net",
    "phone": "+4901234567890",
    "is_active": False
}
