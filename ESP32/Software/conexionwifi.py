import network
import socket

#ESTE CODIGO GENERA UN HTML Y SOLICITA QUE INGRESE UN VALOR Y AL OPRIMIR UN BOTON
#SE IMPRIMA EL VALOR EN CONSOLA

# Configurar la conexión WiFi
SSID = "Claro-Fibra-2.4G-1219"
KEY = "12345678"

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a la red WiFi...')
        wlan.connect(SSID, KEY)
        while not wlan.isconnected():
            pass
    print('Configuración de red:', wlan.ifconfig())
    return

do_connect()

# Función para generar la página HTML
def generate_html():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Ingresar Valor</title>
    <style>
        body {
            background-color: lightblue; /* Cambia el color de fondo aquí */
        }
    </style>
    </head>
    <body>
    <h1>SEBASTIAN SOS UN BOLUDO</h1>
    
    <h1>Ingrese un valor:</h1>
    <form action="/" method="post">
    <input type="text" name="valor" required>
    <button type="submit">Enviar</button>
    </form>
    </body>
    </html>
    """
    return html

# Función para manejar las solicitudes HTTP
def handle_request(conn):
    request = conn.recv(1024)
    request = str(request)
    if 'POST /' in request:
        valor = request.split('valor=')[1].split('&')[0]
        print("Valor ingresado:", str(valor[:-1]))
    response = generate_html()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()

# Configurar el servidor HTTP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# Esperar solicitudes y manejarlas
while True:
    conn, addr = s.accept()
    handle_request(conn)