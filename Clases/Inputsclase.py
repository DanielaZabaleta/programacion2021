#-----Constantes-----# 
PREGUNTA_NOMBRE = "Como te llamas? : "
PREGUNTA_EDAD = "Cuantos años tienes? : "
PREGUNTA_ESTATURA = "Cuanto mides? : "

MENSAJE_SALUDO = "Un gusto en conocerte"

#-------Entrada al codigo-------#
Nombre = input (PREGUNTA_NOMBRE)
print (MENSAJE_SALUDO, Nombre)
Edad = int (input (PREGUNTA_EDAD))
Estatura = float (input (PREGUNTA_ESTATURA))
print (Edad + 8)