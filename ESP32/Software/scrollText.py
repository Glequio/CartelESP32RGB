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
#    print("X---------------",x)
    for n in range(len(texto)):
        sizeText =sizeText+sl+len(diccionario[texto[n]])    
    for n in range(sizeText):
        if (x < -(sizeText-1) or x > (COL*NMATRIZ) or y > 8 or y < -7):
#            print("Impresion fuera de rango")
            return 
#        print("SE IMPRIME")
        if x < 1:
            puntero = 0
            for n in range(len(texto)):
                puntero = puntero + len(diccionario[texto[n]])
#                 print("ANTES IF x+puntero",x+puntero)
#                 time.sleep(1)
                if((x+puntero)>1):
                    #Imprimo
                    xc = len(diccionario[texto[n]])+1 - (x + puntero)
#                     print("x+puntero----",x+puntero)
             #       print("caracter---->Xc:", xc,"  n------->",n)
                    #time.sleep(1)
                    
                    imprime(texto,n,xc,1,color)
                    return
                else:
                    puntero = puntero + sl
                    if((x+puntero)>1):
                        xc = x + puntero
            #            print("SL------>Xc: ",xc,"  n------->",n)
                        #time.sleep(1)
                        imprime(texto,n,0,xc,color)
                        
                        
                        return

    
    
    
    return

# n es el numero de caracter de texto que se debe escribir
# ni es la pocision de la columna del caracter donde se comienza a escribir en la columna 1
# Dentro de la funcion ni es el puntero de x del cartel
# sl es el numero de columna desde donde imprime el primer caracter Solo se utiliza parta x<1


def imprime(texto, n, ni, sl,color):
    borrar()
    m = 0
    while(m < NMATRIZ):
        i = ni
        ni = 0
        #borrar()
        if(sl > 1):
            ni = sl-1
            i = 0
            sl = 1
            n += 1
#         else:
#             i = ni
#         print("i:  ",i)
#         print("n: ",n)
#         print("(diccionario[texto[n][i]]:  ",(diccionario[texto[2]][2]))
        while(ni < COL):

           # print("ni .......",ni)
            if (i < len(diccionario[texto[n]])):
 #               print("La letra a imprimir es----->",texto[n])
                for j in range(ROW):
 #                   print("i=",i )
                    if(diccionario[texto[n]][i] >> (7-j)) & 1:
                        #print("pixel--->",barrido(j,ni,0))
                        pixels[barrido(j,ni,0)] = color
                i += 1
                ni += 1
            else:
               # print("(ni + SL-1)::::",(ni + SL-1))
                if ((ni + SL-1) >= COL):
              #      print("ESTOY EN EL IF")
                    sl = (ni+SL-COL)
                    ni = 0
                    m += 1
                    n += 1
                    break
                elif ((ni + SL - 1) == COL-1):
             #       print("ESTOY EN EL PRIMER ELIF")
                    sl = 1
                    ni = 0
                    m += 1
                    n += 1
                    break
                else:
            #        print("ESTOY EN EL ELSE")
                    i = 0
                    ni = ni + SL
                    n += 1
            #print("ni actual: ",ni,"  i actual: ",i)

            
            if (ni == COL):
                sl = 1
                m += 1
    pixels.show()            
    time.sleep(0.15)
    return        
    
    
    
    
    
    
    
    return




# Bucle principal
while True:
    texto1="MB1M1B23456789009873124312345"
    texto2="Hola Que tal como va todo"
    
    
    try:
        color = (0,0,30)
        #scrollG(texto1,.5,0)
        #pruebaMatriz(.1)
        x=-0
        
        #while(x<1):
        
        y= 1
       # print("X = ",x)
        printText("A3B0123456789",x,y,2,(0,0,30))
    #imprime("M", -1, 3, 1,color)
        x += 1
        #time.sleep(.05)

  
      
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
    
    
    
    
    
    
    
    #print("valor x : ",x)
#     
#     cont = 1
#     while(cont <= NMATRIZ):
#         if x<(cont * COL) and x > -sizeText :	#chequeo si algo del texto cae en la impresion
#             print("valor x",x)
#             for k in range(len(texto)):
#                 puntero = puntero + len(diccionario[texto[k]])
#                 print("PUNTERO: ",puntero)
#                 if puntero >= 1:	#veo cuando el caracter toca la posision x=1 de iz a der
#                     print("imprimo carcater :",texto[k])
#                     time.sleep(1)
#                                         
#                     for i in range(len(character)):
#                         for j in range(8):
#                             if(character[i] >> (7-j)) & 1:
#                                 pixels[barrido(j,i,0)] = color                   
#                     
#                     
#                     
#                 puntero = puntero + sl
# #             if len(diccionario[texto])-x > 0: 
# #                 for i in range(len(diccionario[texto])-x):
# #                     for j in range(ROW):
# #                         if(diccionario[texto][i+x] >> (7-j)) & 1:
# #                             pixels[barrido(j,i,0)] = color
#             
#             
#             
#         else:
#             print("Fuera de rango o finalizacion")            
#         cont+=1











#     sizeText = 0
#     for n in range(len(texto)):
#         sizeText =sizeText+sl+len(diccionario[texto[n]])
#     #print("Tamaño de texto: ",sizeText)
#     if (x < -(sizeText-1) or x > (COL*NMATRIZ) or y > 8 or y < -7):
#         print("Impresion fuera de rango")
#         return 
#     print("SE IMPRIME")
#     if x < 1:
#         numCaracter = -1
#         puntero = 0
#         for n in range(len(texto)):
#             numCaracter += 1
#             puntero = puntero + len(diccionario[texto[n]])
#             #print("Puntero: ",puntero)
#             #print("x + puntero : ",x  + puntero)
#             if ( (x + puntero) > 1 ):
#                 #print("Tengo que escribir a partir del caracter",texto[numCaracter])
#                 #showText(texto,xi,yi,color)
#                 cont=1
#                 punteroBefore = puntero - len(diccionario[texto[n]])
#                 while (cont <= len(diccionario[texto[n]])):
#                     if ((x + punteroBefore + cont -1) == 1):
#                         xi = sl - (cont -2)
#                         yi = y
#                         print("CAyo en un sl y el x es :",xi)
#                         #showText(texto,xi,yi,color)
#                     cont += 1
# 
# 
# 
#                 puntero = puntero + sl
#             elif ((x + puntero + sl) > 1):
#                 puntero = puntero + sl
#                 #if ((x + puntero) >= 1):
#                 print("TEngo que escribir despues de un sl: ")
#                 punteroBefore = puntero - sl
#                 cont=1
#                 while (cont <= sl):
#                     print("Entre al while con cont= ",cont,"(x + punteroBefore + cont)",(x + punteroBefore + cont))
#                     if ((x + punteroBefore + cont -1) == 1):
#                         xi = sl - (cont -2)	#Valor de x desde el que se imprime el texto ingresado
#                         yi = y
#                         print("CAyo en un sl y el x es :",xi)
#                         #showText(texto,xi,yi,color)
#                     cont += 1
#             else:
#                 puntero = puntero +sl
#                     
#                     
#         
#         print("Imprimo para x > 1")
# 
# 
#     pixels.show()
#     return 