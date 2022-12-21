import socket
import threading
import board
from gpiozero import LED
import adafruit_dht

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10451))



def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
            if message == '1':
                ligar_lampadas_sala1()
            elif message == '2':
                desligar_lampadas_sala1()
            elif message == '3':
                ligar_lampadas_sala2()
            elif message == '4':
                desligar_lampadas_sala2()
            elif message == '5':
                estados_da_sala_1()
            elif message == '6':
                estados_da_sala_2()
        except:
            print('Error!')
            client.close()
            break

def ligar_lampadas_sala1():
    led = LED(18)
    led.on()
    led = LED(23)
    led.on()
    print(led.value)

def desligar_lampadas_sala1():
    led = LED(18)
    led.off()
    led = LED(23)
    led.off()
    print('desligar_lampada')

def ligar_lampadas_sala2():
    led = LED(26)
    led.on()
    led = LED(19)
    led.on()
    print(led.value)

def desligar_lampadas_sala2():
    led = LED(26)
    led.off()
    led = LED(19)
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

    mensagem = ('Lâmpada 01 da Sala ' + led_1 + '\nLâmpada 02 da Sala ' + led_2+ '\nAr-Condicionado '+ led_3 +'\nProjetor Multimídia ' + led_4)
    client.send(mensagem.encode('utf-8')) 

    try:
        dhtDevice = adafruit_dht.DHT22(board.D4)
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        mensagem = ('Temperatura: ' + str(temperature_c) + 'C' + '\nUmidade: ' + str(humidity) + '%')
        client.send(mensagem.encode('utf-8'))
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

    mensagem = ('Lâmpada 01 da Sala ' + led_1 + '\nLâmpada 02 da Sala ' + led_2+ '\nAr-Condicionado '+ led_3 +'\nProjetor Multimídia ' + led_4)
    client.send(mensagem.encode('utf-8')) 

    try:
        dhtDevice = adafruit_dht.DHT22(board.D4)
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        mensagem = ('Temperatura: ' + str(temperature_c) + 'C' + '\nUmidade: ' + str(humidity) + '%')
        client.send(mensagem.encode('utf-8'))
    except:
        print('Erro ao ler os sensores de temperatura e umidade')

def client_send():
    while True:
        message = input()
        client.send(message.encode('utf-8'))





receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()