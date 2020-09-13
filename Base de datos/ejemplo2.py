import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

# Le damos un id unico inreppetible, y hacemos que se incremente solo
# Con UNIQUE le decimos que no puede estar repetido el valor de ese campo
# miCursor.execute('''
#     CREATE TABLE PRODUCTOS(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#         PRECIO INTEGER,
#         SECCION VARCHAR(20))
# ''')

# productos = [
    # ("AR01", "Pelota", 20, "Juguetería"),
    # ("AR02", "Pantalón", 15, "Confección"),
    # ("AR03", "Destornillador", 25, "Ferretería"),
    # ("AR04", "Jarrón", 45, "Cerámica")
#     ("Pelota", 20, "Juguetería"),
#     ("Pantalón", 15, "Confección"),
#     ("Pantalónes", 35, "Confección"),
#     ("Destornillador", 25, "Ferretería"),
#     ("Jarrón", 45, "Cerámica")
# ]
# Cargamos a la base de datos la lista
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'Tren', 15, 'Juguetería')")

# Leemos la información almacenada en la base de datos
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección'")
productos = miCursor.fetchall()
print(productos)

# Actualizamos un valor de la base de datos
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")

# Borramos un articulo
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

# Hacemos efectiva la carga
miConexion.commit()
miConexion.close()