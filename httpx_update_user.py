import httpx

from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)
print(create_user_response.status_code)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)
print(login_response.status_code)

update_user_payload = {
    "email": get_random_email(),
    "password": "string1",
    "lastName": "string1",
    "firstName": "string1",
    "middleName": "string1"
}

user_id = create_user_response_data["user"]["id"]

access_token = login_response_data["token"]["accessToken"]

update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}",
                                   json=update_user_payload,
                                   headers={"Authorization": f"Bearer {access_token}"})

update_user_response_data = update_user_response.json()
print('Update data:', update_user_response_data)
print(update_user_response.status_code)