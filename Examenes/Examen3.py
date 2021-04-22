#----Punto 1-----#
print ('Punto 1')
class ElementoDigital ():
    def __init__ (self, nombreEntrada, creadorEntrada, fechadePublicacion):
        self.nombre = nombreEntrada
        self.creador = creadorEntrada
        self.fecha = fechadePublicacion
    def mostrarAtributos (self):
        print (f'Hola, soy una {self.nombre}, mis creadores son {self.creador} y mi fecha de publicacion fue el {self.fecha}')

elementoDigital1 = ElementoDigital ('memoria', 'Paulina Y Daniela', 'Diciembre 2019')
elementoDigital1.mostrarAtributos ()

print ('#'*10)

class Usuario ():
    def __init__ (self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.sexo = sexoEntrada
        self.nacionalidad = nacionalidadEntrada
    def mostrarAtributos (self):
        print (f'Hola, soy {self.nombre}, tengo {self.edad} años, soy de sexo {self.sexo} y soy de nacionalidad {self.nacionalidad}')
    def cancionEscuchada (self, cancion):
        print (f'Hola soy {self.nombre} y estoy escuchando {cancion}')

usuario1 = Usuario ('Daniela', 18, 'femenino', 'colombiana')
usuario1.mostrarAtributos ()
usuario1.cancionEscuchada ('Adios')

print ('#'*10)

class Pagina ():
    def __init__ (self, tipodeContenido, formatoEntrada, fechadePublicacion):
        self.tipo = tipodeContenido
        self.formato = formatoEntrada
        self.fecha = fechadePublicacion
    def mostrarAtributos (self):
        print (f'Hola soy una pagina, mi tipo de contenido es {self.tipo}, tengo una formato {self.formato} y mi fecha de publicacion fue el {self.fecha}')

pagina1 = Pagina ('vlogs musicales', 'weblog', 'Octubre 2020')
pagina1.mostrarAtributos ()

print ('#'*10)

#---Punto 2----#
print ('Punto 2')
class Cancion (ElementoDigital): 
    def __init__ (self, nombreEntrada, creadorEntrada, fechadePublicacion, generoMusical, duracionenSegundos):
        ElementoDigital.__init__ (self, nombreEntrada, creadorEntrada, fechadePublicacion )
        self.genero = generoMusical
        self.duracion = duracionenSegundos
        print (f'Hola soy una nueva cancion, mi nombre es {self.nombre} y mi fecha de creacion fue el {self.fecha}')
    def bucleCancion (self, cantidad):
        for i in range (cantidad):
            print (f'Cancion {self.nombre} sonando {i+1} vez')

cancion1 = Cancion ('Adios', 'Sebastian Yatra', '14 Enero 2021', 'Pop', 240)
cancion1.bucleCancion (5)

print ('#'*10)

class Artista (Usuario):
    def __init__ (self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada, generoMusical, numerodeCancionesPublicadas, numerodeAlbums):
        Usuario.__init__ (self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada)
        self.genero = generoMusical
        self.numeroCanciones = numerodeCancionesPublicadas
        self.albums = numerodeAlbums
    def concierto (self, ciudad):
        print (f'Hoy habra una concierto del nuevo artista en la ciudad de {ciudad}')

artista1 = Artista ('Daniela', 18, 'femenino', 'colombiana', 'Pop', 28, 3)
artista1.concierto ('Medellin')

print ('#'*10)

class Favoritos (Pagina):
    def __init__ (self, tipodeContenido, formatoEntrada, fechadePublicacion, favoritosdelaComunidad, fechadeUltimaActualizacion):
        Pagina.__init__ (self, tipodeContenido, formatoEntrada, fechadePublicacion)
        self.favoritos = favoritosdelaComunidad
        self.fechaActualizacion = fechadeUltimaActualizacion
    def agregarCancion (self, cancion, actualizacion):
        self.favoritos.append (cancion)
        self.fechaActualizacion = actualizacion
    def mostrarEliminarLista (self, cancionEliminada):
        print(self.favoritos)
        self.favoritos.pop (cancionEliminada)

favoritas = ['An', 'Pb', 'Cr', 'Da']
favoritos1 = Favoritos('cancion','mp3',2020,favoritas,2021)
favoritos1.mostrarEliminarLista(3)
favoritos1.agregarCancion('Cancion nueva agregada',2021)
print (favoritos1.favoritos)

#Daniela Zabaleta 
#Paulina Florez 