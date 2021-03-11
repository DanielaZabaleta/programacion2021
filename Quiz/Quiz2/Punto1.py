ListaPesos = [20000, 30000, 4000, 2500, 1000, 7600]
PreguntaMoneda = ''' Ingrese alguna de estas opciones
    C- Mostrar original en Pesos colombiano
    D- Mostrar en Dolares 
    E- Mostrar en Euros 
''' 
MensajePesos = 'Mostrando lista en pesos'
MensaeDolares = 'Mostrando lista en dolares'
MensajeEuros = 'Mostrando lista en euros'
MensajeErrorEntrada = 'Valor ingresado no valido'

ListaEuros = []
for elemento in ListaPesos: 
    Conversor = round (elemento*0.00023,2)
    ListaEuros.append (Conversor)
ListaDolares = []
for elemento in ListaPesos: 
    Conversor = round (elemento*0.00028,2)
    ListaDolares.append (Conversor)

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