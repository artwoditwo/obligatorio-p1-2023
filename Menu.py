import re
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
from exceptions.EntidadExiste import EntidadExiste

class Menu():
    def __init__(self):
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
                
                edad_input = input("Ingrese la edad: ")
                if edad_input == "" or not edad_input.isdigit():
                    raise InvalidDatos("ingrese un salario correcto")
                edad = int(edad_input)
                if edad <= 18: 
                    raise ValueError("ingrese una edad mayor a 18")
                    

                fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
                if fecha_nacimiento == "" or not re.match(r'\d{2}/\d{2}/\d{4}', fecha_nacimiento):
                    raise InvalidFechaNacimiento("El formato de la fecha debe ser (DD/MM/AAAA)")
                
                nacionalidad = input("Ingrese nacionalidad: ")
                if nacionalidad == "" or nacionalidad.isdigit():
                    raise InvalidDatos("Tiene que elegir una nacionalidad correcta")
                
                salario_input = input("Ingrese salario: ")
                if salario_input == "" or not salario_input.isdigit():
                    raise InvalidDatos("ingrese un salario correcto")

                salario = int(salario_input)
                if salario <= 0: 
                    raise ValueError("El salario debe ser mayor a 0")    

                print("Ingrese cargo:")
                print("1. Piloto")
                print("2. Piloto de reserva")
                print("3. Mecánico")
                print("4. Jefe de equipo")
                cargo = input("Opción: ")

                if cargo == "1" or cargo == "2":
                    score_input = input("Ingrese score(1-99): ")
                    if score_input == "" or not score_input.isdigit():
                        raise InvalidDatos("Ingrese un digito entre 1 y 99")
                    score=int(score_input)
                    
                    if score > 99 or score < 1:
                        raise InvalidDatos("ingrese un numero dentro del rango")
                        
                    else:
                        numero_auto_input = input("Ingrese el numero de auto: ")
                        if numero_auto_input == "" or not numero_auto_input.isdigit():
                            raise InvalidDatos("lo ingresado no es un numero")
                        numero_auto=int(numero_auto_input)
                        es_reserva = False 

                        if cargo == "2":
                            es_reserva = True 
                        empleado = Piloto(ci, nombre, edad, fecha_nacimiento, nacionalidad, salario, score, numero_auto, es_reserva)
                elif cargo == "3":

                    score_input = input("Ingrese score(1-99): ")
                    if score_input == "" or not score_input.isdigit():
                        raise InvalidDatos("Ingrese un digito entre 1 y 99")
                    score=int(score_input)

                    if score > 99 or score < 1:
                        raise InvalidDatos
                    else:
                        empleado = Mecanico(ci, nombre,edad, fecha_nacimiento, nacionalidad, salario, score)
                    
                elif cargo == "4":
                    empleado = Director_equipo(ci, nombre,edad, fecha_nacimiento, nacionalidad, salario)
                else:
                    print("Opción de cargo no válida.")
                    return
                
                for _ in self._lista_empleados:
                    if _.ci == ci:
                        raise EntidadExiste("La CI igresada ya le pertenece a otro empleado")
                
                self._lista_empleados.append(empleado)
                print("Empleado cargado con éxito")
     
                
            except (InvalidDatos, ValueError, InvalidFechaNacimiento,EntidadExiste) as e:
                        print(f"Error de validación: {e}") 
     
    def alta_auto(self):

        try:
            modelo = input("Ingrese modelo: ")
            if modelo == "":
                 raise InvalidDatos("El campo se encuentra vacío")
            
            ano = input("Ingrese año: ")
            if ano == "" or ano.isalpha() :
                raise InvalidDatos("lo ingresado no es un numero")
            if len(ano) != 4:
                raise InvalidDatos("Ingrese un año correcto")
            

            score_input = input("Ingrese score(1-99): ")
            if score_input == "" or not score_input.isdigit():
                raise InvalidDatos("Ingrese un digito entre 1 y 99")

            score = int(score_input)

            if score > 99 or score < 1:
                raise InvalidDatos("Ingrese un digito entre 1 y 99")
            
            if score > 99 or score < 1:  
                raise InvalidDatos("Ingrese un digito entre 1 y 99")

            
            auto = Auto(modelo, ano, score)
            self._lista_auto.append(auto)
            print("Auto cargado con éxito.")
            
        except InvalidDatos as e:
            print(f"Error de validación: {e}")

        
    
    def alta_equipo(self):
        empleados = []
        try:
            nombre_equipo = input("Ingrese nombre del equipo: ")
            for _ in self._lista_equipos:
                if _.nombre == nombre_equipo:
                    raise EntidadExiste("El nombre ingresado ya le pertenece a un equipo")
            modelo_auto = input("Ingrese modelo de auto: ")
            for _ in self._lista_auto:
                if _.modelo == modelo_auto:
                    break
            else:
                raise EntidadExiste("El modelo ingresado no existe")

            
            
            for a in range(0,2):
                cedula = input("Agregue cedula del empleado titular: ")
                for a in self._lista_empleados:
                    if a.ci == cedula:
                        if isinstance(a,Piloto):
                            if a.reserva == False:
                                empleados.append(cedula)
                                break
                            else:
                                raise EsReserva("El piloto ingresado es un piloto de Reserva")
                        else:
                            raise CargoIncorrecto("El cargo del empleado ingresado no es de Piloto")
                else:
                    raise CInoExiste("La CI ingresada no le pertenece a ningun empleado")
                
                            
            cedula = input("Agregue cedula del empleado reserva: ")
            for a in self._lista_empleados:
                if a.ci == cedula:
                    if isinstance(a,Piloto):
                        if a.reserva == True:
                            empleados.append(cedula)
                            break
                        else:
                                raise EsReserva("El piloto ingresado es un piloto Titular")
                    else:
                            raise CargoIncorrecto("El cargo del empleado ingresado no es de Piloto")
            else:
                raise CInoExiste("La CI ingresada no le pertenece a ningun empleado")
                
            cedula = input("Agregue cedula del jefe de equipo: ")
            for a in self._lista_empleados:
                if a.ci == cedula:
                    if isinstance(a,Director_equipo):
                        empleados.append(cedula)
                        break
                    else:
                            raise CargoIncorrecto("El cargo del empleado ingresado no es de Jefe")
            else:
                    raise CInoExiste("La CI ingresada no le pertenece a ningun empleado")
                
            for a in range(0,8):
                cedula = input("Agregue cedula del mecanico: ")
                for a in self._lista_empleados:
                    if a.ci == cedula:
                        if isinstance(a,Mecanico):
                            empleados.append(cedula)
                            break
                        else:
                            raise CargoIncorrecto("El cargo del empleado ingresado no es de Mecanico")
                else:
                        raise CInoExiste("La CI ingresada no le pertenece a ningun empleado")

        except (ValueError,CInoExiste,CargoIncorrecto,EsReserva,EntidadExiste) as e:
            print(f"Error de validación: {e}")

        equipo = Equipo(nombre_equipo,empleados,modelo_auto)

        self._lista_equipos.append(equipo)

    

