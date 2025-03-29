import network
import socket
import ure

# Conectarse a la red WiFi
ssid = 'TuSSID'  # Reemplaza con el nombre de tu red
password = 'TuPassword'  # Reemplaza con la contraseña de tu red

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Conexión exitosa')
print(station.ifconfig())

# Configurar el servidor HTTP
def web_page():
    html = """<html>
                <head>
                    <title>ESP32 Input</title>
                </head>
                <body>
                    <h1>Enviar texto al ESP32</h1>
                    <form action="/" method="POST">
                        <input type="text" name="input_text">
                        <input type="submit" value="Enviar">
                    </form>
                </body>
              </html>"""
    return html

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind



