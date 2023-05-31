import socket
import threading

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(data)
        print(addr)
        print(f'Received from Client:{addr[1]}', data.decode('utf-8'))


def main():
    host = 'localhost'
    port = 8001

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    

    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()
    
    print("Server Iniciado")


if __name__ == '__main__':
    main()
    
