from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director_equipo import Director_equipo
from entities.auto import Auto
from entities.equipo import Equipo
from entities.simulacion_carrera import Simulacion_Carrera
from exceptions.InvalidDatos import  InvalidDatos
from exceptions.CInoExiste import CInoExiste 
from exceptions.CargoIncorrecto import CargoIncorrecto 
from exceptions.EsReserva import EsReserva 
from exceptions.ValueError import ValueError
from exceptions.InvalidFechaNacimiento import InvalidFechaNacimiento
import re

class Menu():
    def _init__(self):
        self._lista_empleados=[]
        self._lista_auto=[]
        self._lista_equipos=[]
    
    def alta_empleado(self): 
            try: 
                
                ci = input("Ingrese cedula: ")
                if ci.isalpha() or len(ci) != 8 or ci == "":
                    raise ValueError("La cédula debe contener 8 dígitos")
                
                nombre = input("Ingrese nombre: ")
                if nombre == "":
                    raise InvalidDatos("El nombre se encuentra vacío") #Podría existir nombre con números :)
                
                fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
                if fecha_nacimiento == "" or not re.match(r'\d{2}/\d{2}/\d{4}', fecha_nacimiento):
                    raise InvalidFechaNacimiento("El formato de la fecha debe ser (DD/MM/AAAA)")
                
                nacionalidad = input("Ingrese nacionalidad: ")
                if nacionalidad == "" or nacionalidad.isdigit():
                    raise InvalidDatos("Tiene que elegir una nacionalidad correcta")
                
                salario = input("Ingrese salario: ")
                if salario <= 0 or salario == "": ## CRASHEA ##
                    raise ValueError("El salario debe ser mayor a 0")    

                print("Ingrese cargo:")
                print("1. Piloto")
                print("2. Piloto de reserva")
                print("3. Mecánico")
                print("4. Jefe de equipo")
                cargo = input("Opción: ")
####################################### TENGO QUE VERLO ##############
                if cargo == "1" or cargo == "2":
                    score = int(input("Ingrese score(1-99): "))
                    
                    if score > 99 or score < 1:
                        raise InvalidDatos
                        
                    else:
                        numero_auto = int(input("Ingrese número de auto: "))
                        es_reserva = False 
                        if cargo == "2":
                            es_reserva = True 
                        empleado = Piloto(ci, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, es_reserva)
                elif cargo == "3":
                    score = int(input("Ingrese score: "))
                    if score > 99 or score < 1:
                        raise InvalidDatos
                    else:
                        empleado = Mecanico(ci, nombre, fecha_nacimiento, nacionalidad, salario, score)
                    
                elif cargo == "4":
                    empleado = Director_equipo(ci, nombre, fecha_nacimiento, nacionalidad, salario)
                else:
                    print("Opción de cargo no válida.")
                    return
                
                self._lista_empleados.append(empleado)
                print("Empleado cargado con éxito")
 #########################################################################       
                
            except InvalidDatos or ValueError or InvalidFechaNacimiento as e:
                        print(f"Error de validación: {e}")
     
    def alta_auto(self):
        try:
            modelo = input("Ingrese modelo: ")
            if modelo == "":
                 raise InvalidDatos("El campo se encuentra vacío")
            
            ano = input("Ingrese año: ")
            if ano == "" or ano.isalpha() or len(ano) != 4:
                raise InvalidDatos("Ingrese un año correcto")

            score = input("Ingrese score(1-99): ")
            if score.isalpha() or score == "" or score > 99 or score < 1:  ## CRASHEA ##
                 raise InvalidDatos("Ingrese un digito entre 1 y 99")

            auto = Auto(modelo, ano, score)
            self._lista_auto.append(auto)
            print("Auto cargado con éxito.")
        except InvalidDatos as e:
            print(f"Error de validación: {e}")
    
    def alta_equipo(self):
        empleados = []
        nombre_equipo = input("Ingrese nombre del equipo: ")
        modelo_auto = input("Ingrese modelo de auto: ")
        try:
            try:
                try:
                    try:
                        for a in range(0,2):
                            cedula = input("Agregue cedula del empleado titular: ")
                            for a in self._lista_empleados:
                                if a.ci == cedula:
                                    if isinstance(a,Piloto):
                                        if a.reserva == False:
                                            empleados.append(cedula)
                                        else:
                                            raise EsReserva
                                    else:
                                        raise CargoIncorrecto
                                else:
                                    raise CInoExiste
                                        
                        cedula = input("Agregue cedula del empleado reserva: ")
                        for a in self._lista_empleados:
                            if a.ci == cedula:
                                if isinstance(a,Piloto):
                                    if a.reserva == True:
                                        empleados.append(cedula)
                                    else:
                                            raise EsReserva
                                else:
                                        raise CargoIncorrecto
                            else:
                                    raise CInoExiste
                        cedula = input("Agregue cedula del jefe de equipo: ")
                        for a in self._lista_empleados:
                            if a.ci == cedula:
                                if isinstance(a,Director_equipo):
                                    empleados.append(cedula)
                                else:
                                        raise CargoIncorrecto
                            else:
                                    raise CInoExiste
                            
                        for a in range(0,9):
                            cedula = input("Agregue cedula del mecanico: ")
                            for a in self._lista_empleados:
                                if a.ci == cedula:
                                    if isinstance(a,Mecanico):
                                        empleados.append(cedula)
                                    else:
                                        raise CargoIncorrecto
                                else:
                                        raise CInoExiste
                    except EsReserva:
                        print("El piloto ingresado ....") ### REVISAR ###
                except CargoIncorrecto:
                    print("El cargo de ese empleado no es el pedido")           
            except CInoExiste:
                print("La cedula ingresada no pertenece a ningun empleado existente")
        except ValueError:
            print("Error de validacion")

        equipo = Equipo(nombre_equipo)
    

######################### NO TOCAR ########################
    def ejecutar_menu(self):
        while True:
            print("\nIngrese el número de la operación que desea ejecutar:")
            print("1 - Alta de empleado")
            print("2 - Alta de auto")
            print("3 - Alta de equipo")
            print("4 - Simular carrera")
            print("5 - Realizar consultas")
            print("6 - Finalizar programa")
            opcion = input(">>>")
            if opcion == "1":
                self.alta_empleado()
            elif opcion == "2":
                self.alta_auto()
            elif opcion == "3":
                self.alta_equipo()
            elif opcion == "4":
                self.Simulacion_Carrera()
            elif opcion == "5":
                self.realizar_consultas()
            elif opcion == "6":
                print("Programa finalizado")
                break
            else: 
                print ("Opción inválida")

###########################################################