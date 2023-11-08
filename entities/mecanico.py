from empleado import Empleado
class Mecanico(Empleado):
    def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score):
        super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)
        self._score = score