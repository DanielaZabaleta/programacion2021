class Gecko ():
    '''Especies de lagartos pequeños que pertenecen a un infraorden de reptiles escamosos.
    Lo caraterizan varios atributos que los fiferencian entre ellos:
    nombreEntrada: Hace referencia al nombre del Gecko
    generoEndrada: Hace referencia si es macho o hembra 
    habitatEntrada: Hace referencia al entorno en el que se desarrolla
    especieEntrada: Hace referencia a la categoria a la que pertenece por sus cualidades
    colorEntrada: Hace referencia al color de su cuerpo
    tamañoEntrada: Hace referencia al tamaño de su cuerpo 
    pesoEntrada: Hace refrencia al peso total de su cuerpo 


    Tiene las siguientes acciones: 
    * comer (alimento):
        Describe con que se alimenta 
    * mostrarAtributos ():
        Muestra los atributos de los pequeños lagartos
        ''' 
    def __init__ (self, nombreEntrada, generoEndrada, habitatEntrada, especieEntrada, colorEntrada, tamañoEntrada, pesoEntrada):
        print ("Hola, soy un gecko muy tranquilo")
        self.nombre = nombreEntrada
        self.genero = generoEndrada
        self.habitat = habitatEntrada
        self.especie = especieEntrada
        self.color = colorEntrada
        self.tamaño = tamañoEntrada
        self.peso = pesoEntrada
    def comer (self, alimento):
        print (f'Hola soy {self.nombre} y mi especie es la {self.especie}, me gusta comer ', alimento)
    def mostrarAtributos (self):
        print (f'''Hola, mi nombre es {self.nombre}
        Mi genero es {self.genero}
        Mi habitat es {self.habitat} 
        Mi especie es {self.especie}
        Mi color es {self.color}
        Mi tamaño es de {self.tamaño} cm
        Mi peso es de {self.peso} gr
        ''')


gecko1 = Gecko ('Leo','macho','casa','Leopardo','amarillo con manchas oscuras', 20, 60)
gecko1.mostrarAtributos ()
gecko1.comer = ('grillos, saltamontes o gusanos')