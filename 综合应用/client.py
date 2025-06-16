import socket

def main():
    # 连接到服务器
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 8888)
    client_socket.connect(server_address)

    # 注册用户
    username = input("请输入用户名: ")
    client_socket.send(username.encode())

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode()
                print(message)
            except:
                print("连接已断开")
                break

    # 启动接收消息的线程
    import threading
    thread = threading.Thread(target=receive_messages)
    thread.start()

    while True:
        command = input("请输入命令 (/list 查看在线用户, /msg 用户名 消息 发送消息, exit 退出): ")
        if command.lower() == "exit":
            break
        client_socket.send(command.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
