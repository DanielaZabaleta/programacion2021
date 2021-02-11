PruebaV = True
PruebaF = False
print (PruebaF)
print (PruebaV)
PruebaV = PruebaF
print (PruebaV)
Edad = 18
Estatura = 1.60
Peso = 54 
NOMBRE = "Daniela Zabaleta Benitez"
print ("#"*15,"Mayor Edad","#"*15)
isMayorEdad = Edad >= 18
print (isMayorEdad)
print ("#"*15,"Bajo la Estatura promedio","#"*15)
isMayorEstatura = Estatura < 1.70
print (isMayorEstatura)
# Peso diferente de 54
print ("#"*15,"Peso diferente 54","#"*15)
isPesoDiferente = Peso != 54 
print (isPesoDiferente)
# Vamos a ver si un apellido esta en el nombre completo
apellido = "Zabaleta"
isApellido = apellido in NOMBRE
print (isApellido)