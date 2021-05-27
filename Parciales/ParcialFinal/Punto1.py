#---- Punto 1 ----# 
print ('Punto 1 - Grafico de Barras')
import matplotlib.pyplot as plt 

def agregarAlimentos (pregunta1, pregunta2):
    alimentos =[]
    precios = [] 
    for i in range (8):
        print (f'Ingresando dato {i+1} de 8')
        alimentos.append (input(pregunta1))
        precios.append (input(pregunta2))
    return alimentos, precios 

Alimentos = 'Ingrese su alimento favorito: '
Precios = 'Ingrese el precio del alimento: '

alimentos, precios = agregarAlimentos(Alimentos, Precios)
print (alimentos, precios)
plt.bar (alimentos, precios, width = 0.6, color = 'c')
plt.title ('Alimentos Favoritos')
plt.xlabel ('Alimentos')
plt.ylabel ('Precios')
plt.savefig ('grafico alimentos.png')

plt.show ()