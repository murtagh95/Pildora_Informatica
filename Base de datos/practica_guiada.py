from tkinter import *
from tkinter import messagebox
import sqlite3

# -------------FUNCIONES----------------------

def conexionBBDD():
    # Creamos el archivo de la base de datos
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    
    # Solo se puede crear el archivo una vez, si ya esta cargado genera un erro
    try:
        miCursor.execute('''
        CREATE TABLE DATOS_USUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100)
            )
        ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")

    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")
    
def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if valor == "yes":
        root.destroy()

def limpiarCampos():
    miNombre.set("")
    miID.set("")
    miApellido.set("")
    miDireccion.set("")
    miContra.set("")
    textoComentario.delete(1.0, END)

def crear():
    miConexion =sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    # miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,\
    #      '" + miNombre.get() +"', '"+ miContra.get()+"', '"+ miApellido.get()+"',\
    #           '"+ miDireccion.get()+"', '"+ textoComentario.get("1.0", END)+"')")

    # CONSULTA PARAMETRICA
    datos = miNombre.get(), miContra.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END)
    miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, ?, ?, ?, ?, ?)",(datos))

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():
    miConexion =sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    # Buscamos los registros que coincidan con el id enviado
    miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID="+ miID.get())
    # Creamos el array con todos los registros y la guardamos en una var
    elUsuario = miCursor.fetchall()

    try:
        # Asignamos los valores del array a las variables utilizadas para visualizar
        miID.set(elUsuario[0][0])
        miNombre.set(elUsuario[0][1])
        miContra.set(elUsuario[0][2])
        miApellido.set(elUsuario[0][3])
        miDireccion.set(elUsuario[0][4])
        textoComentario.insert(1.0,elUsuario[0][5])

        miConexion.commit()

    except:
        messagebox.showerror("¡ERROR!", "No se encontro ningun usuario con ese ID")

def actualizar():
    miConexion =sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    datos = miNombre.get(), miContra.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END)
    miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?"+\
        "WHERE ID="+ miID.get(), (datos))

    # miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=\
    #      '" + miNombre.get() +"', PASSWORD='"+ miContra.get()+"', APELLIDO='"+ miApellido.get()+"',\
    #           DIRECCION='"+ miDireccion.get()+"', COMENTARIOS='"+ textoComentario.get("1.0", END)+"'\
    #               WHERE ID="+ miID.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con éxito")

def eliminar():
    miConexion =sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID="+ miID.get())
    miConexion.commit()
    messagebox.showinfo("DDBB", "Registro con ID:"+ miID.get() +" borrado con éxito")


root = Tk()

# Creo el menu
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Incluimos los elementos del menu
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

# Agrego las obciones al menu
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUDE", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ------------DEFINO VARIABLES-----------------------
miID = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miContra = StringVar()
miDireccion = StringVar()


# -----------Comienzo en creacion de campos------------

miFrame = Frame(root)
miFrame.pack()

cuadroID = Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, fg="red", justify="center", textvariable= miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10,)

cuadroContra = Entry(miFrame, textvariable=miContra)
cuadroContra.grid(row=2, column=1, padx=10, pady=10)
# Al escribir en el texto si visualizara un ?
cuadroContra.config(show="?")

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
# Le agrego la barra de desplazamiento
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

# ----------- Aquí comienzan los label---------------

idLabel = Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

contraLabel = Label(miFrame, text="Password:")
contraLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel = Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# ------------Creamos los botones de parte inferior------------

miFrame2 = Frame(root)
miFrame2.pack()

botonCrear = Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonActualizar = Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonBorrar = Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)


root.mainloop()