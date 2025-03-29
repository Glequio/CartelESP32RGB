import machine
import neopixel
import time
import funcion
import caracter
"""
import network
import socket

# Configuración Wi-Fi
ssid = 'Claro-Fibra-2.4G-1219'
password = '12345678'

# Conectar a la red Wi-Fi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

print('Conectando a WiFi...')
while not station.isconnected():
    pass

print('Conectado a WiFi!')
print('Configuración de red:', station.ifconfig())

# HTML de la página web con CSS
html = """

"""

<!DOCTYPE html>
<html>
<head>
    <title>CARTEL MERCADO ALICIA</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; }
        h1 { color: #333; }
        form { margin-top: 20px; }
        input[type="text"] { padding: 10px; width: 300px; }
        input[type="submit"] { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        input[type="submit"]:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <h1>Ingrese un texto</h1>
    <form action="/" method="post">
        <input type="text" name="input_text">
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
"""

"""

# Crear un servidor web
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('Servidor web iniciado en:', addr)

def handle_request(conn):
    global received_text
    request = conn.recv(1024)
    request = request.decode('utf-8')
    
    print('Solicitud:')
    print(request)

    # Manejar solicitudes POST
    if 'POST' in request:
        content_length = int(request.split('Content-Length: ')[1].split('\r\n')[0])
        body = request.split('\r\n\r\n')[1]
        if 'input_text=' in body:
            received_text = body.split('input_text=')[1]
            received_text = received_text.replace('+', ' ')
            print("Texto recibido:", received_text)
            texto = received_text
    
    # Enviar la respuesta HTML
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
    conn.send(response)
    conn.close()

received_text = ""


"""

#import barrido

# Configuración
pin = 18  # Pin GPIO donde se conecta la matriz LED
ROW = 8
COL = 8
NMATRIZ = 1
ZIGZAG = 1	#Si es 1 matriz zigzag si es 0 barre de izquierda a derecha
SL = 1
num_leds = ROW * COL * NMATRIZ  # Número de LEDs en la matriz
REGLAH = ROW * NMATRIZ


# Inicializar la tira de LEDs
pixel = neopixel.NeoPixel(machine.Pin(pin), num_leds)


def muestraCar(letra,color,px,py):
#    pixel.fill((0,0,0))
    temp = 0
    for i in range(len(caracter.diccionario[letra])):
        temp += 1
        if (i+px)>=0 and (i+px)<COL*NMATRIZ:
            for j in range(ROW):
                if py < 0:
                    if (caracter.diccionario[letra][i] << -py >> (7-j)) & 1:
                        pixel[barr(i+px,j,1)] = color
                else :
                    if(caracter.diccionario[letra][i] >> (7-j+py)) & 1:
                        pixel[barr(i+px,j,1)] = color
#     pixel.write()
    return temp + SL

def clear():
    pixel.fill((0,0,0))
    pixel.write()
    return

def barr(x,y,nmatriz):
    if ZIGZAG:
        if y%2:
            return (COL*(y+1)-1-x)+((nmatriz-1)*COL*ROW)
        return (COL*y+x)+((nmatriz-1)*COL*ROW) 
    return (y*COL+x)+((nmatriz-1)*COL*ROW)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#funcion textshow

# El maximo horizontal del mensaje a mostrar es de ROW x NMATRIZ
# x me marca desde donde arrancamos con el mensaje siendo 0 el primer lugar a la izquierda
# siendo ROW x NMATRIZ - 1 el final horizontal que esta a la derecha del cartel
# la secuencia del texto sería una letra y un espacio de tamaño SL y luego el otro caracter
# defino como paquete al valor formado por el largo del caracter mas el valor de SL
# siguiente al mismo caracter+SL

def textshow(text,x,y,color):
    pixel.fill((0,0,0))
    puntero = x
    n = 0
    while(puntero < REGLAH):
        puntero = puntero + muestraCar(text[n],color,puntero,y)
        n += 1
        if n == len(text):
            break 
    
    
    pixel.write()
    
    return 


color=(50,10,0)
clear()
texto='1234567890 HOLA QUE TAL ESTO ES UN EJEMPLO DE UTILIZACION DEL CARTEL RGB 1234567890'
w=8
# textshow(texto,-7,0,(50,10,0))


while (1):
     conn, addr = s.accept()
     print('Conexión desde', addr)
     handle_request(conn)
#      muestraCar('M',(60,16,0),w,0)
     textshow(texto,w,0,(50,3,0))    
     time.sleep(0.1)
     w -=1
     if w == -(len(texto)*5):
         w = 8
    



# time.sleep(2)
# pixel[8]=(0,10,0)
# pixel.write()
# p1 = barr(4,1,1)
# p2 = barr(4,4,1)
# pixel[p1]=(0,0,50)
# pixel[p2]=(10,0,5)
# pixel.write()
# print("0%2:",0%2)
# print("1%2:",1%2)
# print(caracter.diccionario['2'])