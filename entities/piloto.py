from entities.empleado import Empleado
class Piloto(Empleado):
      def __init__(self, ci, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, reserva) -> None:
            super().__init__(ci, nombre, edad, nacionalidad, fecha_nacimiento, salario)
            self._score = score
            self._numero_auto = numero_auto
            self._reserva = reserva #True or False
            self._puntaje_campeonato = 0
            self._puntuacion=None

            


      @property
      def score(self):
            return self._score
      
      @property
      def numero_auto(self):
            return self._numero_auto
      
      @numero_auto.setter
      def numero_auto(self,numero_auto):
            self._numero_auto=numero_auto

      @property
      def reserva(self):
            return self._reserva

      @reserva.setter
      def reserva(self, reserva):
            self._reserva = reserva

      @property
      def puntaje_campeonato(self):
            return self._puntaje_campeonato

      @puntaje_campeonato.setter
      def puntaje_campeonato(self, puntaje_campeonato):
            self._puntaje_campeonato = puntaje_campeonato

      @property
      def puntuacion(self):
            return self._puntuacion

      @puntuacion.setter
      def puntuacion(self, puntuacion):
            self._puntuacion = puntuacion