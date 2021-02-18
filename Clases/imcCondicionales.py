#-----Constantes-----# 
PREGUNTA_PESO = "Cuanto pesas en kg? :"
PREGUNTA_ESTATURA = "Cuanto mides en mts? :"
MENSAJE_BIENVENIDA = "Hola, como estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es ..."
MENSAJE_BAJO_PESO = "Estas pero delgado"
MENSAJE_NORMAL = "Estas en forma"
MENSAJE_SOBRE_PESO ="Ten cuidado estas en sobre peso"
MENSAJE_OBESO = "Cuidado estas obeso, tu salud corre riesgo"

#----Entrada codigo----#
print (MENSAJE_BIENVENIDA)
Peso = float (input (PREGUNTA_PESO))
Estatura = float (input (PREGUNTA_ESTATURA))
IMC = Peso/(Estatura)**2
isBajoPeso = IMC < 18.5
isNormal = IMC >= 18.5 and IMC < 25
isSobrePeso = IMC >= 25 and IMC < 30
resultado = ""
if (isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isNormal):
    resultado = MENSAJE_NORMAL
elif (isSobrePeso):
    resultado = MENSAJE_SOBRE_PESO
else:
    resultado = MENSAJE_OBESO
print (MENSAJE_DESPEDIDA, IMC)
print (resultado)