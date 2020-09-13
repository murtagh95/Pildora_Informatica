import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

# Buscamos una cadena dentro de otra, 1º parametro cadena a buscar
# 2º parametro cadena donde se realizara la busqueda, devuelve un 
# objeto si lo encuentra o None si no.
print(re.search("aprender", cadena))

textoBuscar = "aprender"

if re.search(textoBuscar, cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

# Almaceno el objeto en una var
textoEncontrado = re.search(textoBuscar, cadena)
# start devuelve el indice donde empieza a encontrar el str
print(textoEncontrado.start())
# end devuelve el indice donde termina el str
print(textoEncontrado.end())
# span devuelve una tupla con el nº de inicio y fin
print(textoEncontrado.span())

textoBuscar = "Python"
# findall nos devuelve un array con los elemetos encontrados
print(re.findall(textoBuscar, cadena))
# De esta manera obtenemos el nº de veces que se repite
print(len(re.findall(textoBuscar, cadena)))

lista_nombres = [
    "http://pilporasinformaticas.es",
    "ftp://pilporasinformaticas.es",
    "http://pilporasinformaticas.com",
    "ftp://pilporasinformaticas.com",
    "http://informaticaenespaña.es",
    "Hombres",
    "Mujeres",
    "Mascotas",
    "Niños",
    "Niñas",
    "camion",
    "camión"
]

for elemento in lista_nombres:
    # Con ^ le decimos que busque los que empiezen con...
    if re.findall("^ftp", elemento):
        print("Empieza: "+ elemento)

    if re.findall('es$', elemento):
        print("Termina: " + elemento)

    if re.findall("[ñ]", elemento):
        print("Contiene ñ: ", elemento)

    if re.findall("Niñ[oa]s", elemento):
        print("Busqueda especifica",elemento)

    if re.findall("cami[oó]n", elemento):
        print("Busqueda especifica",elemento)
    
print("----------------------")

lista = [
    "Ana",
    "Pedro",
    "María",
    "Rosa",
    "Sandra",
    "Celia"
]

for elemento in lista:
    # Imprimimos solo los que tienen letras desde la o a la t
    if re.findall("[o-t]", elemento):
        print(elemento)
    
    if re.findall("^[O-T]", elemento):
        print(elemento)

print("------------------")

lista1 = [
    "Ma1",
    "Se1",
    "Ba1",
    "Ma2",
    "Va1",
    "Ma3",
    "Va2",
    "Ma4",
    "Se2",
    "MaA",
    "Ma5",
    "MaB",
    "MaC",
    "MaD"
]

for elemento in lista1:
    if re.findall("Ma[0-3]", elemento):
        print(elemento)
    
    # Con ^ lo negamos
    # if re.findall("Ma[^0-3]", elemento):
    #     print(elemento)

    if re.findall("Ma[0-3A-B]", elemento):
        print(elemento)

        