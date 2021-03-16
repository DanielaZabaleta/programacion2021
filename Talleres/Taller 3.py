#----Preguntas----#
PreguntaNumero = '''Ingrese algunas de estas opciones :  
    1. Convertir dolares
    2. Mostrar categoria de ingresos 
    3. Ver el mayor, menor y promedio de ingresos
    4. Salir
'''
PreguntaMoneda = '''Ingrese alguna de estas opciones . 
    C- Mostrar en pesos colombianos
    D- Mostrar original en dolares
    E- Mostrar en euros 
''' 
#----Mensajes----#
MensajeErrorNumero = 'Por favor recuerda ingresar una de las opciones validas 1,2,3,4'
MensajeErrorMoneda = 'Por favor recurda ingresar una de las opciones validad C,D,E'
MensajePesos = 'Mostrando lista en pesos'
MensajeDolares = 'No es necesaria la conversion, pero te mostramos la lista'
MensajeEuros = 'Mostrando lista en euros'
MensajeDespedida = 'Que tengas un feliz dia'
MensajeAlto = 'El ingreso mas alto fue --> '
MensajeBajo = 'El ingres mas bajo fue --> '
MensajePromedio = 'El ingreso promedio fue --> '

ListaDolares = [20000,30000,4000,2500,1000,7600]

#----Conversion punto 1----#
ListaPesos = []
for elemento in ListaDolares:
    Conversor = round (elemento*3700)
    ListaPesos.append (Conversor)
ListaEuros = []
for elemento in ListaDolares:
    Conversor = round (elemento*0.84)
    ListaEuros.append (Conversor)

#----Categoria de ingresos punto 2----#
ListaCategoria = []
for elemento in ListaDolares:
    Categoria = ''
    if (elemento < 1000):
        Categoria = 'Ingresos Bajos'
    elif (elemento >= 1000 and elemento < 7000):
        Categoria = 'Ingresos medios'
    elif (elemento >= 7000 and elemento < 20000):
        Categoria = 'Ingresos altos'
    else:
        Categoria = 'Ingresos elevados'
    ListaCategoria.append (Categoria)
''


OpcionEscogida = int (input(PreguntaNumero))
while (OpcionEscogida != 4):
    #---Opcion1---#
    if (OpcionEscogida == 1):
        OpcionMoneda = input (PreguntaMoneda)
        if (OpcionMoneda == 'C'):
            print (MensajePesos)
            print (ListaPesos)
        elif (OpcionMoneda == 'D'):
            print (MensajeDolares)
            print (ListaDolares)
        elif (OpcionMoneda == 'E'):
            print (MensajeEuros)
            print (ListaEuros)
        else: 
            print (MensajeErrorMoneda)
    #---Opcion2---#
    elif (OpcionEscogida == 2):
        print (ListaCategoria)
    #---Opcion3---#
    elif (OpcionEscogida == 3):
        print (MensajeAlto, max (ListaDolares))
        print (MensajeBajo, min (ListaDolares))
        print (MensajePromedio, sum (ListaDolares) / len (ListaDolares))
    #---Opcion NO valida---#
    else:
        print (MensajeErrorNumero)
    OpcionEscogida = int (input (PreguntaNumero))
#----Punto 4----#
print (MensajeDespedida)