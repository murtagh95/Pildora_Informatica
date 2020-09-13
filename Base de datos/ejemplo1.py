import sqlite3

# Abrimos/Creamos la conección
miConexion = sqlite3.connect("PrimeraBase")

# Creamos el cursor/puntero
miCursor = miConexion.cursor()

# Creamos una tabla llamada productos con 3 campos, nombreArt, precio, sccion
# Una ves creada la tabla si volvemos a ejecutar el codigo se genera un error
# miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTERGER, SECCION VARCHAR(20))")

# Insertamso datos
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
variosProducos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 40, "Cerámica"),
    ("Camión", 20, "Juguetería")
]
# Agregamos la lista a la bse de datos
# Debemos colocar un ? por cada elemento columna de la tabla
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProducos)
# Cada vez que realizamos un cambio hay que verificar
# miConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTOS")
variableProductos = miCursor.fetchall()
for producto in variableProductos:
    print("Nombre Artículo:", producto[0])
    print("Sección:", producto[2])
    print("Precio:", producto[1])
    print("------------------------------")

# Cerramos la conección
miConexion.close()