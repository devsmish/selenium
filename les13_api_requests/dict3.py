import json

invalid_json = "{ 'id': 111, 'name': 'Test Company' }"  # Неправильные одинарные кавычки

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Ошибка при разборе JSON: {e}")
