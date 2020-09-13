# Llamamos la libreria que nos permite trabajar con GUI
from tkinter import *

# Contruimos la raiz, es la ventana principal
raiz = Tk()

# Le damos un tituloa la ventala
raiz.title("Ventana de prueba")
# Cambiamos el icono
# raiz.iconbitmap("goku.ico")

# Impedimos que el usuario cambie el tamaño de la ventana
# 1º pertenece al width: ancho
# 2º pertenece al height: alto
# raiz.resizable(False, False)

# Cambiamos el tamaño de la ventana
# Pasamos el ancho x largo
# raiz.geometry("650x350")

# Este método sirve para varias cosas, en este caso cambiamos el color de fondo
raiz.config(bg="pink")

# Creamos el Frame
miFrame = Frame()
# Agregamos el frame a la raiz
# Lo anclamos a la derecha
# miFrame.pack(side="right")
# Lo anclamos a bajo
# miFrame.pack(side="bottom")
# Lo anclamos a arriba y a la izquierda
# miFrame.pack(side="left", anchor="n")
#  A medida que la raiz crece tambien el frame en el eje x
# miFrame.pack(fill="x")
#  A medida que la raiz crece tambien el frame en el eje y
miFrame.pack(fill="y", expand="True")
#  A medida que la raiz crece tambien el frame 
# miFrame.pack(fill="both", expand="True")


# Le damos un color de fondo al frame
miFrame.config(bg="red")

# Le damos un tamaño al frame, este tendra un tamaño fijo por default
miFrame.config(width="650", height="300")

# Le cambiamos el borde al frame
# Primero cambiamos el grosor del borde
miFrame.config(bd="15")
# miFrame.config(relief="groove")
miFrame.config(relief="sunken")

# Cambiamos el cursor
# miFrame.config(cursor="hand2")
miFrame.config(cursor="pirate")


# Creamos un bucle infinito para que la ventana este activa siempre
raiz.mainloop()




