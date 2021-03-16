#----Preguntas----#
PreguntaNumero = ''' Ingrese alguna de las opciones 
    1. Convertir las temperaturas 
    2. Mostrar estado de las temperaturas del paciente 
    3. Ver la temperatura maxima, minima y cada cuanto fueron tomados los datos 
    4. Salir 
''' 
PreguntaConversionTemperatura = ''' Ingrese alguna de las opciones
    F- Mostrar temperatura en Fahrenheit
    K- Mostrar temperatura en Kelvin 
    C- Mostrar temperatura en Celsius 
''' 

#----Mensajes----#
MensajeErrorNumero = 'Por favor recuerda ingresar una de las opciones validas 1,2,3,4'
MensajeErrorConversion = 'Por favor recuerda ingresar una de las opciones validas F,K,C'
MensajeFahrenheit = 'Mostrando lista en grados Fahrenheit'
MensajeKelvin = 'Mostrando lista en Kelvin'
MensajeCelsius = 'No es necesaria la conversion, pero te mostramos la lista en grados centigrados'
MensajeMaxima = 'La temperatura maxima es : '
MensajeMinima = 'La temperatura minima es : '
MensajeCadaCuanto = 'Los datos se tomaron cada '
MensajeDespedida = 'Que tengas un feliz dia'

ListaTemperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#----Conversion punto 1----#
ListaFahrenheit = []
for elemento in ListaTemperaturaCorporal: 
    Conversor = round ((elemento*1.8)+32)
    ListaFahrenheit.append (Conversor)
ListaKelvin = []
for elemento in ListaTemperaturaCorporal:
    Conversor = round (elemento+273.15)
    ListaKelvin.append (Conversor)

#----Estado de la temperatura punto 2----#
ListaEstadoTemperatura = []
for elemento in ListaTemperaturaCorporal:
    EstadoTemperatura = ''
    if (elemento < 36):
        EstadoTemperatura = 'Hipotermia'
    elif (elemento >= 37.6):
        EstadoTemperatura = 'Fiebre'
    elif (elemento >= 36 and elemento < 37.6):
        EstadoTemperatura = 'Temperatura normal'
    ListaEstadoTemperatura.append (EstadoTemperatura)
''


OpcionEscogida = int (input(PreguntaNumero))
while (OpcionEscogida != 4): 
    #---Opcion1---#
    if (OpcionEscogida == 1):
        OpcionTemperatura = input (PreguntaConversionTemperatura)
        if (OpcionTemperatura == 'F'):
            print (MensajeFahrenheit)
            print (ListaFahrenheit)
        elif (OpcionTemperatura == 'K'):
            print (MensajeKelvin)
            print (ListaKelvin)
        elif (OpcionTemperatura == 'C'):
            print (MensajeCelsius)
            print (ListaTemperaturaCorporal)
        else: 
            print (MensajeErrorConversion)
    #---Opcion2---#
    elif (OpcionEscogida == 2):
        print (ListaEstadoTemperatura)
    #---Opcion3---#
    elif (OpcionEscogida == 3):
        print (MensajeMaxima, max (ListaTemperaturaCorporal))
        print (MensajeMinima, min (ListaTemperaturaCorporal))
        print (MensajeCadaCuanto, 24/len(ListaTemperaturaCorporal), 'horas')
    #----Opcion NO valida----#
    else: 
        print (MensajeErrorNumero)
    OpcionEscogida = int (input(PreguntaNumero))
#----Punto 4----#
print (MensajeDespedida)