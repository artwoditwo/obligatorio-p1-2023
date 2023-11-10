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

class Menu():
    def _init__(self):
        self._lista_empleados=[]
        self._lista_auto=[]
        self._lista_equipos=[]
    
    def alta_empleado(self):
            
            try: 
                ci = int(input("Ingrese cedula: "))
                
                ci_str=str(ci)
                try:
                    if len(ci_str) != 8:
                        raise InvalidDatos
                    else:
                        
                        #Falta hacer la validacion
                    
                        nombre = input("Ingrese nombre: ")
                        if nombre == "":
                            print("el nombre se encuentra vacio")
                            raise InvalidDatos
                        else:
                            fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
                            if fecha_nacimiento == "":
                                raise InvalidDatos
                            nacionalidad = input("Ingrese nacionalidad: ")
                            if nacionalidad == "":
                                raise InvalidDatos
                            salario = float(input("Ingrese salario: "))
                            

                            print("Ingrese cargo:")
                            print("1. Piloto")
                            print("2. Piloto de reserva")
                            print("3. Mecánico")
                            print("4. Jefe de equipo")
                            cargo = int(input("Opción: "))

                            if cargo == 1 or cargo == 2:
                                score = int(input("Ingrese score(1-99): "))
                                
                                if score > 99 or score < 1:
                                    
                                    raise InvalidDatos
                                    
                                else:
                                    numero_auto = int(input("Ingrese número de auto: "))
                                    es_reserva = False 
                                    if cargo == 2:
                                        es_reserva = True 
                                    empleado = Piloto(ci, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, es_reserva)
                            elif cargo == 3:
                                score = int(input("Ingrese score: "))
                                if score > 99 or score < 1:
                                    raise InvalidDatos
                                else:
                                    empleado = Mecanico(ci, nombre, fecha_nacimiento, nacionalidad, salario, score)
                                
                            elif cargo == 4:
                                empleado = Director_equipo(ci, nombre, fecha_nacimiento, nacionalidad, salario)
                            else:
                                print("Opción de cargo no válida.")
                                return
                            
                            self._lista_empleados.append(empleado)
                            print("Empleado cargado con éxito")
                    
                
                except InvalidDatos as e:
                            print("Error de validación:", e)
            except ValueError:
                print("Error de validación")
        
        #             raise DatosYaExistentes
        # except DatosYaExistentes:
        #     print("El dato ingresado")
    def alta_auto(self):
        try:
            modelo = str(input("Ingrese modelo: "))
            ano = int(input("Ingrese año: "))
            score = int(input("Ingrese score: "))

            auto = Auto(modelo, ano, score)
            self._lista_auto.append(auto)
            print("Auto cargado con éxito.")
        except InvalidDatos as e:
            print("Error de validación:", e)
    
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