from empleado import Empleado
class Piloto(Empleado):
      def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, reserva,) -> None:
            super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)
            self._score = score
            self._numero_auto = numero_auto
            self._puntaje_campeonato = puntaje_campeonato
            self._reserva = reserva #True or False
            self._score_carrera = 0

            #nico luego agrega vos el getter y setter para los demas

      @property
      def reserva(self):
                  return self._reserva

      @reserva.setter
      def reserva(self, reserva):
                  self._reserva = reserva

      @property
      def score_carrera(self):
            return self._score_carrera

      @score_carrera.setter
      def score_carrera(self, score_carrera):
            self._score_carrera = score_carrera