# def area_triangulo(base, altura):
#     return (base * altura) / 2

area_triangulo = lambda base, altura: (base*altura)/2

print(area_triangulo(5, 7))
triangulo1 = area_triangulo(5, 8)
triangulo2 = area_triangulo(5, 10)

print(triangulo1)
print(triangulo2)

al_cubo = lambda numero: numero**3
al_cubo_pow = lambda numero: pow(numero, 3)

print(al_cubo(13))
print(al_cubo_pow(13))

destacar_valor = lambda comision: "¡{}!$".format(comision)  

comisionAna= 15558
print(destacar_valor(comisionAna))
