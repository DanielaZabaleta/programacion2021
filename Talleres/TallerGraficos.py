#----Punto 1-----#
print ('Punto 1 - Grafico de Barras')
import matplotlib.pyplot as plt 
mes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 
'Octubre', 'Noviembre', 'Diciembre']
ingresos = [200, 480, 550, 500, 620, 680, 530, 700, 710, 790, 820, 900]
plt.bar (mes, ingresos, width = 0.6, color = 'c')

plt.title ('Niveles de ingresos 2020 (Mil $)')
plt.xlabel ('Meses')
plt.ylabel ('Ingresos')
plt.savefig ('grafico ingresos.png')

plt.show ()

#-----Punto 2-----#
print ('Punto 2 - Grafico de Torta')


def etiquetarElementosPorcentuales(sizes, labels, indicador= ' --> '):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len (labels)):
        porcentaje = round (sizes[i]/acumulador*100,2)
        pieLabels[i] += indicador + str(porcentaje) +'%'


pieExplode = [0.1,0,0,0,0]
acumulador = 0
pieLabels = ['Bogota', 'Medellin','Cali', 'Barranquilla', 'Cartagena']
sizes = [7743955, 2533424, 2252616, 1274250, 1028736]
etiquetarElementosPorcentuales(sizes,pieLabels)

plt.pie(sizes,labels=pieLabels, 
        explode=pieExplode, 
        shadow= True, 
        counterclock = True, 
        startangle= 90)

plt.title("Ciudades más pobladas de Colombia")
plt.show() 