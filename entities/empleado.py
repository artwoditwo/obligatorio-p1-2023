class Empleado:
      def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario):
            self._id = id 
            self._nombre = nombre 
            self._edad = edad 
            self._nacionalidad = nacionalidad 
            self._fecha_nacimiento = fecha_nacimiento
            self._salario = salario 

      #nico crea los demas getters

      @property
      def nombre(self):
            return self._nombre

      @nombre.setter
      def nombre(self, nombre):
            self._nombre = nombre