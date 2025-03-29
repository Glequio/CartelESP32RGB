import board
import neopixel
import time
import gc
import network
import socket




PIN = board.D13
ROW = 8
COL = 8
SL = 1
NMATRIZ = 3
SIZEX = COL * NMATRIZ
NUMPIXELS = ROW * COL * NMATRIZ
zigzag = False	#esta opcion anula el zigzag que hacen algunois modelos de matriz
# Configura el objeto neopixel
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=0.2, auto_write=False)

#Caracteres






diccionario={' ':[0B00000000,0B00000000,0B00000000,0B00000000],
             '1':[0B00100010,0B01111110,0B01111110,0B00000010],
             '2':[0B01001110,0B01010010,0B01110010,0B01110010],
             '3':[0B01010010,0B01010010,0B01111110,0B01111110],
             '4':[0B01111000,0B00001000,0B01111110,0B01111110],
             '5':[0B01110010,0B01010010,0B01011110,0B01011110],
             '6':[0B01111110,0B01010010,0B01011110,0B01011110],
             '7':[0B01000000,0B01000000,0B01111110,0B01110000],
             '8':[0B01111110,0B01010010,0B01111110,0B01111110],
             '9':[0B01111000,0B01001000,0B01111110,0B01111110],
             '0':[0B01111110,0B01000010,0B01111110,0B01111110],
             'A':[0B00111110,0B01001000,0B01111110,0B01111110],
             'B':[0B01111110,0B01010010,0B01111110,0B00011110],
             'C':[0B01111110,0B01000010,0B01100110,0B01100110],
             'D':[0B01111110,0B01000010,0B01111110,0B00111100],
             'E':[0B01111110,0B01010010,0B01010110,0B01000110],
             'F':[0B01111110,0B01001000,0B01101000,0B01100000],
             'G':[0B01111110,0B01001010,0B01101010,0B01101110],
             'H':[0B01111110,0B00001000,0B01111110,0B01111110],
             'I':[0B01111110,0B01111110],
             'J':[0B00000010,0B00000010,0B01111110,0B01111100],
             'K':[0B01111110,0B00010000,0B00111110,0B01000110],
             'L':[0B01111110,0B00000010,0B00000110,0B00000110],
             'M':[0B01111110,0B00100000,0B00010000,0B00100000,0B01111110,0B01111110],
             'N':[0B01111110,0B00100000,0B00010000,0B01111110,0B01111110],
             'Ñ':[0b01011110,0b01001000,0b01000100,0b01011110,0b00011110],
             'O':[0B00111100,0B01000010,0B01111110,0B00111100],
             'P':[0B01111110,0B01001000,0B01111000,0B00110000],
             'Q':[0B00111100,0B01001010,0B01000110,0B01111110,0B00111000],
             'R':[0B01111110,0B01001000,0B01111100,0B00110010],
             'S':[0B00100010,0B01010010,0B01011110,0B01001110],
             'T':[0B01000000,0B01111110,0B01111110,0B01000000],
             'U':[0B01111100,0B00000010,0B01111110,0B01111100],
             'V':[0B01100000,0B00011000,0B00000110,0B00011000,0B01100000,0B01100000],
             'W':[0B01111000,0B00000110,0B00001000,0B00000110,0B01111000,0B01111000],
             'X':[0B01100110,0B00100100,0B00010000,0B00100100,0B01100110,0B01100110],
             'Y':[0B01000000,0B00110000,0B00001110,0B00110000,0B01100000,0B01100000],
             'Z':[0B01000010,0B01000110,0B01001010,0B01110010,0B01100010],
             '$':[0B00010010,0B01111111,0B00101010,0B01111111,0B00100100]



             }
I=[0B01111110]


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








def borrar():
    # Apaga todos los LEDs
    pixels.fill((0, 0, 0))
    pixels.show()


def muestraCar(character,color):
    borrar()
    for i in range(len(character)):
        for j in range(8):
            if(character[i] >> (7-j)) & 1:
                pixels[barrido(j,i,0)] = color


    pixels.show()

def showText(text,xi,yi,color):
    print("SHOW TEXT X=",xi," Y=",yi)




    pixels.show()
    time.sleep(5)
    return




def	barrido(row,col,nMatriz):	#row y col representa las coordenadas que representa un barrido
                                #de izquierda a derecha en una matriz con zig zag
    if zigzag==True:
        if(row%2)==0:
            return (row*ROW+col)+(nMatriz*ROW*COL)
        else:
            return ((row+1)*COL-1-col)+(nMatriz*ROW*COL)
        
    else:
        if(row%2)==0:
            return (row*ROW+col)+(nMatriz*ROW*COL)
        else:
            return (row*COL+col)+(nMatriz*ROW*COL)        


def pruebaMatriz(tiempo):
    borrar()
    for i in range(8):
        borrar()
        pixels.show()
        for j in range(8):
            pixels[barrido(i,j,1)]=(0,20,40)
            pixels.show()
            time.sleep(tiempo)

def get_free_memory():
    # Recoge la basura para liberar memoria no utilizada
    gc.collect()

    # Obtiene la memoria libre actual
    free_memory = gc.mem_free()
    return free_memory

