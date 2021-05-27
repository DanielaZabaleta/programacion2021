#---- Punto 4 ----#
print ('Punto 4')

import sys
nombreArchivo = 'Pacientes.txt'
titulo = 'Manejo de los datos del paciente'

isCorrectInfo = False 
while (isCorrectInfo == False):
    try: 
        nombre = input ('Ingrese el nombre del paciente: ')
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print ('Ingresaste un dato incorrecto')

descEnfermedad = input ('Ingrese una breve descripcion de la enfermedad del paciente: ')
isCorrectInfo = False 
while (isCorrectInfo == False):
    try: 
        precio = float (input('Ingrese el precio de la consulta: '))
        isCorrectInfo = True
    except ValueError:
        print ('Ingresaste un dato incorrecto')
try: 
    archivo = open (nombreArchivo)
except FileNotFoundError:
    archivo = open (nombreArchivo, 'w', encoding='UTF-8')
    archivo.writelines(titulo)
    sys.exit

archivo = open(nombreArchivo, 'a')
linea = "\nNombre: "+ nombre + " Descripcion: "+ str(descEnfermedad) + " Precio: "+ str(precio)
archivo.writelines(linea)
archivo.close