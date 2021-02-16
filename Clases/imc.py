#-----Constantes-----# 
PREGUNTA_PESO = "Cuanto pesas en kg? :"
PREGUNTA_ESTATURA = "Cuanto mides en mts? :"
MENSAJE_BIENVENIDA = "Hola, como estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es ..."

#----Entrada codigo----#
print (MENSAJE_BIENVENIDA)
Peso = float (input (PREGUNTA_PESO))
Estatura = float (input (PREGUNTA_ESTATURA))
IMC = Peso/(Estatura)**2
print (MENSAJE_DESPEDIDA, IMC)
isObeso = IMC >= 30 
print ("El resultado de la prueba de obesidad es ...", isObeso)