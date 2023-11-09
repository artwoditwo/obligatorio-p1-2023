import random
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.auto import Auto

class Simulacion_Carrera:
    def __init__ (self,equipos,lesionados,abandonos,error_pits,penalizados):

        self._equipos=equipos #recibir lista de todos los equipos desde la variable equipos
        self._pilotos_lesionados=lesionados
        self._pilotos_abandonos=abandonos
        self._pilotos_error_pits=error_pits
        self._pilotos_penalizados=penalizados

        # Getter para equipos
    @property
    def equipos(self):
        return self._equipos

    # Setter para equipos
    @equipos.setter
    def equipos(self, equipo):
        self._equipos = equipo

    # Getter para pilotos_lesionados
    @property
    def pilotos_lesionados(self):
        return self._pilotos_lesionados

    # Setter para pilotos_lesionados
    @pilotos_lesionados.setter
    def pilotos_lesionados(self, piloto_lesionado):
        self._pilotos_lesionados = piloto_lesionado

    # Getter para pilotos_abandonos
    @property
    def pilotos_abandonos(self):
        return self._pilotos_abandonos

    # Setter para pilotos_abandonos
    @pilotos_abandonos.setter
    def pilotos_abandonos(self, piloto_abandono):
        self._pilotos_abandonos = piloto_abandono

    # Getter para pilotos_error_pits
    @property
    def pilotos_error_pits(self):
        return self._pilotos_error_pits

    # Setter para pilotos_error_pits
    @pilotos_error_pits.setter
    def pilotos_error_pits(self, piloto_error_pit):
        self._pilotos_error_pits = piloto_error_pit

    # Getter para pilotos_penalizados
    @property
    def pilotos_penalizados(self):
        return self._pilotos_penalizados

    # Setter para pilotos_penalizados
    @pilotos_penalizados.setter
    def pilotos_penalizados(self, piloto_penalizado):
        self._pilotos_penalizados = piloto_penalizado


    def simular_carrera(self):
        corredores=[]
        corredores_con_puntuacion_final = []
        lista_ganadores=[]
        for a in self._equipos:
            for b in a:
                if isinstance(b,Piloto): #cambiar para piloto titular
                    if b.reserva == False:
                        if b not in self._pilotos_lesionados:
                            corredores.append(b)
                    

        
        
        for i in corredores:
            if i.ci in self._pilotos_abandonos:
                corredores.remove(i)
        
        
        for i in corredores:

            suma_score_mecanicos=0
            score_auto=0
            score_piloto=i.score
            valor_pits=0
            valor_penalizacion=0

            
            
            if i.ci in self._pilotos_error_pits:
                cant_errores_pits = self._pilotos_error_pits.count(i)
                valor_pits= 5*cant_errores_pits
            
            if i.ci in self._pilotos_penalizados:
                cant_penalizaciones = self._pilotos_penalizados.count(i)
                valor_penalizacion = 8*cant_penalizaciones
            
            for a in self._equipos:
                for b in a:
                    if i==b:
                        equipo_del_corredor=a
            
            for c in equipo_del_corredor:
                if isinstance(c,Mecanico):
                    suma_score_mecanicos = suma_score_mecanicos + c.score
            
            for c in equipo_del_corredor:
                if isinstance(c,Auto):
                    score_auto=c.score
            

            
            score_final= suma_score_mecanicos + score_auto + score_piloto - valor_pits - valor_penalizacion

            corredor_con_puntuacion = (score_final, i) 
            corredores_con_puntuacion_final.append(corredor_con_puntuacion) #guarde el score_final con el corredor
            
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
        
        return lista_ganadores
            
            


        

    
        
        