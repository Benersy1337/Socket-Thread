import socket
import threading

def send_message(sock, host, port):
    while True:
        message = input('Enter message: ')
        sock.sendto(message.encode('utf-8'), (host, port))


def main():
    host = 'localhost'
    port = 8001

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, 8002))

    send_thread = threading.Thread(target=send_message, args=(sock, host, port))
    send_thread.start()

    send_thread.join()


if __name__ == '__main__':
    main()