#----Ejercicio 1 Condicionales----#
print ("Ejercicio 1")
#----Constantes----#
PREGUNTA_NUMERO_1 = "Ingrese un primer numero :"
PREGUNTA_NUMERO_2 = "Ingrese un segundo numero :"
MENSAJE_MAYOR = "El numero 1 es mayor que el numero 2"
MENSAJE_IGUAL ="Numero 1 y Numero 2 son iguales"
MENSAJE_MAYOR_2 ="El numero 2 es mayor que el numero 1"
#----Entrada al codigo----#
Numero1 = int (input(PREGUNTA_NUMERO_1))
Numero2 = int (input(PREGUNTA_NUMERO_2))
isMayor = Numero1 > Numero2
isIguales = Numero1 == Numero2
Resultado = ""
if (isMayor):
    print (MENSAJE_MAYOR)
    Resultado = MENSAJE_MAYOR
elif (isIguales): 
    print (MENSAJE_IGUAL)
    Resultado = MENSAJE_IGUAL
else:
    print (MENSAJE_MAYOR_2)
    Resultado = MENSAJE_MAYOR_2

print (Resultado)

#----Ejercicio 2----#
print ("Ejercicio 2")
#----Constantes----#
PREGUNTA_EDAD = "Ingrese su edad, por favor :"
MENSAJE_MENOR_EDAD = "Tienes menos de 18 años, eres menor de edad"
MENSAJE_PERSONA_JOVEN = "Es usted una persona joven"
MENSAJE_ADULTO = "Es usted un adulto"
MENSAJE_ADULTO_MAYOR = "Es usted un adulto mayor"
#----Entrada al codigo----#
Edad = int (input(PREGUNTA_EDAD))
isMenorEdad = Edad < 18 
isPersonaJoven = Edad >= 18 and Edad <= 25
isAdulto = Edad >= 26 and Edad <= 60
isAdultoMayor = Edad > 60 
Resultado = ""
if (isMenorEdad):
    print (MENSAJE_MENOR_EDAD)
    Resultado = MENSAJE_MENOR_EDAD
elif (isPersonaJoven):
    print (MENSAJE_PERSONA_JOVEN)
    Resultado = MENSAJE_PERSONA_JOVEN
elif (isAdulto):
    print (MENSAJE_ADULTO)
    Resultado = MENSAJE_ADULTO
else:
    print (MENSAJE_ADULTO_MAYOR)
    Resultado = MENSAJE_ADULTO

print (Resultado)

#----Ejercicio 3----#
print ("Ejercicio 3")

#----Constantes----#
PREGUNTA_AÑO_ACTUAL = "Ingrese el año actual, por favor :"
PREGUNTA_AÑO_CUALQUIERA = "Ingrese un año cualquiera, por favor :"
#----Entrada al codigo----#
AñoActual = int (input (PREGUNTA_AÑO_ACTUAL))
AñoCualquiera = int (input(PREGUNTA_AÑO_CUALQUIERA))
isMayor = AñoCualquiera > AñoActual
isMayor2 = AñoActual > AñoCualquiera
if (isMayor):
    Resta = AñoCualquiera - AñoActual
    print (f"Faltan {Resta} años para llegar")
elif (isMayor2):
    Resta2 = AñoActual - AñoCualquiera
    print (f"Han pasado {Resta2} años")
else:
    print ("Los años son iguales")

#----Ejercicio 4----#
print ("Ejercicio 4")

#----Constantes----#
PREGUNTA_MEDIDA = "Ingrese una distancia en centimentros, por favor : "
PREGUNTA_UNIDADES = ''' Ingrese en que unidades desea transformar el valor :
      K - Kilometros
      M - Metros 
      mm -milimetros
'''
MENSAJE_ERROR = "Entrada no valida, repita el proceso"
#----Entrada al codigo----#
Medida = float (input(PREGUNTA_MEDIDA))
Unidades = input (PREGUNTA_UNIDADES)
#----Conversiones-----#
Metros = Medida / 100
Kilometros = Medida / 10**5
Milimetros = Medida * 10
if (Unidades == 'K'):
    print (Kilometros)
elif (Unidades == 'M'):
    print (Metros)
elif (Unidades == 'mm'):
    print (Milimetros)
else: 
    print (MENSAJE_ERROR)