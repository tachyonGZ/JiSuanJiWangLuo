# server.py

import socket

# 1. 创建UDP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('0.0.0.0', 8888)
server_socket.bind(server_address)
print("UDP服务端已启动，等待客户端消息...")

while True:
    # 2. 接收数据
    data, client_addr = server_socket.recvfrom(1024)
    print(f"收到来自{client_addr}的消息：{data.decode()}")
    # 3. 处理并响应
    response = f"服务端已收到：{data.decode()}"
    server_socket.sendto(response.encode(), client_addr)