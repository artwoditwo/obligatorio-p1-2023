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
                
                ci = input("Ingrese cédula: ")
                if ci.isalpha() or len(ci) != 8 or ci == "":
                    raise ValueError("La cédula debe contener 8 dígitos")
                
                nombre = input("Ingrese nombre: ")
                if nombre == "":
                    raise InvalidDatos("El nombre se encuentra vacío") #Podría existir nombre con números :)
                
                edad_input = input("Ingrese la edad: ")
                if edad_input == "" or not edad_input.isdigit():
                    raise InvalidDatos("Lo ingresado no es un digito")
                edad = int(edad_input)
                if edad <= 18: 
                    raise ValueError("Ingrese una edad mayor a 18")
                    

                fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
                if fecha_nacimiento == "" or not re.match(r'\d{2}/\d{2}/\d{4}', fecha_nacimiento):
                    raise InvalidFechaNacimiento("El formato de la fecha debe ser (DD/MM/AAAA)")
                
                nacionalidad = input("Ingrese nacionalidad: ")
                if nacionalidad == "" or nacionalidad.isdigit():
                    raise InvalidDatos("Tiene que elegir una nacionalidad correcta")
                
                salario_input = input("Ingrese salario: ")
                if salario_input == "" or not salario_input.isdigit():
                    raise InvalidDatos("Ingrese un salario correcto")
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
                        raise InvalidDatos("Ingrese un numero dentro del rango")
                        
                    else:
                        numero_auto_input = input("Ingrese el numero de auto: ")
                        if numero_auto_input == "" or not numero_auto_input.isdigit():
                            raise InvalidDatos("Lo ingresado no es un numero")
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
                        raise InvalidDatos("Ingrese un numero dentro del rango")
                    else:
                        empleado = Mecanico(ci, nombre,edad, fecha_nacimiento, nacionalidad, salario, score)
                    
                elif cargo == "4":
                    empleado = Director_equipo(ci, nombre,edad, fecha_nacimiento, nacionalidad, salario)
                else:
                    print("Opción de cargo no válida.")
                    return
                
                for _ in self._lista_empleados:
                    if _.ci == ci:
                        raise EntidadExiste("La CI ingresada ya le pertenece a otro empleado")
                
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
            if ano == "" or ano.isalpha():
                raise InvalidDatos("Lo ingresado no es un numero")
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
            if nombre_equipo == "":
                raise ValueError("Ingrese un nombre")
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
                cedula = input("Agregue cédula del piloto titular: ")
                for empleado in self._lista_empleados:
                    if empleado.ci == cedula:
                        if isinstance(empleado,Piloto):
                            if empleado.reserva == False:
                                if cedula in empleados:
                                    raise EntidadExiste("ERROR: Esa Persona ya ha sido ingresada en el equipo")
                                else:
                                    empleados.append(empleado) #solia ser cedula, pero ahora append a la persona con esa cedula
                                break
                            else:
                                raise EsReserva("El piloto ingresado es un piloto de reserva")
                        else:
                            raise CargoIncorrecto("El cargo del empleado ingresado no es de piloto")
                else:
                    raise CInoExiste("La CI ingresada no le pertenece a ningún empleado")
                
                            
            cedula = input("Agregue cédula del empleado reserva: ")
            for empleado in self._lista_empleados:
                if empleado.ci == cedula:
                    if isinstance(empleado,Piloto):
                        if empleado.reserva == True:
                            if cedula in empleados:
                                raise EntidadExiste("ERROR: Esa Persona ya ha sido ingresada en el equipo")
                            else:
                                empleados.append(empleado)
                            break
                        else:
                                raise EsReserva("El piloto ingresado es un piloto titular")
                    else:
                            raise CargoIncorrecto("El cargo del empleado ingresado no es de piloto")
            else:
                raise CInoExiste("La CI ingresada no le pertenece a ningún empleado")
                
            cedula = input("Agregue cédula del jefe de equipo: ")
            for empleado in self._lista_empleados:
                if empleado.ci == cedula:
                    if isinstance(empleado,Director_equipo):
                        if cedula in empleados:
                            raise EntidadExiste("ERROR: Esa Persona ya ha sido ingresada en el equipo")
                        else:
                            empleados.append(empleado)
                        break
                    else:
                            raise CargoIncorrecto("El cargo del empleado ingresado no es de jefe")
            else:
                    raise CInoExiste("La CI ingresada no le pertenece a ningún empleado")
                
            for a in range(0,8):
                cedula = input("Agregue cédula del mecanico: ")
                for empleado in self._lista_empleados:
                    if empleado.ci == cedula:
                        if isinstance(empleado,Mecanico):
                            if cedula in empleados:
                                raise EntidadExiste("ERROR: Esa Persona ya ah sido ingresada en el equipo")
                            else:
                                empleados.append(empleado)
                            break
                        else:
                            raise CargoIncorrecto("El cargo del empleado ingresado no es de mecánico")
                else:
                        raise CInoExiste("La CI ingresada no le pertenece a ningún empleado")

        except (CInoExiste,CargoIncorrecto,EsReserva,EntidadExiste) as e:
            print(f"Error de validación: {e}")

        equipo = Equipo(nombre_equipo,empleados,modelo_auto)

        self._lista_equipos.append(equipo)
        print("Equipo ingresado con excito!")

    def Simulacion_Carrera(self):
        nro_auto_pilotos_lesionados=[] #recibir lista de todos los equipos desde la variable equipos
        nro_auto_pilotos_abandonaron=[]
        nro_auto_pilotos_error_pits=[]
        nro_auto_pilotos_penalidad=[]




        corredores=[]
        corredores_con_puntuacion_final = []
        lista_ganadores=[]
        for a in self._lista_equipos:
            for b in a:     # a seria el equipo y b seria cada empleado dentro de ese equipo
                if isinstance(b,Piloto): #cambiar para piloto titular
                    if b.reserva == False:
                        if b in nro_auto_pilotos_lesionados:
                            for c in a: #c cumple la misma funcion que b
                                if c.reserva==True:
                                    if c in corredores:
                                        pass
                                    else:
                                        corredores.append(c)

                        else:
                            corredores.append(b)
                    

        
        
        for i in corredores:
            if i.numero_auto in nro_auto_pilotos_abandonaron:
                corredores.remove(i)
        
        
        for i in corredores:

            suma_score_mecanicos=0
            score_auto=0
            score_piloto=i.score
            valor_pits=0
            valor_penalizacion=0

            
            
            if i.numero_auto in nro_auto_pilotos_error_pits:
                cant_errores_pits = nro_auto_pilotos_error_pits(i)
                valor_pits= 5*cant_errores_pits
            
            if i.numero_auto in nro_auto_pilotos_penalidad:
                cant_penalizaciones = nro_auto_pilotos_penalidad(i)
                valor_penalizacion = 8*cant_penalizaciones
            
            for a in self._lista_equipos:
                for b in a:
                    if i==b:
                        equipo_del_corredor=a
            
            for c in equipo_del_corredor:
                if isinstance(c,Mecanico):
                    suma_score_mecanicos = suma_score_mecanicos + c.score
            
            for o in self._lista_auto:
                if o.modelo == equipo_del_corredor.auto:
                    score_auto=o.score
            

            
            score_final= suma_score_mecanicos + score_auto + score_piloto - valor_pits - valor_penalizacion

            corredor_con_puntuacion = (score_final, i) 
            corredores_con_puntuacion_final.append(corredor_con_puntuacion) #guarde el score_final con el corredor en una tupla
            
        lista_ganadores=sorted(corredores_con_puntuacion_final, key=lambda x: x[0]) #lleno la lista con la forma ordenada de las tuplas a partir del score_final
        
        for i in lista_ganadores:
            if i == lista_ganadores[0]:
                puntuacion_posicion=25
            elif i == lista_ganadores[1]:
                puntuacion_posicion=18
            elif i == lista_ganadores[2]:
                puntuacion_posicion=15
            elif i == lista_ganadores[3]:
                puntuacion_posicion=12
            elif i == lista_ganadores[4]:
                puntuacion_posicion=10
            elif i == lista_ganadores[5]:
                puntuacion_posicion=8
            elif i == lista_ganadores[6]:
                puntuacion_posicion=6
            elif i == lista_ganadores[7]:
                puntuacion_posicion=4
            elif i == lista_ganadores[8]:
                puntuacion_posicion=2
            elif i == lista_ganadores[9]:
                puntuacion_posicion=1
            else:
                puntuacion_posicion=0

            puntaje=i.puntuacion +puntuacion_posicion
            i.puntuacion=puntaje
        
        print(lista_ganadores) 
        
        


    


        
        

        


