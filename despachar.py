from utiles import *
from estructuras import *
from testing import *

def despachar():
    printLista(distribuidores_list, "Lista de distribuidores:")
    distAux = ()
    identificadorDist = pedirId(False)
    for dist in distribuidores_list:
        if dist.id == identificadorDist:
            distAux = dist
            break
    if distAux == ():
        printError("El identificador de distribuidor introducido no existe")
        return
    printLista(equipos_disponibles, "Equipos disponibles:")
    equipoAux = ()
    identificadorEquipo = pedirId(False)
    for e in equipos_disponibles:
        if e.id == identificadorEquipo:
            equipoAux = e
            break
    if equipoAux == ():
        printError("El identificador de equipo introducido no existe")
        return
    #Quitar de equipos disponibles
    elimina(equipoAux, equipos_disponibles)
    #Asignacion en despachos:
    despacho = despachos.get(distAux.id)
    if despacho is None:
        despachos[distAux.id] = []        
    despachos[distAux.id].append(Despacho(distAux, equipoAux, distAux.tiempoEntrega))
    printLog("Despacho creado correctamente. Tiempo restante en días: " + str(distAux.tiempoEntrega))
    
def dias():
    dias = introducirValor("entero", "Introduce el número de días que van a transcurrir")
    if dias <= 1:
        printError("Se debe indicar mínimo un día")
        return
    else:
        
        for distId in despachos:
            despachosAEliminar = []
            despachos_list = despachos[distId]
            indiceRemove = 0
            for despacho in despachos_list:
                tiempoRestante = despacho.decTiempo(dias)
                if tiempoRestante <= 0:
                    printLog("El distribuidor " + despacho.distribuidor.nombre + " ha recibido ya su equipo!")                    
                    equipos_despachados.append(despacho.equipo)
                    despachos_list.pop(indiceRemove)
                    if len(despachos_list) == 0:
                        despachosAEliminar.append(distId)
                indiceRemove += 1
        for id in despachosAEliminar:
            del despachos[distId]
