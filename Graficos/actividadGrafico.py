#Actividad Grafica
import matplotlib.pyplot as plt 
bl = ['TOL', 'Sotus S', 'LBC', 'Sotus', '2Gether']
visualizaciones = [124, 133, 197, 245, 259]
plt.bar (bl, visualizaciones,width = 0.6, color = 'c')

plt.title ('BL con más visualizaciones en el 2020')
plt.xlabel ('Nombres de BL')
plt.ylabel ('# de millones de visualizaciones en la plataforma')
plt.savefig ('Grafico BL.png')

plt.show ()