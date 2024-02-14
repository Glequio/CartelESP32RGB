import board
import neopixel
import time
import gc

# Configura el número total de LEDs y el pin de salida

PIN = board.D13
ROW = 8
COL = 8
SL = 2
NMATRIZ = 1
SIZEX = COL * NMATRIZ
NUMPIXELS = ROW * COL * NMATRIZ
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

             'M':[0B01111110,0B00100000,0B00010000,0B00100000,0B01111110,0B01111110]
             
             
             
             
             }
I=[0B01111110]

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
    if(row%2)==0:
        return (row*ROW+col)+(nMatriz*ROW*COL)
    else:
        return ((row+1)*ROW-1-col)+(nMatriz*ROW*COL)
      

def pruebaMatriz(tiempo):
    borrar()
    for i in range(8):
        borrar()
        pixels.show()
        for j in range(8):
            pixels[barrido(i,j,0)]=(80,10,0)
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

def printText(texto,x,y,sl,color):
    sizeText = 0
    for n in range(len(texto)):
        sizeText =sizeText+sl+len(diccionario[texto[n]])    
    for n in range(sizeText):
        if (x < -(sizeText-1) or x > (COL*NMATRIZ) or y > 8 or y < -7):
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
                    puntero = puntero + sl
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
    borrar()    
    while(nm <= NMATRIZ):
        
        i = ni
        ni = xo
        if(sl > 1):
            ni = sl-1
            i = 0
            sl = 1
            n += 1
        while(ni < COL):
            if (i < len(diccionario[texto[n]])):
                for j in range(ROW):
                    if(y > 0):
                        if(diccionario[texto[n]][i] >> (7-j+y-1)) & 1:
                            pixels[barrido(j,ni,0)] = color
                    else:
                        if(diccionario[texto[n]][i] << - (y - 1)>> (7-j)) & 1:
                            pixels[barrido(j,ni,0)] = color

                i += 1
                ni += 1
            else:
                if ((ni + SL-1) >= COL):
                    sl = (ni+SL-COL)
                    ni = 0
                    nm += 1
                    n += 1
                    break
                elif ((ni + SL - 1) == COL-1):
                    sl = 1
                    ni = 0
                    nm += 1
                    n += 1
                    break
                else:
                    i = 0
                    ni = ni + SL
                    n += 1
            if (ni == COL):
                sl = 1
                nm += 1
    pixels.show()

    return




# Bucle principal
while True:
    texto1="MB1M1B23456789009873124312345"
   # texto2="Hola Que tal como va todo"
    
    
    try:
        color = (0,0,30)
        #scrollG(texto1,.5,0)
        #pruebaMatriz(.1)
        x=1
        y=-8
        while(y<9):
            
            x=-y
            #y= int(x/10)
            printText("A3B0123456789",x,y,2,(0,100,30))
            y += 1
            time.sleep(.09)

  
      
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
    
    
