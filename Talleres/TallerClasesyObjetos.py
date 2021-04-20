#-----Punto 1-----#
print ('Punto 1')
class Torta ():
    def __init__ (self, saborEntrada, alturaEntrada, formaEntrada):
        self.sabor = saborEntrada
        self.altura = alturaEntrada
        self.forma = formaEntrada 
    def mostrarAtributos (self):
        print (f''' Atributos de la torta
        Su sabor es de {self.sabor}
        Tiene una altura de {self.altura} cm
        Tiene una forma {self.forma}
        ''')

torta1 = Torta ('chocolate', 10, 'circular')
torta1.mostrarAtributos ()

#----Punto 2----#
print ('Punto 2')
class Estudiante ():
    def __init__ (self, edadEntrada, nombreEntrada, idEntrada, carreraEntrada, semestreEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
    def estudiarMateria (self, materia, horasEstudiar):
        print (f'Hola soy {self.nombre} y procedo a estudiar {materia} por {horasEstudiar} horas')

estudiante1 = Estudiante (18, 'Daniela', 1006615197, 'Ingenieria Biomedica', 3)
estudiante1.estudiarMateria ('programacion', 2)

#----Punto 3----#
print ('Punto 3')
class Nutricionista ():
    def __init__ (self, edadEntrada, nombreEntrada, universidadEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.universidad = universidadEntrada
    def imcPaciente (self, peso, altura ):
        return round (peso/(altura**2))

nutricionista1 = Nutricionista (25, 'Paola', 'CES')
print (nutricionista1.imcPaciente (53, 1.61))

#-----Punto 4-----#
print ('Punto 4')
class Canguro ():
    def __init__ (self, edadEntrada, idEntrada, nombreEntrada):
        self.edad = edadEntrada
        self.id = idEntrada
        self.nombre = nombreEntrada
    def saltar (self, saltos):
        for i in range (saltos):
            print (f'El canguro {self.nombre} ha dado {i+1} salto')

canguro1 = Canguro (15, 1006147, 'Bambi')
canguro1.saltar (5)

#-----Punto 5-----#
print ('Punto 5')
class Guitarra ():
    def __init__ (self, marcaEntrada, tipoEntrada, materialEntrada, colorEntrada):
        self.marca = marcaEntrada
        self.tipo = tipoEntrada
        self.material = materialEntrada
        self.color = colorEntrada
    def interpretar (self, cancion):
        print (f'Interpretacion de la cancion {cancion}')

guitarra1 = Guitarra ('Yamaha FX370C', 'Acustica', 'Caoba', 'Negro')
guitarra1.interpretar ('Adios')