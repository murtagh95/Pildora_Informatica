from tkinter import *
# Libreria para la utilización de ventanas emergentes
from tkinter import messagebox

root = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Nico","Procesador de texto 2020")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
    # Este método devuelve un valor dependiendo de que eliga el usurio
    # valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    # Cambiamos la ventana
    valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")

    # askquestion devuelve yes o no
    # if valor == "yes":
        # Cerramos la aplicación
        # root.destroy()
    
    # askokcacel devuelve un boolean
    if valor == True:
        # Cerramos la aplicación
        root.destroy()
    
def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posiblo cerrar. Documento bloqueado")

    if not(valor):
        root.destroy()
    else:
        cerrarDocumento()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
# Le agregamos elementos a las opciones del menu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Cargar")
archivoMenu.add_command(label="Guarda")
archivoMenu.add_command(label="Guarda Como")
# Creamos una barra separadora
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barraMenu)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de..", command=infoAdicional)

# Introdusco las obciones en la ventana
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)




root.mainloop()