# Llamamos a la biblioteca pickle
import pickle

lista_nombres = ["Nicolas", "Pedro", "Ana", "María", "Isable"]

# Creamos un fichero externo en escritura binaria
fichero_binario = open("lista_nombres", "wb")  # La wb es para escritura binaria

# Le debemos pasar 2 parametros, 1º la lista u objeto a guardas
# 2º El nombre del fichero 
pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()
# Borramos el fichero de memoria una vez cerrado
del(fichero_binario)


fichero = open("lista_nombres", "rb")  # La rb es por lectura binaria
# Guardamos en una variable lo contenido en el archivo binario
lista = pickle.load(fichero)

print(lista)

fichero.close()
