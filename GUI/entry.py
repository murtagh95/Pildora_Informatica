from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

cuadroTexto = Entry(miFrame)
# cuadroTexto.place(x=100, y=100)
# grid recibe dos parametros, fila y columna empezando en 0
# Con sticky le indicamos en que posición se debe alinear, se deben pasar los valores de 
# n: norte/arriba -- e: este/derecha  --  s: sur/abajo  --  w: oeste/izquierda
cuadroTexto.grid(row=0, column=1, padx=10, pady=10)
# Cambiamos alguna configuracion como el color de la letras y la alineación
cuadroTexto.config(fg="red", justify="center")


nombreLabel = Label(miFrame, text="Nombre:")
# nombreLabel.place(x=100, y=100)
# Con padx y pady le damos un espacio entre elementos
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

contraLabel = Label(miFrame, text="Contraseña:")
contraLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
contraTexto = Entry(miFrame)
contraTexto.grid(row=1, column=1, padx=10, pady=10)
# Agregamos la configuración en el Entry para que se vea el texto como contraseña
contraTexto.config(show="*")

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
apellidoTexto = Entry(miFrame)
apellidoTexto.grid(row=2, column=1, padx=10, pady=10)
# Agregamos un texto, 1º parametro una posición y 2º una cadena
apellidoTexto.insert(0, "Catalano")
segundoApellido = " Salimeni"
# apellidoTexto.insert(8, segundoApellido)
# Le podemos especificar que la posición sea la última
apellidoTexto.insert(END, segundoApellido)
# Seleccionamos el texto desde uyna posición hasta otra, focus lo hacemos efectivo
apellidoTexto.select_range(0, END)
apellidoTexto.focus()
# Obtenemos la posición del cursor
print(apellidoTexto.index(INSERT))
# Coloco el cursor en un punto especifico y despues lo pongo en 'efecto'
apellidoTexto.icursor(7)
apellidoTexto.focus()


direccionLabel = Label(miFrame, text="Direccion de casa:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
direccionTexto = Entry(miFrame)
direccionTexto.grid(row=3, column=1, padx=10, pady=10)
# Desabilitamos el acceso a la caja de texto
# direccionTexto.config(state="disabled")

def obtenerSeleccion():
    # Comprobamos que haya una selección
    if direccionTexto.select_present():
        # Obtener los indices del inicio y fin de la selección
        primero = direccionTexto.index(SEL_FIRST)
        segundo = direccionTexto.index(SEL_LAST)
        print(direccionTexto.get()[primero:segundo])
    else:
        print("No hay selección.")

botonSeleccion = Button(miFrame, text="Obtener selección", command=obtenerSeleccion)
botonSeleccion.grid(row=3, column=2)

# Obtenemos la información de la caja de texto 
button = Button(miFrame, text="Obtener texto", command=lambda: print(direccionTexto.get()))
button.grid(row=4, column=1)

# Tk nos provee la clase tk.StringVar() para crear objetos que actúan como una cadena, con la 
# excepción de que para asignarle un valor usamos el método set() y, para obtenerlo, get().
var = StringVar()  # Genero la variable
var.set("¡Hola, mundo!")  # Escribo en la variable con método set
print(var.get())  # Leo la variable con el método get

# Podemos asociar una variable de estas características a una caja de texto al momento de su creación, vía el parámetro textvariable
entry = Entry(miFrame, textvariable= var)
entry.grid(row=5, column=1)


root.mainloop()