import re

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"
nombre4 = "sandra Martinez"
nombre5 = "Jara Martinez"
nombre6 = "Lara Martinez"
nombre7 = "154616"
nombre8 = "a154616"

codigo1 = "sahdfiusabdfiuasdbi71aksjdhfiusadhflashd"
codigo2 = "saidbfiasdb71afasdfilnasdkflasnd  asdfika es"
codigo3 = "asdfbsaidfb asdfkbasiugkhnaps vaiesukjfwieufbasf"

# match busca coincidencia al inicio de la cadena
if re.match("Sandra", nombre1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado el nombre")
# Hacemos que identifique mayusculas como minusculas
if re.match("Sandra", nombre4, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado el nombre")
# Con el . le decimos que ignore ese caracter
if re.match(".ara", nombre5, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado el nombre")
# Con \d busca si empieza con un número
if re.match("\d", nombre7):
    print("Hemos encontrado el número")
else:
    print("No lo hemos encontrado el número")

# ------------BUSQUEDA CON SEARCH------------
# busca en todo el str no solo al inicio
if re.search("López", nombre1):
    print("Hemos encontrado el apellido")
else:
    print("No lo hemos encontrado el apellido")

if re.search("71", codigo3):
    print("Hemos encontrado el 71")
else:
    print("No lo hemos encontrado el 71")




