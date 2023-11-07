from empleado import Empleado
class Piloto(Empleado):
      def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, lesionado) -> None:
            super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)
            self.score = score
            self.numero_auto = numero_auto
            self.puntaje_campeonato = puntaje_campeonato
            self.lesionado = lesionado