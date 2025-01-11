import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            message = input("Введите сообщение (напишите 'exit' для выхода): ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Ответ от сервера: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client("127.0.0.1", 60000)
