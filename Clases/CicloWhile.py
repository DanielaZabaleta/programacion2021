#----Mensajes----#
MENSAJE_SALUDAR = 'Bienvenido!! Te apoyare ahorrando'
MESANJE_AHORRO = 'LLEVAS AHORRADO ...'
PREGUNTAR_VALOR_CPU = 'Cuanto vale el pc que deseas? : '
PREGUNTA_CUANTO_TIENE = 'Cuanto llevas ahorrado? : '

#----Entradas----#
print (MENSAJE_SALUDAR)
Valor = float (input (PREGUNTAR_VALOR_CPU))
Ahorrado = float (input (PREGUNTA_CUANTO_TIENE))

while (Valor > Ahorrado):
    print (MESANJE_AHORRO, Ahorrado, "Te faltan ...", Valor - Ahorrado)
    Ahorrado = Ahorrado + 1000
print (Valor == Ahorrado)