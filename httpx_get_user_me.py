import httpx


base_url = "http://localhost:8000/api/v1"
login_payload = {"email": "nye@example.com", "password": "passw12345"}


login_response = httpx.post(f"{base_url}/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(f"Response data: {login_response_data}")
print(f"Response status code: {login_response.status_code}")

access_token = login_response_data["token"]["accessToken"]


profile_response = httpx.get(f"{base_url}/users/me", headers={"Authorization": f"Bearer {access_token}"})
profile_response_data = profile_response.json()

print(f"Profile response data: {profile_response_data}")
print(f"Profile response status code: {profile_response.status_code}")
