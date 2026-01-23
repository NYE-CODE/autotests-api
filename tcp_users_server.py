import socket



def server():
    message_array = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print('Сервер запущен и ждет подключения...')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        message_array.append(data)

        response = f"Пользователь с адресом: {client_address} отправил сообщение: {message_array}"
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == '__main__':
    server()