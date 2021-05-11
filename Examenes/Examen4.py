#----Punto 1-----#
print ('Punto 1 - Grafico de Barras')
import matplotlib.pyplot as plt

snacks = []
precios = []
for i in range (5):
    Snacks = input ("Agrega tu snack favorito : ")
    Precios = input ("Agrega el precio de ese snack : ")
    snacks.append (Snacks)
    precios.append (Precios)
    print (f"Realice este proceso {4-i} veces")

print (snacks)
print (precios)
plt.bar (snacks, precios, width = 0.6, color = 'c')

plt.title ('Snacks Favoritos')
plt.xlabel ('Snacks')
plt.ylabel ('Precios')
plt.savefig ('grafico snacks.png')

plt.show ()

#-----Punto 2-----#
print ('Punto 2 - Grafico de Torta')

Ciudades = []
Poblaciones  = []

for i in range (5):
    ciudad = input ("Agregue una de sus ciudades favoritas en el mundo :")
    poblacion = input ("Agregue la poblacion de esa ciudad: ")
    Ciudades.append (ciudad)
    Poblaciones.append (poblacion)
    print (f"Realice este proceso {4-i} veces")

print (Ciudades)
print (Poblaciones)
Maximo = Poblaciones.index (max (Poblaciones))
pieExplode = [0,0,0,0,0]

pieExplode [Maximo] = 0.1

plt.pie(Poblaciones,labels=Ciudades, 
        explode=pieExplode)
plt.title("Ciudades favoritas en el Mundo")
plt.savefig ('grafico ciudadesfavoritas.png')
plt.show() 

#----Punto 3----#
print ('Punto 3 - Grafico Curvas')

print ('ecg = Es la representación visual de la actividad eléctrica del corazón en función del tiempo, que se obtiene, desde la superficie corporal.')
print ('ppg = Es una técnica óptica simple usada para descubrir cambios volumétricos en sangre en la circulación periférica.')

import pandas as pd

ppgData = pd.read_csv ('ppg.csv', encoding= 'UTF-8', header= 0, delimiter= ';').to_dict ()
muestras = list (ppgData ['muestra'].values ())
valores = list (ppgData ['valor'].values ())
plt.plot (muestras, valores)
plt.xlabel ('Tiempo (ms)')
plt.ylabel ('Voltaje (mV)')
plt.title ('Fotopletismografia')
plt.savefig ('grafico ppg.png')
plt.show ()
##################################################
ecgData = pd.read_csv ('ecg.csv', encoding= 'UTF-8', header= 0, delimiter= ';').to_dict ()
muestras1 = list (ecgData ['muestra'].values ())
voltaje = list (ecgData ['valor'].values ())
plt.plot (muestras1, voltaje)
plt.xlabel ('Tiempo (ms)')
plt.ylabel ('Voltaje (mV)')
plt.title ('Electrocardiograma')
plt.savefig ('grafico ecg.png')
plt.show ()