#Graficos Pie
#Importamos la libreria 
import matplotlib.pyplot as plt 
#Creamos los labels, sizes y explode 
#Labels: Python, java, dart, js (Nombres porciones de torta/etiquetas)
pieLabels = ['python', 'java', 'dart', 'js']
#Sizes: Los tamaños de cada porcion de la torta 
sizes = [50,25,15,10]
#Explode: Que tan alejado del origen esta la torta
pieExplode = [0,0,0.2,0]

def etiquetarElementosPorcentuales(sizes, labels, indicador= '->'):
    acumulador = 0 
    for elemento in sizes: 
        acumulador += elemento
    for i in range (len(pieLabels)):
        pieLabels [i] += '->' + str (sizes[i]/acumulador*100) + '%'
etiquetarElementosPorcentuales(sizes,pieLabels,'->')
#Diferentes formas
plt.pie (sizes, 
labels= pieLabels, 
explode= pieExplode, 
shadow= True, 
counterclock= True, 
startangle= 45)
##################################
plt.title ('Uso de lenguajes de programacion en el 2021')
plt.savefig ('Tortas lenguajes.png')
##################################
plt.show ()