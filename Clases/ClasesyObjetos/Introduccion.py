class Humano ():
    def __init__(self, nombreEntrada, edadEntrada, estaturaEntrada):
        print ('Hola soy un humano nuevo')
        self.raza = 'Humano'
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.estatura =  estaturaEntrada
        self.dinero = 0
    
    def hablar (self,mensaje):
        print (f'Hola soy {self.nombre} tengo un mensaje que decir...', mensaje)
    def mostarAtributos (self):
        print (f'''Mi nombre es {self.nombre}
        Mi estatura es {self.estatura} metros
        Mi edad es {self.edad} años
        Tengo ahorrado {self.dinero} pesos
        ''')
    def recorrerDistanacia (self,distanciaMetros):
        for i in range (distanciaMetros):
            print (f'Hola soy {self.nombre} y he recorrido {i+1} metros')

    def ahorrarDinero (self):
        preguntaIngresarMontos = 'Ingrese S --> para continuar añadiendo montos y N --> para finalizar: '
        preguntaMonto = 'Cuanto vas a ingresar?: '
        ingresarMontos = input (preguntaIngresarMontos)
        while (ingresarMontos != 'N'):
            monto = float (input (preguntaMonto))
            self.dinero = self.dinero + monto 
            print (f'Soy {self.nombre} y tengo {self.dinero} pesos')
            ingresarMontos = input (preguntaIngresarMontos)
        return self.dinero




humano1 = Humano ('Daniel', 27, 1.67)
humano2 = Humano ('Mafe', 27, 1.60)

humano1.hablar ('Espero que esten muy bien')
humano2.hablar ('Chao')
print (humano1.nombre)
print (humano2.nombre)
print (humano2.edad)
humano1.mostarAtributos ()
humano2.mostarAtributos ()
humano1.recorrerDistanacia (25)
totalAhorrado = humano2.ahorrarDinero ()
humano2.mostarAtributos ()