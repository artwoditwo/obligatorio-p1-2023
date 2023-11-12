class Empleado:
      def __init__(self, ci, nombre, edad, nacionalidad, fecha_nacimiento, salario):
            self._ci = ci 
            self._nombre = nombre 
            self._edad = edad 
            self._nacionalidad = nacionalidad 
            self._fecha_nacimiento = fecha_nacimiento
            self._salario = salario 

      

      @property
      def ci(self):
            return self._ci

      @property
      def nombre(self):
            return self._nombre
      
      @nombre.setter
      def nombre(self, nombre):
            self._nombre = nombre

      @property
      def edad(self):
            return self._edad

      @edad.setter
      def edad(self, edad):
            self._edad = edad

      @property
      def nacionalidad(self):
            return self._nacionalidad

      @nacionalidad.setter
      def nacionalidad(self, nacionalidad):
            self._nacionalidad = nacionalidad

      @property
      def fecha_nacimiento(self):
            return self._fecha_nacimiento

      @fecha_nacimiento.setter
      def fecha_nacimiento(self, fecha_nacimiento):
            self._fecha_nacimiento = fecha_nacimiento

      @property
      def salario(self):
            return self._salario

      @salario.setter
      def salario(self, salario):
            self._salario = salario