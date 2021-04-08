#----Función que dado tres números muestre en pantalla las operaciones-----#
def sumar (a=0,b=0,c=0):
    suma = a + b + c
    return suma 
print (sumar(2,3,4))
def restar (a=0,b=0,c=0):
    resta = a - b - c 
    return resta 
print (restar(2,3,4))
def multiplicar (a=0,b=0,c=0):
    multiplica = a * b
    return multiplica 
print (multiplicar(2,3,4))
def dividir (a=0,b=1,c=1):
    divide = a / b / c
    return divide
print (dividir(2,3,4))
def potenciar (base=0,exponente=1, exponente2=1):
    potencia = base ** exponente ** exponente2
    return potencia
print (potenciar(2,3,4))

#----Función que dada tres listas del mismo tamaño las muestre en pantalla----#
Numeros = [12,6,7,21,15,28,9]
Nombres = ['Andres','Daniela','Cristo','Jesus','Luis','Luisa','Miguel']
Enteros = [12,22,14,68,76,84,26]
def MostrarListas (Lista):
    print (Lista)
MostrarListas (Numeros)
MostrarListas (Nombres)
MostrarListas (Enteros)

#-----Función que calcule y devuelva el área de un triangulo----#
def area (base=0,altura=0):
    triangulo = (base * altura)/2
    return triangulo
def calcular (operacion,NumeroA,NumeroB):
    print (operacion(NumeroA,NumeroB))
BaseIngresada = int (input('Ingrese una base entera: '))
AlturaIngresada = int (input('Ingrese una altura entera: '))
print (area(BaseIngresada,AlturaIngresada))

#----Función que dada una lista de números enteros muestre el promedio, el máximo, el mínimo----#
ListaNumerosEnteros = [12,22,14,68,76,84,26,16,18,24,88]
def InformacionLista (Lista):
    Mayor = max (Lista)
    Menor = min (Lista)
    Acumulado = 0
    for elemento in Lista:
        Acumulado += elemento
    TamañoDeLista = len (Lista)
    Promedio = Acumulado / TamañoDeLista
    print (f'El numero mayor en la lista es el {Mayor}, el menor es el {Menor} y el promedio es {Promedio}')
InformacionLista (ListaNumerosEnteros)

#----Dado un número n de la sucesión muestre en pantalla su valor----#

print ('#-----Bonus-----#')
#-----Desde otro archivo llame todas las funciones creadas----#
import TallerFunciones as tf 