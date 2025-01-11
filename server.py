import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от клиента: {client_address}")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    print(f"Отключение клиента: {client_address}")
                    break
                print(f"Получено сообщение: {data.decode()}")
                client_socket.sendall(data)
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server("127.0.0.1", 60000)
