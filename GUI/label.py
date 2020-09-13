# Traemos la libreria encargada de la GUI
from tkinter import *

# Creamos la ventana
root = Tk()

# Creamos el Frame dentro del root y con unas medidas
miFrame = Frame(root, width=500, height=400)
# Empaquetamos el Frame
miFrame.pack()

# Creamo un label. le especificamos el contenedor padre
miLabel = Label(miFrame, text="Hola alumnos de Python")
# Empaquetamos el Label, lo malo es que con pack el frame se adapta al contenido
# miLabel.pack()
# Usamos un metodo para introducir el widget sin modificar el tamaño del padre
# place nos permite colocar el widget segun coordenadas 
miLabel.place(x=100, y=50)

# Cargamos la imagen
miImagen = PhotoImage(file="raton.png")
# Colocamos la imagen en un label
Label(miFrame, image=miImagen).place(x=0, y=100)

# Si el label no se usara en un futuro podemos hacer...
# Especifico el color de la letra, su fuente y tamaño
Label(miFrame, text="Hola de nuevo", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=70)



root.mainloop()


