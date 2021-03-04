
import random
#----Entradas----#
MENSAJE_SALUDAR = '''Bienvenido a este programa, juguemos!!'''
MENSAJE_SEGUNDO_NIVEL  =  'Felicidades pasaste el primer nivel ahora ve por el último !!'
MENSAJE_CALIENTE  =  'Estas caliente'
MENSAJE_FRIO  =  'Estas Frio'
PREGUNTAR_NUMERO = 'En este juego debes acertar un numero entero que va desde el 1-10, la idea es que antes de que se te acaben las vidas, no existe una vida 0... Muchos exitos, ingresa tu numero : '
PREGUNTA_DIFICULTAD = '''
    1- Facil
    2- Moderado 
    3- Dificil 
'''

PREGUNTA_FALLIDA = 'Aaaah! Fallaste, ingrese otro numero : '
MENSAJE_GANASTE = 'Felicidades ganaste!!'
MENSAJE_PERDISTE = 'Perdiste, vuelve a intentarlo!!'
#----Entrada al codigo----#
NumeroOculto = random.randint(1,10)
NumeroOcultoDos = random.randint (1,10)
Vidas = None

Dificultad = int (input (PREGUNTA_DIFICULTAD))
while (Dificultad !=1 and Dificultad !=2 and Dificultad !=3):
    print ('Ingrese una opcion valida')
    Dificultad = int (input (PREGUNTA_DIFICULTAD))


if (Dificultad == 1):
    Vidas = 10
    print ('Modo facil activado')
elif (Dificultad == 2):
    Vidas = 5
    print ('Modo moderado activado')
else:
    Vidas = 2
    print ('Modo dificil actvidado. significa peligro')

NumeroIngresado = int(input(PREGUNTAR_NUMERO))
while (NumeroIngresado != NumeroOculto and Vidas > 1):
    if (NumeroIngresado > NumeroOculto):
        print (MENSAJE_CALIENTE)
    else:
        print (MENSAJE_FRIO)
    Vidas -= 1
    print (f'Te quedan {Vidas} vidas')
    NumeroIngresado = int (input (PREGUNTA_FALLIDA))
if (Vidas >= 0 and NumeroIngresado == NumeroOculto):
    print (MENSAJE_SEGUNDO_NIVEL)
    NumeroIngresado = int (input (PREGUNTAR_NUMERO))
    while (NumeroIngresado != NumeroOcultoDos  and Vidas > 1 ):
        if (NumeroIngresado > NumeroOcultoDos ):
            print (MENSAJE_CALIENTE)
        else:
            print (MENSAJE_FRIO)
        Vidas -= 1
        print (f'Te quedan {Vidas} vidas')
        NumeroIngresado = int (input (PREGUNTA_FALLIDA))

if (Vidas >= 0  and NumeroIngresado == NumeroOcultoDos):
    print (MENSAJE_GANASTE)
else: 
    print (MENSAJE_PERDISTE, 'El numero era el', NumeroOculto,
    'El numero oculto dos era el', NumeroOcultoDos)