#-----Constantes----#
MENSAJE_SALUDO = "Hola, como estas? Voy a analizar el nivel de trigliceridos y homocisteina"
PREGUNTA_NIVEL_TRIGLICERIDOS = "Ingrese el valor del nivel de trigliceridos : "
PREGUNTA_NIVEL_HOMOCISTEINA = "Ingrese el valor del nivel de homocisteina : "
MENSAJE_TRI_OPTIMO = "Los trigliceridos se encuentran en un rango de valor normal"
MENSAJE_TRI_SOBRE_LIM_OPTIMO = "Los trigliceridos se encuentran sobre el limite optimo, hay que tener cuidado"
MENSAJE_TRI_ALTO = "Los trigliceridos se encuentran en un rango alto, se necesita ayuda"
MENSAJE_TRI_MUYALTO = "Los trigliceridos estan en un nivel muy alto, es urgente solicitar ayuda"
MENSAJE_HOM_OPTIMO = "La homocisteina se encuentra en un rango de valor normal"
MENSAJE_HOM_SOBRE_LIM_OPTIMO = "La homocisteina se encuentra sobre el limite optimo, hay que tener cuidado"
MENSAJE_HOM_ALTO = "La homocisteina se encuentra en un rango alto, se necesita ayuda"
MENSAJE_HOM_MUYALTO = "La homocisteina esta en un nivel muy alto, es urgente solicitar ayuda"

#----Entrada al codigo----#
print (MENSAJE_SALUDO)
Trigliceridos = int (input (PREGUNTA_NIVEL_TRIGLICERIDOS))
Homocisteina = int (input (PREGUNTA_NIVEL_HOMOCISTEINA))
isOptimoTri = Trigliceridos < 150 
isSobreLimTri = Trigliceridos >= 150 and Trigliceridos <= 199 
isAltoTri = Trigliceridos >= 200 and Trigliceridos <= 499 
isMuyAltoTri = Trigliceridos > 500 
isOptimoHomo = Homocisteina >= 2 and Homocisteina < 15 
isSobreLimHomo = Homocisteina >= 15 and Homocisteina < 30
isAltoHomo = Homocisteina >= 30 and Homocisteina <= 100
isMuyAltoHomo = Homocisteina > 100

if (isOptimoTri):
    print (MENSAJE_TRI_OPTIMO)
elif (isSobreLimTri):
    print (MENSAJE_TRI_SOBRE_LIM_OPTIMO)
elif (isAltoTri):
    print (MENSAJE_TRI_ALTO)
else: 
    print (MENSAJE_TRI_MUYALTO)

if (isOptimoHomo):
    print (MENSAJE_HOM_OPTIMO)
elif (isSobreLimHomo):
    print (MENSAJE_HOM_SOBRE_LIM_OPTIMO)
elif (isAltoHomo):
    print (MENSAJE_HOM_ALTO)
else:
    print (MENSAJE_HOM_MUYALTO)