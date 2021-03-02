
#----Entradas----#
MENSAJE_BIENVENIDA = 'Muy buenos dias, despierte que esta en clase de 6'
MENSAJE_ERROR = 'Por favor ingrese una opcion valida'
PREGUNTA_MENU = ''' Ingrese 
    1- para mostrar los numeros del 1-5
    2- para preguntar tu nombre 
    3- para mostrar el año en el que estamos 
    4- salir 
''' 
PREGUNTA_NOMBRE = 'Ingrese su nombre, por favor : '
Entrada = 1
while (Entrada >= 1 and Entrada <= 3):
    Entrada = int (input (PREGUNTA_MENU))
    print (Entrada)
    if (Entrada == 1):
        print (1,2,3,4,5)
    elif (Entrada == 2):
        Nombre = input (PREGUNTA_NOMBRE)
        print (f'Bienvenido {Nombre} a este menu emplee las otras opciones')
    elif (Entrada ==3):
        print ('Estamos en el año 2021')
    elif (Entrada == 4):
        print ('Muchas gracias por usar el programa, feliz dia')
    else: 
        Entrada = 1
        print (MENSAJE_ERROR)
