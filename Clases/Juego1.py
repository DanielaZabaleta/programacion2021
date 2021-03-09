#----Entradas----#
MENSAJE_SALUDAR = '''Bienvenido a este programa, juguemos!!'''
PREGUNTAR_NUMERO = 'En este juego debes acertar un numero entero que va desde el 1-10, la idea es que lo puedes intentar las veces que quieras... Muchos exitos, ingresa tu numero : '
PREGUNTA_FALLIDA = 'Aaaah! Fallaste, ingrese otro numero : '
MENSAJE_GANASTE = 'Felicidades ganaste!!'
MENSAJE_PERDISTE = 'Perdiste, vuelve a intentarlo!!'
#----Entrada al codigo----#
NumeroOculto = 7
Vidas = 5
print (MENSAJE_SALUDAR)
NumeroIngresado = int (input (PREGUNTAR_NUMERO))
if (NumeroIngresado != NumeroOculto):
    Vidas -=1
while (NumeroOculto != NumeroIngresado and Vidas > 0):
    NumeroIngresado = int (input(PREGUNTA_FALLIDA))
    Vidas -=1

if (Vidas >= 0 and NumeroIngresado == NumeroOcultoDos):
    print (MENSAJE_GANASTE)
    print (Vidas)
else:
    print (MENSAJE_PERDISTE, 'El numero era el ', NumeroOculto)