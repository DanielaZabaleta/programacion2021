#----- Punto 1 -----# 
print ('Punto 1')
def validateFloat (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print ('Datos incorrectos, ingrese nuevamente')
        return valor
def validateString (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert (valor.isalpha())
            isCorrectData = True
        except AssertionError:
            print ('Datos incorrectos, ingrese nuevamente')
        return valor
#Calcular IMC -> estatura, peso -> peso/estatura**2
def pedirDatosEPN():
    ''' Se le pide al usuario el peso, la estatura y el nombre;
    validando que la data este buena'''
    preguntaPeso = 'Ingrese su peso en Kg: '
    preguntaEstatura = 'Ingrese su estatura en metros: '
    preguntaNombre = 'Ingrese su nombre: '
    peso = validateFloat(preguntaPeso)
    estatura = validateFloat(preguntaEstatura)
    nombre = validateString(preguntaNombre)
    return peso, estatura, nombre 

def calcularIMC ():
    pesoIn, estaturaIn, nombreIn = pedirDatosEPN()
    imc = pesoIn/(estaturaIn**2)
    return imc, nombreIn

imc, nombre = calcularIMC()
print (imc, nombre)
print( (f'El imc de {nombre} es de {imc} %'))

#---- Punto 2 ----#
print ('Punto 2')

def validateEndWith (strValidate, pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert (valor.endswith(strValidate))
            isCorrectData = True
        except AssertionError:
            print (f'Datos incorrectos, ingrese nuevamente y recuerde que debe terminar con {strValidate}')
        return valor
parrafo = validateEndWith('.', 'Ingrese un parrafo: ')
parrafo = parrafo[:-1]
palabras = parrafo.split (' ')
print (palabras)
print (f'La palabra mas grande es "{max (palabras, key = len)}" y el menor es "{min (palabras, key = len)}"')

#Truco 
# parrafo = 'hola, como anda todo, muchachos'
# parrafo = parrafo.replace (',', '')
# print (parrafo)
# palabras = parrafo.split (' ')
# print (palabras)

#----- Punto 3 -----#
print ('Punto 3')

def validarArchivo (nombreArchivo, descripcion):
    import sys
    try: 
        archivo = open (nombreArchivo)
        return True
    except FileNotFoundError:
        archivo = open(nombreArchivo, 'w', encoding='UTF-8')
        print ("2")
        archivo.writelines (descripcion)
        return False 

def guardarLinea (nombreArchivo, lineaIn):
    archivo = open (nombreArchivo, 'a')
    archivo.writelines('\n'+ lineaIn)

nameFile = "mantenimiento.txt"
isValidate = validarArchivo(nameFile, 'Seguimiento de mantenimientos de equipos medicos')
if (isValidate):
    descEquipo = input ('Ingrese la descripcion del equipo: ')
    nombre = validateString ('Ingrese su nombre: ')
    precio = validateFloat ('Ingrese el precio: ')
    linea = '\n' + descEquipo + ' nombre tecnico: ' + nombre + 'precio acordado: ' + str (precio)
    guardarLinea(nameFile, linea)
else: 
    print ('Se creo el archivo')