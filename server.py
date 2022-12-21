'Chat Room Connection - Client-To-Client'
import threading
import socket
import os
import log


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
        if message == '7':
            os.system('clear')
            print('1 - Ligar lampada 1 sala 1')
            print('2 - Ligar lampada 2 sala 1')
            print('3 - Ligar ar condicionado sala 1')
            print('4 - Ligar projetor sala 1')
            print('5 - Ligar lampada 1 sala 2')
            print('6 - Ligar lampada 2 sala 2')
            print('7 - Ligar ar condicionado sala 2')
            print('8 - Ligar projetor sala 2')
            message = input()
            message = str(int(message) + 70)
            os.system('clear')
            
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
    print('7 - ligar aparelho especifico')

 


def receive():
    while True:
        print('Servidor esta funcionando ...')
        log.logger.info("[i] Server Online")
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
    