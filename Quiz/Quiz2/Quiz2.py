#----Preguntas----#
PreguntaNumero = ''' Ingrese alguna de estas opciones
    1. Hacer conversion de pesos a dolares o euros 
    2. Agregue un valor a la liesta de pesos 
    3. Mostrar valor mas alto, mas bajo y promedio
    4. Eliminar elemento de la lista
    5. Salir
'''
PreguntaMoneda = ''' Ingrese alguna de estas opciones
    C- Mostrar original en Pesos colombiano
    D- Mostrar en Dolares 
    E- Mostrar en Euros 
''' 
PreguntarNumero = 'Ingrese un  valor en COP : '
PreguntaBorrarCoordenada = 'Ingrese la posicion que desea borrar: '
#----Mensajes----#
MensajePesos = 'Mostrando lista en pesos'
MensaeDolares = 'Mostrando lista en dolares'
MensajeEuros = 'Mostrando lista en euros'
MensajeMayor = 'El mayor numero ingresado es -> '
MensajeMenor = 'El menor numero ingresado es -> '
MensajePromedio = 'El promedio es -> '
MensajeDespedida = 'Que tengas un feliz dia'
#----Error----#
MensajeErrorEntrada = 'Valor ingresado no valido'


ListaPesos = [20000, 30000, 4000, 2500, 1000, 7600]

#----Conversion punto 1----#
ListaEuros = []
for elemento in ListaPesos: 
    Conversor = round (elemento*0.00023,2)
    ListaEuros.append (Conversor)
ListaDolares = []
for elemento in ListaPesos: 
    Conversor = round (elemento*0.00028,2)
    ListaDolares.append (Conversor)


OpcionEscogida = int (input (PreguntaNumero))
while (OpcionEscogida != 5):
    #----Opcion 1----#
    if (OpcionEscogida == 1):
        OpcionMoneda = input (PreguntaMoneda)
        if (OpcionMoneda == 'C'):
            print (MensajePesos)
            print (ListaPesos)
        elif (OpcionMoneda == 'D'):
            print (MensaeDolares)
            print (ListaDolares)
        elif (OpcionMoneda == 'E'):
            print (MensajeEuros)
            print (ListaEuros)
        else:
            print (MensajeErrorEntrada)
    #----Opcion 2----#
    elif (OpcionEscogida == 2):
        ValorIngresado = float (input (PreguntarNumero))
        ListaPesos.append (ValorIngresado)
        print (ListaPesos)
    #----Opcion 3----#
    elif (OpcionEscogida == 3):
        print (MensajeMayor, max (ListaPesos))
        print (MensajeMenor, min (ListaPesos))
        print (MensajePromedio, sum (ListaPesos)/ len (ListaPesos))
    #----Opcion 4----#
    elif (OpcionEscogida == 4):
        print (ListaPesos)
        Posicion = int (input (PreguntaBorrarCoordenada))
        ListaPesos.pop (Posicion)
        print (ListaPesos)
    #----Opcion no valida----#
    else:
        print (MensajeErrorEntrada)
    OpcionEscogida = int (input (PreguntaNumero))

print ('Feliz dia')