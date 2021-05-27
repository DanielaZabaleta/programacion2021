#---- Punto 3 ----#
print ('Punto 3')

def ConversorEuros ():
    isCorrectInfo = False 
    while (isCorrectInfo == False):
        try: 
            nombre = input ('Ingrese su nombre: ')
            assert (nombre.isalpha())
            isCorrectInfo = True
        except AssertionError:
            print ('Ingresaste un dato incorrecto')
    isCorrectInfo = False 
    while (isCorrectInfo == False):
        try: 
            dinero = float (input('Ingresa la cantidad de dinero en dolares que tienes: '))
            isCorrectInfo = True
        except ValueError:
            print ('Ingresaste un dacto incorrecto')
    print (f'Hola {nombre}, la cantidad de dinero que tienes en euros es {dinero*0.82}')
ConversorEuros()