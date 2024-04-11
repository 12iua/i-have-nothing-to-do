import socket
import threading

def client_handler(client_socket, client_address):
    try:
        username = client_socket.recv(1024).decode('utf-8')
        welcome_message = f"{username} 加入了聊天室！"
        broadcast_message(welcome_message)
        print(welcome_message)

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            broadcast_message(f"{username}: {message}")
    except Exception as e:
        clients.remove(client_socket)
        broadcast_message(f"{username} 离开了聊天室。")
        print(f"{client_address} 离开了聊天室。 Error: {e}")
        client_socket.close()

def broadcast_message(message):
    for client in list(clients):
        try:
            client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error broadcasting message to a client: {e}")
            client.close()
            clients.remove(client)

def main():
    global clients
    clients = set()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 11451))
    server_socket.listen()
    print("服务器启动，等待连接...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            clients.add(client_socket)
            thread = threading.Thread(target=client_handler, args=(client_socket, client_address))
            thread.start()
    except KeyboardInterrupt:
        print("服务器关闭中...")
        for client in list(clients):
            client.close()
        server_socket.close()
        print("服务器已关闭。")

if __name__ == "__main__":
    main()
