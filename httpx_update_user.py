import httpx

from tools.fakers import get_random_email

base_url = "http://localhost:8000/api/v1"

create_user_payload = {
    "email": get_random_email(),
    "password": "passw12345",
    "firstName": "Ralf",
    "lastName": "Stinger",
    "middleName": "Musa"
}

create_user_response = httpx.post(f"{base_url}/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(f"Create user data: {create_user_response_data}")
print(f"Create user response status code: {create_user_response.status_code}")


user_id = create_user_response_data["user"]["id"]

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}


login_response = httpx.post(f"{base_url}/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(f"Login data: {login_response_data}")
print(f"Login response status code: {login_response.status_code}")

access_token = login_response_data["token"]["accessToken"]


headers = {"Authorization": f"Bearer {access_token}"}

update_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}


update_user_response = httpx.patch(f"{base_url}/users/{user_id}", headers=headers, json=update_user_payload)
update_user_response_data = update_user_response.json()

print(f"Update user data: {update_user_response_data}")
print(f"Update user response status code: {update_user_response.status_code}")
