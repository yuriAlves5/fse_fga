'Chat Room Connection - Client-To-Client'
import threading
import socket
import os


host = 'localhost'
port = 10451
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()
clients = []


# Function to handle clients'connections


def receiver_server(client):
    while True:
        message = client.recv(1024).decode('utf-8')
        print(f'{message}')

def send_server(client):
    menu()
    while True:
        message = input()
        client.send(message.encode('utf-8'))
        menu()

# Main function to receive the clients connection
def menu():
    os.system('clear')
    print('1 - Ligar lampadas sala 1')
    print('2 - Desligar lampadas sala 1')
    print('3 - Ligar lampadas sala 2')
    print('4 - Desligar lampadas sala 2')
    print('5 - estados da sala 1')
    print('6 - estados da sala 2')
 


def receive():
    while True:
        print('Servidor esta funcionando ...')
        client, address = server.accept()

        print(f'Conexao estabelecida com {str(address)}')

        clients.append(client)
        client.send('you are now connected!'.encode('utf-8'))

        receive_thread = threading.Thread(target=receiver_server, args=(client,))
        receive_thread.start()

        send_thread = threading.Thread(target=send_server, args=(client,))
        send_thread.start()

if __name__ == "__main__":
    receive()
    