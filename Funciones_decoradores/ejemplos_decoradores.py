def funcion_decoradora(funcion_parametro):
    # Con *args le decimos la función recibira un nº indeterminado de parametros
    def funcion_interior(*args, **kwargs):
        # Acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")

        # Visualizamos lo que muestra la función pasada como parametro
        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")

    return funcion_interior



@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

# Le avisamos al programa que la función que sigue sera decorada
@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7, 5, 8)
resta(12, 10)

potencia(base=5, exponente=3)

