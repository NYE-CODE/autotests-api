import httpx


login_payload = {"email": "nye@example.com", "password": "passw12345"}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(f"Response data: {login_response_data}")
print(f"Response status code: {login_response.status_code}")

access_token = login_response_data["token"]["accessToken"]


client = httpx.Client(
    base_url="http://localhost:8000/api/v1",
    headers={"Authorization": f"Bearer {access_token}"}
)


profile_response = client.get("/users/me")
profile_response_data = profile_response.json()

print(f"Profile response data: {profile_response_data}")
print(f"Profile response status code: {profile_response.status_code}")
