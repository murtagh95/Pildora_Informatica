# Traemos la libreria encargada de serializar
import pickle

class Persona():
    # Generamos los atributos de la clase
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)

    # str: Convierte en cadena de texto la información de un objeto
    def __str__(self):
        return "Nombre: {} ,Genero: {} ,Edad: {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        # Llevamos el cursor al inicio del archivo
        listaDePersonas.seek(0)
        
        # Le defimos que intente de leer la información, ya que si es la primera
        # vez que se realiza dara un erro
        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersonas(self, p):
        # Agregamos a la lista de personas la Persona pasada al método
        self.personas.append(p)
        # Guardo la lista en el archivo
        self.guardarPersonasEnFicheroExterno()
    
    def guardarPersonasEnFicheroExterno(self):
        # Abrimos el archivo en modo escritura
        ListaPersonas = open("ficheroExterno", "wb")
        # Agregamos la lista al archivo
        pickle.dump(self.personas,ListaPersonas)
        # Cerramos el archivo y lo borramos de memoria
        ListaPersonas.close()
        del(ListaPersonas)


    def mostrarPersonas(self):
        # Recorremos la lista y mostramos cada elemetno
        for p in self.personas:
            # Al colocar el metodo __str__ en la clase, el objeto al ser
            # llamado visualizara el contenido de dicho método
            print(p)

# Creamos el objeto que guardara una listas de los objetos de la clase Persona
miLista = ListaPersonas()

p = Persona("Miriam", "Femenino", 55)
p2 = Persona("Julio", "Masculino", 78)
p3 = Persona("Walter", "Masculino", 15)
p4 = Persona("Mercedes", "Femenino", 20)

# Agregamos los objetos a la lista
# miLista.agregarPersonas(p)
# miLista.agregarPersonas(p2)
# miLista.agregarPersonas(p3)
# miLista.agregarPersonas(p4)

# Usamos el método para mostrar la lista
miLista.mostrarPersonas()

