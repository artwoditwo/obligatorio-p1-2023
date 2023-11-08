import random
from entities.piloto import Piloto
class Simulacion_Carrera:
    def __init__ (self,):

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
        corredores_primeras_diez_posiciones=[]
        for a in self._equipos:
            for b in a:
                if isinstance(b,Piloto): #cambiar para piloto titular
                    if b.reserva == False:
                        if b not in self._pilotos_lesionados:
                            corredores.append(b)
                    

        
        random.shuffle(corredores) #randomiaz el orden de los corredores, el orden desde 0-cantidad de corredores es el orden en que finalizaron
        

        
        for i in corredores[:10]:
            corredores_primeras_diez_posiciones.append(i)
        

    
        
        