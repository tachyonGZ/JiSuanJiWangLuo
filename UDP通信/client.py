#client.py

import socket

# 1. 创建UDP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 8888)

try:
    while True:
        message = input("请输入要发送的消息（输入exit退出）：")
        if message.lower() == 'exit':
            break
        # 2. 发送数据
        client_socket.sendto(message.encode(), server_address)
        # 3. 接收响应
        data, _ = client_socket.recvfrom(1024)
        print(f"收到服务端回复：{data.decode()}")
finally:
    client_socket.close()
