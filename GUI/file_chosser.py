from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    # Por default nos abre la carpeta de Documentos, pero se cambia con initialdir
    # Por default nos muestra todas las extenciones peor se cambia con filetypes
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:",\
                filetypes=(("Ficheros de Excel", "*.xlsx"),("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    # filetypes necesita una tupla, se le pasa el nombre y la extencion
    
    # Como podemos ver nos devuelve la ruta del archivo
    print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()