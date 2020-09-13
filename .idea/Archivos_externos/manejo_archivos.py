# Cargamos la libreria predeterminada de python para leer archivos
from io import open

# Abrimos un archivo externo, recibe varios parametros, 1º nombre del archivo
# 2º el modo en el que abriremos el archivo(lectura, escritura, agregar)
# archivo_texto = open("archivo.txt", "w")  # La w es por escritura

# frase = "Estupendo día para estudiar Python \n El miércoles"

# Incluimos el str en el archivo
# archivo_texto.write(frase)

# Cerramos el archivo
# archivo_texto.close()


# Abrimos el archivo en modo lectura
archivo_texto = open("archivo.txt", "r")  # La r es por lectura

# Cambiamos la posición del cursor
# archivo_texto.seek(11)
# texto = archivo_texto.read()
print(archivo_texto.read())

# Cambiamos la posición del cursor
archivo_texto.seek(0)

# El primer read deja el cursor al final del archivo, si queremos volver
# a leer el archivo no podremos por el lugar del puntero
# Le decimos que leea hasta el caracter 11, deja el cursor en dicha posición
print(archivo_texto.read(11))
# lineas_texto = archivo_texto.readlines()

# Colocamos el cursor justo en el medio del archivo
archivo_texto.seek(len(archivo_texto.read())/2)
print("Mitad del archivo: ", archivo_texto.read())

# Cerramos el archivo
archivo_texto.close()

# print(texto)
# print(lineas_texto)


# archivo_texto = open("archivo.txt", "a")  # La a es por agregar

# Agregamos el siguiente texto al archivo   
# archivo_texto.write("\nSiempre es un una buena ocación para estudiar Python")

# archivo_texto.close()


archivo_texto = open("archivo.txt", "r+")  # La r+ es por lectura y escritura

# print(archivo_texto.readlines())
lista_texto = archivo_texto.readlines()

lista_texto[1] = " .Esta línea ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

# Este método tinene que recibir una lista
archivo_texto.writelines(lista_texto)

# Esto sobrescrive el texto atual
# archivo_texto.write("Comienzo de texto")

archivo_texto.close()

