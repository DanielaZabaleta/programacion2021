
for iteracion in range (10):
    print(iteracion)
print ('#'*60)
for iteracion in range (10):
    print (iteracion+1)
print ('#'*60)
for iteracion in range (1,11):
    print (iteracion) 
print ('#'*60)
for iteracion in range (1,10,2):
    print (iteracion)

Residuo = 5%4
print (Residuo)

print('#'*60)
for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print (iteracion)

print('#'*60)
for iteracion in range (1,11):
    if (iteracion % 2 != 0):
        print (iteracion)

print('#'*60)
for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print (iteracion, '--> Es un numero par')
    else: 
        print (iteracion, '--> Es un numero impar')
print('#'*60)
Rango = int (input('Ingrese el rango maximo : '))

Opcion = int(input ('''
    1- Ver solo impares
    2- Ver solo pares
    3- Ver las dos clasificaciones
    n- Cualquier numero para mostrar nada
'''))
print('#'*60)
if (Opcion == 1):
    for iteracion in range (1,Rango+1):
        if (iteracion % 2 != 0):
            print (iteracion)
elif (Opcion == 2):
    for iteracion in range (1,Rango+1):
        if (iteracion % 2 == 0):
            print (iteracion)
elif (Opcion == 3):
    for iteracion in range (1,Rango+1):
        if (iteracion % 2 == 0):
            print (iteracion, '--> Es un numero par')
        else: 
            print (iteracion, '--> Es un numero impar')
else:
    print('Mostrando nada')
