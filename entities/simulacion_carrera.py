import random
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.auto import Auto


def simulacion_carrera(equipos,lesionados,abandonos,error_pits,penalizados):

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
        
        


    


        
        