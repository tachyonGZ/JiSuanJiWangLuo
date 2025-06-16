import socket
import threading

def handle_client(client_socket, client_address):
    print(f"客户端 {client_address} 已连接")
    while True:
        try:
            # 接收数据
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"收到来自 {client_address} 的消息：{message.decode()}")
            # 发送响应
            response = f"服务端已收到：{message.decode()}"
            client_socket.send(response.encode())
        except ConnectionResetError:
            break
    print(f"客户端 {client_address} 断开连接")
    client_socket.close()

def main():
    # 创建TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 8888)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("TCP服务端已启动，等待客户端连接...")

    while True:
        client_socket, client_address = server_socket.accept()
        # 为每个客户端连接创建新线程
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()