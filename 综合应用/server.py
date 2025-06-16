import socket
import threading

clients = {}  # 存储客户端信息 {用户名: 客户端套接字}

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.startswith("/list"):
                # 返回在线用户列表
                online_users = ", ".join(clients.keys())
                client_socket.send(f"在线用户: {online_users}".encode())
            elif message.startswith("/msg"):
                # 处理私信
                _, target_user, msg = message.split(" ", 2)
                if target_user in clients:
                    clients[target_user].send(f"{username} 说: {msg}".encode())
                else:
                    client_socket.send(f"用户 {target_user} 不在线".encode())
            else:
                client_socket.send("无效命令".encode())
        except:
            break

    client_socket.close()
    del clients[username]
    print(f"{username} 已下线")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(5)
    print("服务器已启动，等待客户端连接...")

    while True:
        client_socket, addr = server_socket.accept()
        username = client_socket.recv(1024).decode()
        clients[username] = client_socket
        print(f"{username} 已连接，地址: {addr}")

        thread = threading.Thread(target=handle_client, args=(client_socket, username))
        thread.start()

if __name__ == "__main__":
    main()
