#Explicacion de como hacer un grafico de barras 
import matplotlib.pyplot as plt 
lenguajes = ['py', 'java', 'dart', 'ts', 'elixir']
encuesta = [50, 10, 20, 10, 10]
plt.bar (lenguajes, encuesta, width = 0.6, color = 'c')
###################
#titulo
plt.title ('Lenguajes más usados')
plt.xlabel ('Leguajes de programación')
plt.ylabel ('% de uso de lenguajes')
plt.savefig ('grafico lenguajes.png')
###################
plt.show ()