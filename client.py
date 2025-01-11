import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data, _ = client_socket.recvfrom(1024)
            print(data.decode())
        except:
            break

def start_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setblocking(False)
    server_address = (server_host, server_port)

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    try:
        while True:
            message = input()
            if message.lower() == "exit":
                client_socket.sendto(message.encode(), server_address)
                break
            client_socket.sendto(message.encode(), server_address)
    finally:
        client_socket.close()
        print("Клиент завершил работу")

if __name__ == "__main__":
    start_client("127.0.0.1", 60000)
