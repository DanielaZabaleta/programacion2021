import matplotlib.pyplot as plt

tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9,10]
plt.plot (tiempo, sensor, 'r')
############
plt.title ('Grafico sensor contra el tiempo')
plt.xlabel ('Tiempo (s)')
plt.ylabel ('Voltaje (mV)')
plt.savefig ('Sensor.png')
############
plt.show ()

diccionario = {}
diccionario ['NombresEstudiantes'] = ['Jacobo', 'Dani', 'Maria', 'Elena']
diccionario ['EdadEstudiantes'] = [18, 17, 24, 32]
diccionario ['Peso'] = [84, 56, 64, 67]
print (diccionario)

print (diccionario ['NombresEstudiantes'][-1], diccionario ['EdadEstudiantes'][-1], diccionario ['Peso'][-1])