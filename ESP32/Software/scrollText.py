import board
import neopixel
import time
import gc

# Configura el número total de LEDs y el pin de salida
NUMPIXELS = 64
PIN = board.D13
ROW = 8
COL = 8
# Configura el objeto neopixel
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=0.2, auto_write=False)

#Caracteres






diccionario={'1':[0B00100010,0B01111110,0B01111110,0B00000010],
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
        



# Bucle principal
while True:
    texto1="MB1M1B23456789009873124312345"
    texto2="Hola Que tal como va todo"
    
    
    try:
        scrollG(texto1,.5,0)
      
    except KeyboardInterrupt:
        # Detiene el bucle si se presiona Ctrl+C
        borrar()
        break
    
    except Exception as e:
        # Captura cualquier otra excepción y muestra información de error
        print("Error:", e)
        borrar()
        break
    
    
    
    free_memory = get_free_memory()
    print("Memoria RAM libre:", free_memory, "bytes")
