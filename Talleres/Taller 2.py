#-----Constantes-----#
PREGUNTA_NOMBRE = "Como te llamas? :"
MENSAJE_SALUDO = "Un gusto en conocerte"
ENUNCIADO = "Ayudanos llenando el siguiente formato"
PREGUNTA_NUMEROA = "Ingrese un Numero A :"
PREGUNTA_NUMEROB = "Ingrese un Numero B :"

#-----Entrada al codigo-----#
Nombre = input (PREGUNTA_NOMBRE)
print (MENSAJE_SALUDO, Nombre)
print (ENUNCIADO)
NumeroA = int (input (PREGUNTA_NUMEROA))
NumeroB = int (input (PREGUNTA_NUMEROB))
isNumeroMayor = NumeroA > NumeroB
print (isNumeroMayor)
isNumeroMayorIgual = NumeroA >= NumeroB
print (isNumeroMayorIgual)
isNumeroMenor = NumeroA < NumeroB
print (isNumeroMenor)
isNumeroMenorIgual = NumeroA <= NumeroB 
print (isNumeroMenorIgual)
isNumerosIguales = NumeroA == NumeroB 
print (isNumerosIguales)
isNumerosDiferentes = NumeroA != NumeroB 
print (isNumerosDiferentes)

#-----Operaciones-----#