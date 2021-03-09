Nombres = []
print (type (Nombres))
print (Nombres)
Nombres = ['Santi', 'Samuel', 'Aleja', 'Elsa']
print (Nombres)
print (Nombres [2])
Nombres.append ('Mauricio')
print (Nombres)
print (Nombres[2])
Edades = [18,19,20,17,32]
Estaturas = [1.62,1.80,1.67,1.98]
#Al ultimo
print (Edades[-2])
print (Edades[0:2])
print (Edades[:3])
print (Edades[2:])
print (Edades[:])
Edades.sort ()
print (Edades)
Edades.sort(reverse=True)
print (Edades)
Mayor = max(Edades)
print (Mayor)
Menor = min (Edades)
print (Menor)
#Como contamos cuantos elementos hay?
LargoListaEdades = len(Edades)
print (LargoListaEdades)
#Como sumamos elementos?
SumaEdades = sum(Edades)
print (SumaEdades)
#Como calculo el promedio?
PromedioEdades = SumaEdades/LargoListaEdades
print (PromedioEdades)
#Eliminar un elemento 
Edades.pop (2)
print (Edades)

#Ciclos for y las listas#
LargoListaEdades = len(Edades)
for indice in range (LargoListaEdades):
    print ('Estpy en la posicion',
    indice, 'Valgo',
    Edades[indice])
LargoListaNombres = len (Nombres)
for indice in range (LargoListaNombres):
    print (Nombres[indice])

PosicionesConValoresPares = []
LargoListaEdades = len(Edades)
for posicion in range (LargoListaEdades):
    if (Edades[posicion]%2 == 0):
        PosicionesConValoresPares.append (posicion)

print (Edades)
print (PosicionesConValoresPares)

#Solo cuando les interese mostrar la lista
Posicion = 0
for Edad in Edades:
    print (Edad)
    Posicion+=1
for Nombre in Nombres:
    print (Nombre)
    print (Posicion)
    Posicion+=1

Posicion = 0 
PosicionesPares = []
for Edad in Edades:
    if (Edad %2 == 0):
        PosicionesPares.append (Posicion)
        Posicion+=1
print (PosicionesPares)