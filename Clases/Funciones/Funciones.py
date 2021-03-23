#----Sumar 2 numeros----#
def sumar (a =0,b = 0):
    '''
        Devuelve la suma de 2 numeros a y b
        por defecto a vale 0 al igual que b
    '''
    suma = a + b
    return suma 
#----Restar 2 numeros----#
def restar (a =0,b = 0):
    resta = a - b
    return resta
#----Multiplicar 2 numeros----#
def multiplicar (a =0,b = 0):
    multiplica = a * b
    return multiplica 
#----Dividir 2 numeros----#
def dividir (a = 0,b = 1):
    dividi = a / b
    return dividi
#----Potenciar 2 numeros----#
def potenciar (base = 0,exponente = 1):
    potencia = base ** exponente
    return potencia
#----Funciones dependientes de otras----#
def calcular (operacion,NumeroA,NumeroB):
    print (operacion(NumeroA,NumeroB))
