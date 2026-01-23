import httpx

#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.json())
#
# data = {
#     "title": "new task",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response.json())
#
#
# data = {
#     "name": "new task",
#     "password": "123456"
# }
#
# response = httpx.post("https://httpbin.org/post", data=data)
# print(response.json())

#
# params = {"userId": 1}
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.json())

# files = {"file": ("example.txt", "rb")}
# response = httpx.post("https://httpbin.org/post", files=files)
# print(response.json())


# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
#     print(response1.json(), response2.json(), sep="\n")


# client = httpx.Client(headers={"User-Agent": "Mozilla/5.0"})
# response = client.get("https://httpbin.org/get")
#
# print(response.json())

# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/todooos")
#     response.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(e)


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")

