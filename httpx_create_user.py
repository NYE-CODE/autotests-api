import httpx

from tools.fakers import get_random_email

base_url = "http://localhost:8000/api/v1"

payload = {
    "email": get_random_email(),
    "password": "passw12345",
    "firstName": "Ralf",
    "lastName": "Stinger",
    "middleName": "Musa"
}

response_create_user = httpx.post(f"{base_url}/users", json=payload)
response_create_user_data = response_create_user.json()

print(f"Response data: {response_create_user_data}")
print(f"Response status code: {response_create_user.status_code}")