######################### NO TOCAR ########################
    def ejecutar_menu(self):
            # Creating 12 employees for testing
        employee1 = Piloto("11111111", "Piloto1", 25, "01/01/1998", "Nacionalidad1", 50000, 90, 1, False)
        employee2 = Piloto("22222222", "Piloto2", 28, "02/02/1995", "Nacionalidad2", 55000, 85, 2, False)
        employee3 = Piloto("33333333", "Piloto3", 22, "03/03/2000", "Nacionalidad3", 60000, 88, 3, True)
        employee4 = Director_equipo("44444444", "Jefe1", 35, "04/04/1987", "Nacionalidad4", 70000)
        employee5 = Mecanico("55555555", "Mecánico1", 30, "05/05/1992", "Nacionalidad5", 40000, 75)
        employee6 = Mecanico("66666666", "Mecánico2", 26, "06/06/1996", "Nacionalidad6", 45000, 78)
        employee7 = Mecanico("77777777", "Mecánico3", 29, "07/07/1993", "Nacionalidad7", 42000, 80)
        employee8 = Mecanico("88888888", "Mecánico4", 32, "08/08/1990", "Nacionalidad8", 48000, 82)
        employee9 = Mecanico("99999999", "Mecánico5", 28, "09/09/1994", "Nacionalidad9", 43000, 79)
        employee10 = Mecanico("10101010", "Mecánico6", 25, "10/10/1997", "Nacionalidad10", 41000, 76)
        employee11 = Mecanico("11111112", "Mecánico7", 27, "11/11/1995", "Nacionalidad11", 44000, 77)
        employee12 = Mecanico("12121212", "Mecánico8", 31, "12/12/1989", "Nacionalidad12", 46000, 81)

        # Adding employees to the menu
        
        self._lista_empleados.extend([employee1, employee2, employee3, employee4, employee5, employee6,
                                    employee7, employee8, employee9, employee10, employee11, employee12])
        #auto for test
        auto = Auto("fiat",1234,55)
        self._lista_auto.append(auto)
        # equipo for test
        lista_empleados=[employee1,employee2,employee3,employee4,employee5,employee6,employee7,
                         employee8,employee9,employee10,employee11,employee12]
        
        equipo=Equipo("Arturo",lista_empleados,"fiat")
        self._lista_equipos.append(equipo)





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