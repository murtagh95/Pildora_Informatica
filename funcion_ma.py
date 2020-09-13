class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self):
        return "{} que trabaja como {}, tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)

def calculo_comision(empleado):
    if empleado.salario <= 3000:
        # Le sumo un 3% el salario
        empleado.salario = empleado.salario * 1.03
    return empleado


listaEmpleados = [
    Empleado("Juan", "Director", 7500),
    Empleado("Ana", "Gerente", 6200),
    Empleado("Antonio", "Administrativo", 5000),
    Empleado("Sara", "Secretaria", 4000),
    Empleado("Mario", "Botones", 2000),
]

# Aplicamos la función a cada elemento de la lista y almacenamos el resultado en una lista nueva
listaEmpleadosNuevos = map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosNuevos:
    print(empleado)



