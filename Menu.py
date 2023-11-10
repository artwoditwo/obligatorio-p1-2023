from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director_equipo import Director_equipo
from entities.auto import Auto
from entities.equipo import Equipo
from entities.simulacion_carrera import Simulacion_Carrera
from exceptions.InvalidDatos import  InvalidDatos

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
                if len(ci_str) == 8:
                    #Falta hacer la validacion
                    try:
                        nombre = input("Ingrese nombre: ")
                        if nombre == "":
                            print("el nombre se encuentra vacio")
                            raise InvalidDatos
                        else:
                            fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
                            nacionalidad = input("Ingrese nacionalidad: ")
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
                                    es_reserva = False if cargo == "1" else True
                                    empleado = Piloto(ci, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, es_reserva)
                            elif cargo == 3:
                                score = int(input("Ingrese score: "))
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
                else:
                    raise InvalidDatos
            except InvalidDatos:
                print("La longitud de la cedula es incorrecta")
        except ValueError:
            print("Error de validación")
        
        
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
        nombre_equipo = input("Ingrese nombre del equipo: ")
        modelo_auto = input("Ingrese modelo de auto: ")
        
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