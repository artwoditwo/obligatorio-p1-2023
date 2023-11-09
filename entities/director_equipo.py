from empleado import Empleado
class Director_equipo(Empleado):
    def __init__(self, ci, nombre, edad, nacionalidad, fecha_nacimiento, salario):
        super().__init__(ci, nombre, edad, nacionalidad, fecha_nacimiento, salario)