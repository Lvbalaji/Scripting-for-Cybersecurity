import socket
import threading

server_ip="127.0.0.1"
server_port=9998


def main():
    server_scoket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_scoket.bind((server_ip,server_port))
    server_scoket.listen(5)
    print(f"server listening on {server_ip}:{server_port}")
    while True:
        client_socket,addr=server_scoket.accept()
        print(f"Accepted connection from {addr}")
        client_handler=threading.Thread(target=func,args=(client_socket,))
        client_handler.start()

def func(client_socket):
    data=client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    client_socket.send(b"I'm Good")
    client_socket.close()

if __name__=="__main__":
    main()
