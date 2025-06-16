import socket

def main():
    # 创建TCP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 8888)
    client_socket.connect(server_address)

    try:
        while True:
            message = input("请输入要发送的消息（输入exit退出）：")
            if message.lower() == 'exit':
                break
            # 发送数据
            client_socket.send(message.encode())
            # 接收响应
            response = client_socket.recv(1024)
            print(f"收到服务端回复：{response.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
