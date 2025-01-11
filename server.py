import socket
import threading

def handle_client(server_socket, clients):
    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        if addr not in clients:
            clients.add(addr)
        if message.lower() == "exit":
            clients.remove(addr)
            continue
        for client in clients:
            if client != addr:
                server_socket.sendto(f"[{addr}] {message}".encode(), client)

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Сервер запущен на {host}:{port}")
    clients = set()
    threading.Thread(target=handle_client, args=(server_socket, clients), daemon=True).start()
    while True:
        command = input()
        if command.lower() == "stop":
            break
    server_socket.close()
    print("Сервер остановлен")

if __name__ == "__main__":
    start_server("127.0.0.1", 60000)
