import httpx

from tools.fakers import fake

base_url = "http://localhost:8000/api/v1"

create_user_payload = {
    "email": fake.email(),
    "password": "passw12345",
    "firstName": "Ralf",
    "lastName": "Stinger",
    "middleName": "Musa"
}

create_user_response = httpx.post(f"{base_url}/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(f"Create user data: {create_user_response_data}")

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


create_file_headers = {"Authorization": f"Bearer {access_token}"}

create_file_response = httpx.post(
    f"{base_url}/files",
    data={"filename": "test.jpg", "directory": "courses"},
    files={"upload_file": open("./testdata/files/test.jpg", "rb")},
    headers=create_file_headers
)

create_file_response_data = create_file_response.json()
print(f"Create file data: {create_file_response_data}")


