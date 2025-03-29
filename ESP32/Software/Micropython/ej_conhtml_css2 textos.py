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
<!DOCTYPE html>
<html>
<head>
    <title>ESP32 Text Input</title>
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
    <form action="/submit1" method="post">
        <input type="text" name="input_text1">
        <input type="submit" value="Enviar Texto 1">
    </form>
    <br>
    <h1>Ingrese otro texto</h1>
    <form action="/submit2" method="post">
        <input type="text" name="input_text2">
        <input type="submit" value="Enviar Texto 2">
    </form>
</body>
</html>
"""

# Crear un servidor web
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('Servidor web iniciado en:', addr)

def handle_request(conn):
    global received_text1, received_text2
    request = conn.recv(1024)
    request = request.decode('utf-8')
    
    print('Solicitud:')
    print(request)

    # Manejar solicitudes POST para el primer input
    if 'POST /submit1' in request:
        content_length = int(request.split('Content-Length: ')[1].split('\r\n')[0])
        body = request.split('\r\n\r\n')[1]
        if 'input_text1=' in body:
            received_text1 = body.split('input_text1=')[1]
            received_text1 = received_text1.replace('+', ' ')
            print("Texto recibido 1:", received_text1)
    
    # Manejar solicitudes POST para el segundo input
    if 'POST /submit2' in request:
        content_length = int(request.split('Content-Length: ')[1].split('\r\n')[0])
        body = request.split('\r\n\r\n')[1]
        if 'input_text2=' in body:
            received_text2 = body.split('input_text2=')[1]
            received_text2 = received_text2.replace('+', ' ')
            print("Texto recibido 2:", received_text2)
    
    # Enviar la respuesta HTML
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
    conn.send(response)
    conn.close()

received_text1 = ""
received_text2 = ""

while True:
    conn, addr = s.accept()
    print('Conexión desde', addr)
    handle_request(conn)
