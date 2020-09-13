import pickle

# Necesitamos cargar la clase para que los objetos que estan en el documento
# puedan ser instanciados o creados
class Vehiculo():
    # Definimos las propiedades
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    # Definimos los métodos
    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enMarcha)
        print("Acelerando:", self.acelera, "\nFrenando:", self.frena)


# Volvemos a abri el archivo
ficheroApertura = open("losCoches", "rb")

# Guardamos la información dle archivo en una variable
misCoches = pickle.load(ficheroApertura)

# Cerramos el fichero
ficheroApertura.close()
# Y lo borramos de la memoria
del(ficheroApertura)

# Reccoremos la lista con los objetos
for c in misCoches:
    print(c.estado())
