from empleado import Empleado
class Piloto(Empleado):
      def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, reserva) -> None:
            super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)
            self._score = score
            self._numero_auto = numero_auto
            self._puntaje_campeonato = puntaje_campeonato
            self._reserva = reserva #True or False
            self._score_total_campeonato = 0
            self._puntuacion=None

            #nico luego agrega vos el getter y setter para los demas


      @property
      def score(self):
            return self._score

      @property
      def reserva(self):
            return self._reserva

      @reserva.setter
      def reserva(self, reserva):
            self._reserva = reserva

      @property
      def score_total_campeonato(self):
            return self._score_total_campeonato

      @score_total_campeonato.setter
      def score_total_campeonato(self, score_total_campeonato):
            self._score_total_campeonato = score_total_campeonato

      @property
      def puntuacion(self):
            return self._puntuacion

      @puntuacion.setter
      def puntuacion(self, puntuacion):
            self._puntuacion = puntuacion