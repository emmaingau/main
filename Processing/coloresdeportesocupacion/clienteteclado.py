import socket
import time
import numpy
import random
import keyboard

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1243))
s.connect(("127.0.0.1", 1243))

#colores = ["terracota", "cian", "magenta", "lila", "mostaza", "verde agua", "verde", "amarillo", "azul", "rojo"]
colores = ["negro", "blanco", "rojo", "verde", "azul", "marrón"]
deportes = ["fútbol", "tenis", "badminton", "processing", "cricket", "rugby", "hockey", "balonmano", "basquetbol", "beisbol"]
ocupaciones = ["estudio", "trabajo"]

while True:
    try:
        if keyboard.is_pressed('page down'):
            selector = random.randint(0,5)
            time.sleep(0.1)
            deporte = deportes[selector]
            print(deporte)
            s.send(deporte.encode())
        if keyboard.is_pressed('page up'):
            selector = random.randint(0,5)
            time.sleep(0.1)
            color = colores[selector]
            print(color)
            s.send(color.encode())
        if keyboard.is_pressed('esc'):
            selector = random.randint(0,1)
            time.sleep(0.1)
            ocupacion = ocupaciones[selector]
            print(ocupacion)
            s.send(ocupacion.encode())
        else:
            pass
    except:
        break