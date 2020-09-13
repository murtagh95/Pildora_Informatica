# def numero_par(num):
#     if num % 2 == 0:
#         return True

numeros = [17, 24, 8, 52, 18, 44, 67]

print(list(filter(lambda num: num%2==0, numeros)))

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self):
        return "{} que trabaja como {}, tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "Gerente", 72000),
    Empleado("Antonio", "Administrativo", 70000),
    Empleado("Sara", "Secretaria", 40000),
    Empleado("Mario", "Botones", 20000),
]

# Recorro el objeto buscando los salarios más altos, filter devolvera solo los elementos
# que cumplan o sean verdaderos de laexpreción lambda
salarios_altos = filter(lambda empleado: empleado.salario >50000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)