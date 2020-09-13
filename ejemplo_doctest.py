def areaTriangulo(base, altura):
    """
    Calcula el área de un triángulo dado

    >>> areaTriangulo(3,6)
    'El área del triángulo es: 9.0'

    """

    return "El área del triángulo es: "+ str((base*altura)/2)

# print(areaTriangulo(2,4))

# Este modulo ejecutara lo que esta en el area de documentación
# se coloca despues de los >>> la funcion a ejecutar y en la linea
# siguiente el resultado que deberia de dar, si el resultado es correcto
# se termina de ejecutar el programa, si el resultado no es el correcto
# presentara un error en pantalla 
import doctest
doctest.testmod()


def compruebaMail(mailUsuario):
    """
    La función evalúa un mail recibido en busca de la @. Si tiene
    una @ es correcto, si tiene más de una @ es incorrecto, la @
    está al final es incorrecto.

    >>> compruebaMail("asdasas@das@@")
    False

    >>> compruebaMail("asdasas@das")
    True

    >>> compruebaMail("asdasas@das@@")
    False

    >>> compruebaMail("asd@asas@das")
    False

    """
    arroba = mailUsuario.count("@")

    if arroba != 1 or mailUsuario.rfind("@") == (len(mailUsuario)-1):
        return False
    else:
        return True
    
# print(compruebaMail("asdasas@das@@"))
doctest.testmod()
