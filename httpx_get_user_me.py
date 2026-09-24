import httpx

# Данные для входа в систему
login_payload = {
    "email": "test@mail.ru",
    "password": "123"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

headers = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(response.status_code)
print(response.json())

