import socket
import threading
from gpiozero import LED
import Adafruit_DHT

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
    led = LED(18)
    led.on()
    print('ligar_lampada')
    print(led.value)

def desligar_lampada():
    led = LED(18)
    led.off()
    print('desligar_lampada')

def estados_da_sala_1():
    led = LED(18)
    led_1 = led.value
    if(led_1 == 1):
        led_1 = 'Ligado'
    else:
        led_1 = 'Desligado'

    led = LED(23)
    led_2 = led.value
    if(led_2 == 1):
        led_2 = 'Ligado'
    else:
        led_2 = 'Desligado'
    led = LED(24)
    led_3 = led.value
    if(led_3 == 1):
        led_3 = 'Ligado'
    else:
        led_3 = 'Desligado'
    led = LED(25)
    led_4 = led.value
    if(led_4 == 1):
        led_4 = 'Ligado'
    else:
        led_4 = 'Desligado'

    mensagem = ('Lâmpada 01 da Sala ' + led_1 + '\n, Lâmpada 02 da Sala ' + led_2+ '\n, Ar-Condicionado '+ led_3 +'\n, Projetor Multimídia ' + led_4)
    client.send(mensagem.encode('utf-8'))
    try:
        dht = Adafruit_DHT.DHT22
        humidate, temperature = Adafruit_DHT.read_retry(dht, 4)
        print(str(humidate) + ' ' + str(temperature))
    except:
        print('Erro ao ler os sensores de temperatura e umidade')

def estados_da_sala_2():
    led = LED(26)
    led_1 = led.value
    if(led_1 == 1):
        led_1 = 'Ligado'
    else:
        led_1 = 'Desligado'

    led = LED(19)
    led_2 = led.value
    if(led_2 == 1):
        led_2 = 'Ligado'
    else:
        led_2 = 'Desligado'
    led = LED(13)
    led_3 = led.value
    if(led_3 == 1):
        led_3 = 'Ligado'
    else:
        led_3 = 'Desligado'
    led = LED(6)
    led_4 = led.value
    if(led_4 == 1):
        led_4 = 'Ligado'
    else:
        led_4 = 'Desligado'

    mensagem = ('Lâmpada 01 da Sala ' + led_1 + '\n, Lâmpada 02 da Sala ' + led_2+ '\n, Ar-Condicionado '+ led_3 +'\n, Projetor Multimídia ' + led_4)
    client.send(mensagem.encode('utf-8')) 
    
    dht = Adafruit_DHT.DHT22
    humidate, temperature = Adafruit_DHT.read_retry(dht, 18)
    print(str(humidate) + ' ' + str(temperature))

def client_send():
    while True:
        message = input()
        client.send(message.encode('utf-8'))





receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()