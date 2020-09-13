class Areas:
    """Esta clase calcula las áreas de diferentes figuras geométricas"""

    def areaCuadrado(lado):

        """Calcula el área de un cuadrado
    elevando al cuadrado el lado pasado por parámetro"""

        return "El área del cuadrado es: " + str(lado * lado)

    def areaTriangulo(base, altura):
        """Calcula el área de un trángulo utilizando los parametros base y altura"""
        return "El área del triángulo es: "+ str((base * altura)/ 2)


print(Areas.areaCuadrado(3))
# Imprimimos en pantalla los comentarios de la función
print(Areas.areaCuadrado.__doc__)
help(Areas.areaCuadrado)
print(Areas.areaTriangulo(2, 7))
help(Areas.areaTriangulo)

help(Areas)