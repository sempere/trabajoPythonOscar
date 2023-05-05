from utiles import *
from estructuras import *
from testing import *


#Funcion principal, llamada desde el menú principal cuando 
def equipos():
    printLista(equipos_disponibles, "Lista de equipos disponibles:")
    
    printMenu("Selecciona una opción:")
    printMenu("1. Alta")
    printMenu("2. Modificación")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0:      return
    elif opcion == 1:    alta(equipos_disponibles)            
    elif opcion == 2:    menuModificacion(equipos_disponibles)
     
def alta(equipos_disponibles):
    equipo = especificarValoresEquipo(equipos_disponibles)
    if  equipo == -1:
        return
    
    equipos_disponibles.append(equipo)
    
    if preguntaYN("¿Desea introducir otro equipo? y/n:") == False: #Añadir otro equipo
        return 0
    
def menuModificacion(equipos_disponibles):
    printMenu("Selecciona una opción:")
    printMenu("1. Modificar equipo a partir del identificador")
    printMenu("2. Listar equipos")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0: return
    if opcion == 1: modificacion(equipos_disponibles)
    if opcion == 2: 
        printLista(equipos_disponibles, "Listado de equipos:")
        modificacion(equipos_disponibles)
    
def modificacion(equipos_disponibles):   
    equipoAux = ()
    identificador = pedirId(False)
    for equipo in equipos_disponibles:
        if equipo.id == identificador:
            equipoAux = equipo
            break
    if equipoAux == ():
        printError("El identificador introducido no existe")
        return
         
    printMenu("Selecciona una opción:")
    printMenu("1. Cambio de configuración")
    printMenu("2. Desensamblar")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0: return
    if opcion == 1: 
        cambio_config(equipoAux)
    if opcion == 2:
        if preguntaYN("¿Está seguro de que desea desensamblar el equipo? y/n:") == True:
            equipos_disponibles = desensamblar(equipoAux, equipos_disponibles)
    

def cambio_config(equipoAux):
    equipo = especificarValoresEquipo([], equipoAux, False)
    if equipo == -1:
        return
    equipoAux = equipo
#---------------------------------------------------
#Funciones genéricas
#---------------------------------------------------
def especificarValoresEquipo(equipos_disponibles, equipo=(), alta=True):
    if alta:
        equipoRes = Equipo()
    else:
        equipoRes = equipo
    identificador = -1
    if alta:
        print("Inicio alta")          
        identificador = pedirId(comprobacion=True, debeExistir=False, lista=equipos_disponibles) #Identificador
        if identificador < 0:
            return -1
        else:
            equipoRes.id = identificador
    
    #Si hay componentes de cada tipo y con stock, pasar a pedir uno por cada tipo al usuario:
    if checkComponentes(componentes_list):
        componentes = {}
        for tipo in tiposComponentes:
            printLista([c for c in componentes_list if c.tipo == tipo], "Componentes del tipo: " + tipo)
            if alta==False:
                printLog("Componente anterior: " + str(equipo.getComponente(tipo)))
            id = pedirId(comprobacion=True, debeExistir=True, lista=componentes_list)
            if id == -2:
                id = equipo.getComponente(tipo).id
            elif id == -1:
                return id
            componentes[tipo] = getElemento(componentes_list, id)
        equipoRes.addComponentes(componentes)
    else:
        printError("No hay componentes de todos los tipos o no hay stock suficiente")
        return
    
    return equipoRes

def desensamblar(equipo, equipos_disponibles):
    equipo.eliminaComponentes()
    elimina(equipo, equipos_disponibles)
    printLista(equipos_disponibles, "Listado de equipos disponibles actualizado")

#Comprobacion de que existe un componente de cada tipo y con STOCK
def checkComponentes(componentes_list):
    tipos = [0,0,0,0,0,0]
    for componente in componentes_list:
        if componente.cantidad > 0:
            tipos[tiposComponentes.index(componente.tipo)] += 1
    hayComponentes = tipos.count(0) == 0
    return hayComponentes
    