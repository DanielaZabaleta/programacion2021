Guardar = print ('Hola')
print (Guardar)

Guardar = round (14.2534897,2)
print (Guardar)

def linedesign (cantidad,simbolo):
    print (simbolo*cantidad)
    return None

linedesign (30,'#')
linedesign (10,'*')
linedesign (100,'🙃')

#----Muestre la lista ----#
def MostrarLista (ListaEntrada = []):
    for elemento in ListaEntrada:
        print (elemento)
    return None
Lista = [213,32,23123,321,321,233,1232,23]
Lista2 = [564654,645,64543,547,57865]
linedesign (30, ':*')
MostrarLista (Lista2)
#----Sumar 2 numeros----#
def sumar (a =0,b = 0):
    suma = a + b
    return suma 
linedesign (30,'*')
resultado = sumar ()
print (resultado)
print (sumar(12,14))
round (12.234897,2)
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


BaseIngresada = int (input('Ingrese una base entera: '))
ExponenteIngresado = int (input('Ingrese un exponente entero: '))


print (restar(83,87))
print (multiplicar(83,87))
print (dividir(83,87))
print (dividir())
print (potenciar(BaseIngresada,ExponenteIngresado))

calcular (sumar,63,67)