def scrollG(cadena,velocidad,direccion):
    for car in cadena:
        muestraCar(diccionario[car],(0,0,50))
        time.sleep(velocidad)

# Hay que hacer una funcion que barra verticalmente los caracteres del texto por matriz
# desde la matriz 1 que es la que esta mas a la izquierda del visor, para barrer lugo
# la matriz 2, luego la 3, etc. Como parametro va a recibir, el str texto, int NMATRIZ,
# int ROW, int COL, posision x,y de vertice suerior izquierdo, separador de letras sl, el color
#
# x es la posicion de donde tengo que imprimir el texto en pixel
# y es la posicion de donde tengo que imprimir el texto en pixel
# xc posicion x del cartel, va desde 1 a COL * NMATRIZ de izquierda --> derecha
# yc pocision y del cartel, va desde 1 a ROW de arriba --> abajo

def printText(texto,x,y,color):
    sizeText = 0
    for n in range(len(texto)):
        sizeText =sizeText+SL+len(diccionario[texto[n]])
    for n in range(sizeText):
        if (x < -(sizeText-1) or x > (COL*NMATRIZ) or y > 8 or y < -7):
            borrar()
            pixels.show()
            return
        if x < 1:
            puntero = 0
            for n in range(len(texto)):
                puntero = puntero + len(diccionario[texto[n]])
                if((x+puntero)>1):
                    #Imprimo
# print("caracter---->Xc:", xc,"  n------->",n)
# imprime(texto,n,xc,x,1,color)

                    xc = len(diccionario[texto[n]])+1 - (x + puntero)
                    imprime(texto,n,xc,x,y,1,color)
                    return
                else:
# print("SL------>Xc: ",xc,"  n------->",n)
# imprime(texto,n,0,x,xc,color)
                    puntero = puntero + SL
                    if((x+puntero)>1):
                        xc = x + puntero
                        imprime(texto,n,0,x,y,xc,color)
                        return
        else:
            imprime(texto,0,0,x,y,1,color)
            return
    return

# n es el numero de caracter de texto que se debe escribir
# ni es la pocision de la columna del caracter donde se comienza a escribir en la columna 1
# Dentro de la funcion ni es el puntero de x del cartel
# sl es el numero de columna desde donde imprime el primer caracter Solo se utiliza parta x<1
# xo es el valor inicial de x donde se comienza a escribir si x > 1

def imprime(texto,n,ni,x,y,sl,color):

    if (x > 0):
        nm = (int((x-1)/COL)) + 1
        xo = x - 1 - (int((x-1)/COL)) * COL

    else:
        nm = 1
        xo = 0

    if(sl > 1):
        ni = sl-1
        i = 0
        sl = 1
        n += 1
    else:
        i = ni
        ni = xo
    borrar()
    
    while(nm <= NMATRIZ):
        while(ni < COL):
            largoTexto = len(diccionario[texto[n]])
            if (i < largoTexto):
                for j in range(ROW):
                    if(y > 0):
                        if(diccionario[texto[n]][i] >> (7-j+y-1)) & 1:
                            pixels[barrido(j,ni,(nm-1))] = color
                    else:
                        if(diccionario[texto[n]][i] << - (y - 1)>> (7-j)) & 1:
                            pixels[barrido(j,ni,(nm-1))] = color
                if (ni == COL - 1):
                    ni = 0
                    nm += 1
                    i +=1
                    break
                i += 1
                ni += 1
           
            elif (ni == COL - 1 and i == largoTexto - 1):
                ni = 0
                i = 0
                n += 1
                nm += 1
                break
                
            elif (ni == COL-1 and i < largoTexto):
                ni = 0
                nm += 1
                break
            
            elif (ni + SL == COL - 1):
                ni = ni + SL
                n += 1
                i = 0
                break

            elif (ni + SL < COL - 1):
                ni = ni + SL
                n += 1
                i = 0
            
            elif (ni + SL > COL - 1):
                ni = ni + SL - COL 
                n += 1
                i = 0
                nm += 1
                break
            
            else:
                null
                
    pixels.show()
    time.sleep(.108)

    return




# Bucle principal
while True:
    texto1="MBC1M1B23456789009873124312345"
    
   # texto2="Hola Que tal como va todo"
# 
# 
    try:

#        pixels[barrido(1,1,1)]=(0,20,40)
#        pixels.show()
#        color = (0,0,30)
#         #scrollG(texto1,.5,0)
#        pruebaMatriz(.1)
         x=1
         y=1
         while(x<251):
# 
             x+=1
#             #y= int(x/10)
             printText("$$$$ HOLA COMO $$$$$$ N ESTAN 1 2 3 4 5 6 7 8 9 0 TUVWXYZ SSS A3OPQRFGHIJKLDECÑMB0123456789",25-x,1,(20,20,20))
#             #y += 1
#             time.sleep(.09)



    except KeyboardInterrupt:
        # Detiene el bucle si se presiona Ctrl+C
        borrar()
        break

#     except Exception as e:
#         # Captura cualquier otra excepción y muestra información de error
#         print("Error:", e)
#         borrar()
#         break



    free_memory = get_free_memory()
    print("Memoria RAM libre:", free_memory, "bytes")
    
    





