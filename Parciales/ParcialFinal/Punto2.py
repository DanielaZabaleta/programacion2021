#---- Punto 2 ----#
print ('Punto 2')

class Humano ():
    def __init__(self, nombreEntrada,sexoEntrada, edadEntrada):
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
        self.edad = edadEntrada
    def mostrarAtributos (self):
        print (f'''Mi nombre es {self.nombre}
        Mi sexo es {self.sexo}
        Mi edad es {self.edad} años ''')
    def hablar (self,mensaje):
        print (f'Hola soy {self.nombre} tengo un mensaje que decir...', mensaje)

humano1 = Humano ('Daniela', 'femenino', 18)
humano1.mostrarAtributos ()
humano1.hablar ('Hola, espero que estes teniendo un buen dia.')

class Doctor (Humano):
    def __init__(self,nombreEntrada, sexoEntrada,edadEntrada):
        Humano.__init__ (self, nombreEntrada, sexoEntrada, edadEntrada) 
    def calcularIMC (self, pesoIn, estaturaIn):
        imc = pesoIn/(estaturaIn**2)
        Informacion = f'El IMC calculado es de {imc}'
        return Informacion

Doctor1 = Doctor('Daniela', 'femenino', 24)
imc = Doctor1.calcularIMC(53, 1.61)
print (imc)