def ConversionTemperatura (temperaturas,unidad):
    '''Convierte una lista de temperaturas segun la unidad ingresada,
    puede ser ...
            K ---> Kelvin
            F ---> Fahrenheit
    '''
    ListaConvertida = []
    for temperatura in temperaturas:
        conversion = None
        if unidad == 'F':
            conversion = temperatura * 1.8 + 32
        elif unidad == 'K':
            conversion = temperatura + 273.15
        else:
            ListaConvertida = None
        ListaConvertida.append (conversion)
    return ListaConvertida
def ClasificarTemperaturas (temperaturas):
    ''' Retorna la clasificacion de las temperaturas ingresadas
    deben estar en grados centigrados
    '''
    ListaClasificacion = []
    Estado = None 
    for temperatura in temperaturas:
        if temperatura < 36: 
            Estado = 'Hipotermia'
        elif temperatura >= 36 and temperatura < 37.6:
            Estado = 'Normal'
        else:
            Estado = 'Fiebre'
        ListaClasificacion.append (Estado)
    return ListaClasificacion 
def MostrarTopes (lista):
    mayor = round (max(lista),2)
    menor = round (min(lista),2)
    PeriodoHoras = round (24/len(lista),2)
    print ('La mayor temperatura es', mayor)
    print ('La menor temperatura es', menor)
    print ('El periodo de muestras es', PeriodoHoras)