#----Punto 1----#
print ('Punto 1')
class Persona ():
    def __init__ (self, nombreEntrada, edadEntrada, idEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEntrada
    def hablar (self, mensaje):
        print (f'Hola soy {self.nombre} tengo un mensaje que decir...', mensaje)
    def caminar (self, pasos):
        for i in range (pasos):
            print (f'Hola soy {self.nombre} y he caminado {i+1} pasos')

persona1 = Persona ('Daniela', 18, 1006615197)
persona1.hablar ('Espero que esten muy bien')
persona1.caminar (12)

#-----Puntp 2-----#
print ('Punto 2')
class Doctor (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, especialidadEntrada):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.especialidad = especialidadEntrada
    def mostrarAtributos (self):
        print (f'Soy el doctor {self.nombre}, tengo {self.edad} años, me especialice en {self.especialidad} y mi identificacion es {self.id}')
    def enfermedadTratada (self, enfermedad):
        print (f'Soy el doctor {self.nombre} y procedo a tratar la {enfermedad}')

doctor1 = Doctor ('Pablo', 29, 100244578, 'Dermatologia')
doctor1.mostrarAtributos ()
doctor1.enfermedadTratada ('Urticaria')

#-----Punto 3-----#
print ('Punto 3')
class Nutricionista (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, universidadEgresado):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.universidad = universidadEgresado
    def mostrarAtributos (self):
        print (f'Soy la nutricionista {self.nombre}, tengo {self.edad} años, mi identificacion es {self.id} y soy egresada de la universidad {self.universidad}')
    def imcPaciente (self, peso, altura):
        return round (peso/(altura**2))

nutricionista1 = Nutricionista ('Paola', 25, 100615578, 'CES')
nutricionista1.mostrarAtributos ()
print (nutricionista1.imcPaciente (53, 1.61))

#-----Punto 4-----#
print ('Punto 4')
class Abogado (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, especialidadEntrada, universidadEgresado):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.especialidad = especialidadEntrada
        self.universidad = universidadEgresado
    def mostrarAtributos (self):
        print (f'Soy el abogado {self.nombre}, tengo {self.edad} años, me identifico con el numero {self.id}, me especialice en {self.especialidad} y soy egresado de la universidad {self.universidad}')
    def casoRepresentado (self, nombre, caso):
        print (f'Soy el abagodo {self.nombre} y procedo a representar al cliente {nombre} en el caso de {caso}')

abogado1 = Abogado ('Julio', 29, 102576866, 'derecho penal', 'UPB')
abogado1.mostrarAtributos
abogado1.casoRepresentado ('Antonio', 'Homicidio culposo')