#----Dada una lista muéstrela en pantalla elemento a elemento----#
Numeros = [12,6,7,21,15,28,9,7,5,15,32,14,22]
Nombres = ['Andres','Daniela','Cristo','Jesus','Luis','Luisa','Miguel']
def MostrarLista (Lista):
    for elemento in Lista:
        print (elemento)
MostrarLista (Numeros)
MostrarLista (Nombres)
#----Dada una lista de números enteros muestre en pantalla el número más grande, el más pequeño y el promedio de la lista----#
NumerosEnteros = [12,22,14,68,76,84,26,16,18,24,88]
def InformacionLista (Lista):
    Mayor = max (Lista)
    Menor = min (Lista)
    Acumulado = 0
    for elemento in Lista:
        Acumulado += elemento
    TamañoDeLista = len (Lista)
    Promedio = Acumulado / TamañoDeLista
    print (f'El numero mayor en la lista es el {Mayor}, el menor es el {Menor} y el promedio es {Promedio}')
InformacionLista (NumerosEnteros)
#----Salude n veces----#
def Saludar (Cantidad = 0):
    print ('Saludos '*Cantidad)
Saludar (8)
#----Que devuelva todos los números pares de una lista de números enteros----#
ListaNumerosEnteros = [2,5,12,17,25,22,18,23,32,24,35,29,16,28]
def ListaPares (Lista):
    Pares = []
    for elemento in Lista:
        if elemento % 2 == 0:
            Pares.append (elemento)
    return Pares
NumerosPares = ListaPares (ListaNumerosEnteros) 
print (NumerosPares)
#----Que devuelva únicamente los elementos mayores a 24----#
Numeros1 = [12,5,8,23,15,24,27,32,29,36,25,33,39]
def ListaMayores (Lista):
    Mayores = []
    for elemento in Lista:
        if elemento > 24:
            Mayores.append (elemento)
    return Mayores
NumerosMayores = ListaMayores (Numeros1)
print (NumerosMayores)
#----Se sabe que el IMC se calcula dividiendo el peso por la altura al cuadrado, realice una función que lo calcule----#
def CalculoIMC (Peso, Altura):
    return Peso / (Altura**2)
IMC = CalculoIMC (53, 1.61)
print (IMC)
#----Crea un función que sirva para despedirte del que esta ejecutando el código----#
def Adios ():
    print ("Fue un placer aprender cosas nuevas")
Adios ()