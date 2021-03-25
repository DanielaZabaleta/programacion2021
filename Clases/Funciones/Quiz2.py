import ConversorTemperaturas as ct
import Funciones as fn
PreguntaNumero = ''' Ingrese alguna de las opciones 
    1. Convertir temperaturas 
    2. Mostrar clasificacion
    3. Mostrar topes
    4. Salir 
''' 
PreguntaTemperatura = ''' Ingrese alguna de las opciones
    F- Mostrar Fahrenheit
    K- Mostrar Kelvin 
    C- Mostrar Celsius 
''' 

#----Mensajes----#
MensajeFahrenheit = 'Mostrando lista en grados Fahrenheit'
MensajeKelvin = 'Mostrando lista en Kelvin'
MensajeCelsius = 'No es necesaria la conversion, pero te mostramos la lista en grados centigrados'
MensajeDespedida = 'Que tengas un feliz dia'
#----Error----#
MensajeErrorEntrada = 'Valor ingresado no valido'

TemperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

TemperaturaCorporalFahrenheit = ct.ConversionTemperatura (TemperaturaCorporal,'F')
TemperaturaCorporalKelvin = ct.ConversionTemperatura (TemperaturaCorporal,'K')
ClasificacionTemperaturas = ct.ClasificarTemperaturas (TemperaturaCorporal)
OpcionEscogida = int (input(PreguntaNumero))
while (OpcionEscogida != 4): 
    #---Opcion1---#
    if (OpcionEscogida == 1):
        OpcionTemperatura = input (PreguntaTemperatura)
        if (OpcionTemperatura == 'F'):
            print (MensajeFahrenheit)
            fn.MostrarLista (TemperaturaCorporalFahrenheit)
        elif (OpcionTemperatura == 'K'):
            print (MensajeKelvin)
            fn.MostrarLista (TemperaturaCorporalKelvin)
        elif (OpcionTemperatura == 'C'):
            print (MensajeCelsius)
            fn.MostrarLista (TemperaturaCorporal)
        else: 
            print (MensajeErrorEntrada)
    #---Opcion2---#
    elif (OpcionEscogida == 2):
        print ('Mostrando clasificación')
        print ('°C','\t','Clasificacion')
        fn.Mostrar2Lista (TemperaturaCorporal,ClasificacionTemperaturas)
    #---Opcion3---#
    elif (OpcionEscogida == 3):
        ct.MostrarTopes (TemperaturaCorporal)
    #----Opcion NO valida----#
    else: 
        print (MensajeErrorEntrada)
    OpcionEscogida = int (input(PreguntaNumero))
#----Punto 4----#
print (MensajeDespedida)