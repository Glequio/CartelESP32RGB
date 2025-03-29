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
    
    # Enviar la respuesta HTML
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
    conn.send(response)
    conn.close()

received_text = ""

while True:
    print('estoy en loop')
    conn, addr = s.accept()
    print('Conexión desde', addr)
    handle_request(conn)
