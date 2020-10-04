import socket

class server_class :
    def build_listen(self):
        # 监听端口
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.1',9999))
        server_socket.listen(5)

        while True:
            # 接收客户端连接
            client_socket, addr = server_socket.accept()
            # 接收客户端信息
            msg = client_socket.recv(1024).decode("utf-8")
            print(f"receive msg from client {addr}：{msg}")
            # 向客户端发送信息
            msg = f"yes , you have client_socketect with server.\r\n".encode("utf-8")
            client_socket.send(msg)
            client_socket.close()



if __name__ == "__main__":
    server = server_class()
    server.build_listen()