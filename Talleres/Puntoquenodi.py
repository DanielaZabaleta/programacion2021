#-----Punto 5-----#
def Fibonnaci (n):
    a = 0
    b = 1
    for elemento in range (n - 1):
        c = a + b
        a = b
        b = c
    return (b)
n = int (input('Ingrese la posicion que quiere saber: '))
Posicion = Fibonnaci (n)
print (Posicion)