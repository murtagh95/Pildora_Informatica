import tkinter

def funcion1(otra_ventana):
    root.deiconify()
    otra_ventana.destroy()

def funcion():
    otra_ventana = tkinter.Toplevel(root)
    root.withdraw()
    tkinter.Label(otra_ventana, text="Ventana Secundaria").pack()

    boton = tkinter.Button(otra_ventana, text="Volver atras", command=lambda:funcion1(otra_ventana))
    boton.pack()



root = tkinter.Tk()
tkinter.Label(root, text="Ventana Principal").pack()
boton = tkinter.Button(root, text="Abrir otra ventana", command=funcion)
boton.pack()

root.mainloop()