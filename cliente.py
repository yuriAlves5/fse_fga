import socket
import threading
from gpiozero import LED

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 59000))



def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
            if message == '1':
                estados_da_lampada()
            elif message == '2':
                ligar_lampada()
            elif message == '3':
                desligar_lampada()
        except:
            print('Error!')
            client.close()
            break

def ligar_lampada():
    led = LED(19)
    led.on()
    print('ligar_lampada')

def desligar_lampada():
    led = LED(19)
    led.off()
    print('desligar_lampada')

def estados_da_lampada():
    print('estados da lampada')


def client_send():
    while True:
        message = input()
        client.send(message.encode('utf-8'))





receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()