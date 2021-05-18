
isCorrectInfo = False
while (isCorrectInfo == False):
    try: 
        edad = int (input('Ingrese su edad: '))
        isCorrectInfo = True
    except ValueError:
        print ('Ingresaste un dato no valido')
nombreArchivo = input ('Ingrese el nombre del archivo que desea encontar: ')
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    print (f'Archivo {nombreArchivo} no se ha encontrado')

base = 4
divisor = 0
try:
    dividir = base/divisor
except ZeroDivisionError:
    print('El divisor ingresado es igual a 0, por lo tanto es imposible dividir')

nombre = 'Daniela'
print (nombre.isalpha())
assert (nombre.isalpha())

isCorrectInfo = False
while (isCorrectInfo == False):
    try: 
        nombre = input('Ingrese su nombre: ')
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError():
        print ('Ingresaste un dato no valido')

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        edad = int(input('Ingrese su edad :'))
        assert (edad >= 18)
        isCorrectInfo = True
    except AssertionError:
        print('Los menores de edad no pueden acceder')
    except ValueError:
        print('Las edades son números enteros')

listas = [2,43,42,4]
try:
    listas[5]
except IndexError:
    print('El indice es mayor al tamaño de la lista')