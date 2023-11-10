from entities.empleado import Empleado
class Mecanico(Empleado):
    def __init__(self, ci, nombre, edad, nacionalidad, fecha_nacimiento, salario, score):
        super().__init__(ci, nombre, edad, nacionalidad, fecha_nacimiento, salario)
        self._score = score
    
    @property
    def score(self):
            return self._score
    
    @score.setter
    def score(self, score):
        self._score = score