######################### NO TOCAR ########################
    def ejecutar_menu(self):
            # Creating 12 employees for testing
        employee1 = Piloto("11111111", "Piloto1", 25, "01/01/1998", "Nacionalidad1", 50000, 90, 1, True)
        employee2 = Piloto("22222222", "Piloto2", 28, "02/02/1995", "Nacionalidad2", 55000, 85, 2, True)
        employee3 = Piloto("33333333", "Piloto3", 22, "03/03/2000", "Nacionalidad3", 60000, 88, 3, False)
        employee4 = Director_equipo("44444444", "Jefe1", 35, "04/04/1987", "Nacionalidad4", 70000)
        employee5 = Mecanico("55555555", "Mecanico1", 30, "05/05/1992", "Nacionalidad5", 40000, 75)
        employee6 = Mecanico("66666666", "Mecanico2", 26, "06/06/1996", "Nacionalidad6", 45000, 78)
        employee7 = Mecanico("77777777", "Mecanico3", 29, "07/07/1993", "Nacionalidad7", 42000, 80)
        employee8 = Mecanico("88888888", "Mecanico4", 32, "08/08/1990", "Nacionalidad8", 48000, 82)
        employee9 = Mecanico("99999999", "Mecanico5", 28, "09/09/1994", "Nacionalidad9", 43000, 79)
        employee10 = Mecanico("10101010", "Mecanico6", 25, "10/10/1997", "Nacionalidad10", 41000, 76)
        employee11 = Mecanico("11111112", "Mecanico7", 27, "11/11/1995", "Nacionalidad11", 44000, 77)
        employee12 = Mecanico("12121212", "Mecanico8", 31, "12/12/1989", "Nacionalidad12", 46000, 81)

        # Adding employees to the menu
        menu = Menu()
        menu._lista_empleados.extend([employee1, employee2, employee3, employee4, employee5, employee6,
                                    employee7, employee8, employee9, employee10, employee11, employee12])
    






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