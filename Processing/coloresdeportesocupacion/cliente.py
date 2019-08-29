import socket
import time
import numpy
import random

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1243))
s.connect(("127.0.0.1", 1243))

colores = ["terracota", "cian", "magenta", "lila", "mostaza", "verde agua", "verde", "amarillo", "azul", "rojo"]
deportes = ["fútbol", "tenis", "badminton", "processing", "cricket", "rugby", "hockey", "balonmano", "basquetbol", "beisbol"]

while True:
    msg = str(random.randint(1,2))
    selector = random.randint(0,9)
    print(msg)
    if (msg == str(1)):
        deporte = deportes[selector]
        time.sleep(0.2)
        s.send(deporte.encode())
    else:
        color = colores[selector]
        time.sleep(0.2)
        s.send(color.encode())