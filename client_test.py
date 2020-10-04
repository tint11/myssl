import socket

class client_class:
    def send_hello(self):
        # 与服务端建立连接
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1',9999))

        # 向服务端发送消息
        msg = "do i connect with server ?".encode("utf-8")
        client_socket.send(msg)
        # 接收服务端返回的消息
        msg = client_socket.recv(1024).decode('utf-8')
        print(f"receive msg from server : {msg}")
        client_socket.close()

if __name__ == "__main__":
    client = client_class()
    client.send_hello()