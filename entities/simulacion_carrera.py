
class Simulacion_Carrera:
    def __init__ (self):

        self._carrera=[] #recibir lista
        self._pilotos_lesionados=[]
        self._pilotos_abandonos=[]
        self._pilotos_error_pits=[]
        self._pilotos_penalizados=[]


    def piloto_lesionado(self,piloto):
        self._pilotos_lesionados.append(piloto)
    
    def piloto_abandona(self,piloto):
        self._pilotos_abandonos.append(piloto)

    def piloto_error_pit(self,piloto):
        self._pilotos_error_pits.append(piloto)

    def piloto_penalizado(self,piloto):
        self._pilotos_penalizados.append(piloto)

    
        
        