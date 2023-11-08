import random
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.auto import Auto

class Simulacion_Carrera:
    def __init__ (self):

        self._equipos=[] #recibir lista de todos los equipos desde la variable equipos
        self._pilotos_lesionados=[]
        self._pilotos_abandonos=[]
        self._pilotos_error_pits=[]
        self._pilotos_penalizados=[]

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
                    

        
        #random.shuffle(corredores) #randomiaz el orden de los corredores, el orden desde 0-cantidad de corredores es el orden en que finalizaron
        
        for i in corredores:
            if i.nombre in self._pilotos_abandonos:
                corredores.remove(i)
        
        
        for i in corredores:

            suma_score_mecanicos=0
            score_auto=0
            score_piloto=i.score
            valor_pits=0
            valor_penalizacion=0

            
            
            if i.nombre in self._pilotos_error_pits:
                cant_errores_pits = self._pilotos_error_pits.count(i)
                valor_pits= 5*cant_errores_pits
            
            if i.nombre in self._pilotos_penalizados:
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
            corredores_con_puntuacion_final.append(corredor_con_puntuacion)
            
        lista_ganadores=sorted(corredores_con_puntuacion_final, key=lambda x: x[0])

        return lista_ganadores
            
            


        

    
        
        