class Equipo:
    def __init__(self, nombre,empleados,auto):
        self._nombre = nombre
        self._empleados = empleados
        self._auto = auto
        self._puntuacion = None

    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def empleados(self):
        return self._empleados

    @empleados.setter
    def empleados(self, empleados):
        self._empleados = empleados

    @property
    def auto(self):
        return self._auto

    @auto.setter
    def auto(self, auto):
        self._auto = auto

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, puntuacion):
        self._puntuacion = puntuacion