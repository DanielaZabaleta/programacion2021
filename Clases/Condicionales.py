#-----Constantes-----#
MENSAJE_BIENVENIDA = "Hola espero que estes bien"
MENSAJE_MAYOR = "El numero A es mayor que B"
MENSAJE_MENOR ="El numero A es menor que B"
MENSAJE_IGUAL ="A y B son iguales"
PREGUNTA_NUMERO_A = "Ingrese un numero A :"
PREGUNTA_NUMERO_B = "Ingrese un numero B :"

#-----Entrada al codigo-----#
print (MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
resultado = ""
if (isMayor):
    print (MENSAJE_MAYOR)
    resultado = MENSAJE_MAYOR
elif (isMenor): 
    print (MENSAJE_MENOR)
    resultado = MENSAJE_MENOR
else:
    print (MENSAJE_IGUAL)
    resultado = MENSAJE_IGUAL

print (resultado)