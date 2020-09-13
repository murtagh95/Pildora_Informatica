from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

# Definición de variables
# Con StringVar le decimos que va a ser una variable de str
miNombre = StringVar()

# Le asociamos una variable al cuadro de texto
cuadroTexto = Entry(miFrame, textvariable=miNombre)
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

direccionLabel = Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
direccionTexto = Entry(miFrame)
direccionTexto.grid(row=3, column=1, padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, sticky="e", padx=10, pady=10)
# Contruimos un objeto de scroll para ingresarlo al Text
# en command hay que pasarle el contenedor y con un . si sera vertical u horizontal
scrollVertical = Scrollbar(miFrame, command=textoComentario.yview)
# Lo colocamos en pantalla, con este stiky se adaptara su tamaño
scrollVertical.grid(row=4, column=2, sticky="nsew")
# Le damos una correcta funcionalidad al scroll
textoComentario.config(yscrollcommand=scrollVertical.set)

def codigoBoton():
    # Le definimos una cadena a la variable
    miNombre.set("Nicolas")

# Con command le decimos que al precionar el boton ejecute dicha función
botonEnvio = Button(miFrame, text="Escribir", command=codigoBoton)
botonEnvio.grid(row=5, column=1)




root.mainloop()


