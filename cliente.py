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
                ligar_lampada()
            elif message == '2':
                desligar_lampada()
            elif message == '3':
                estados_da_sala_1()
            elif message == '4':
                estados_da_sala_2()
        except:
            print('Error!')
            client.close()
            break

def ligar_lampada():
    led = LED(19)
    led.on()
    print('ligar_lampada')
    print(led.value)

def desligar_lampada():
    led = LED(19)
    led.off()
    print('desligar_lampada')

def estados_da_sala_1():
    led = LED(18)
    led_1 = led.value
    led = LED(23)
    led_2 = led.value
    led = LED(24)
    led_3 = led.value
    led = LED(25)
    led_4 = led.value
    print(led_1,led_2,led_3,led_4)

def estados_da_sala_2():
    print('estados da lampada')

def client_send():
    while True:
        message = input()
        client.send(message.encode('utf-8'))





receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()