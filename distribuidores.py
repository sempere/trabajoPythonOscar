from utiles import *
from estructuras import *
from testing import *


#Funcion principal, llamada desde el menú principal cuando 
def distribuidores():
    printLista(distribuidores_list, "Lista de distribuidores:")
    
    printMenu("Selecciona una opción:")
    printMenu("1. Alta")
    printMenu("2. Modificación")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0:      return
    elif opcion == 1:    alta(distribuidores_list)            
    elif opcion == 2:    menuModificacion(distribuidores_list)
     
def alta(distribuidores_list):
    while True:
        dist = especificarValores(distribuidores_list)
        if  dist == -1:
            return   
        distribuidores_list.append(dist)    
        if preguntaYN("¿Desea introducir otro distribuidor? y/n:") == False: #Añadir otro distribuidor
            return 0
    
def menuModificacion(distribuidores_list):
    printMenu("Selecciona una opción:")
    printMenu("1. Modificar distribuidor a partir del identificador")
    printMenu("2. Listar distribuidores")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0: return
    if opcion == 1: modificacion(distribuidores_list)
    if opcion == 2: 
        printLista(distribuidores_list, "Listado de distribuidores:")
        modificacion(distribuidores_list)
    
def modificacion(distribuidores_list):   
    distAux = ()
    identificador = pedirId(False)
    for dist in distribuidores_list:
        if dist.id == identificador:
            distAux = dist
            break
    if distAux == ():
        printError("El identificador introducido no existe")
        return
         
    printMenu("Selecciona una opción:")
    printMenu("1. Cambio de información")
    printMenu("2. Dar de baja")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0: return
    if opcion == 1: 
        cambio_info(distAux)
    if opcion == 2:
        if preguntaYN("¿Está seguro de que desea dar de baja al distribuidor? y/n:") == True:
            distribuidores_list = darDeBaja(distAux, distribuidores_list)
    

def cambio_info(distAux):
    dist = especificarValores([d for d in distribuidores_list if d.nombre != distAux.nombre], distAux, False)
    if dist == -1:
        return
    distAux = dist
#---------------------------------------------------
#Funciones genéricas
#---------------------------------------------------
def especificarValores(distribuidores_list, dist=(), alta=True):
    if alta:
        distRes = Distribuidor()
    else:
        distRes = dist
    identificador = -1
    if alta:
        print("Inicio alta")          
        identificador = pedirId(comprobacion=True, debeExistir=False, lista=distribuidores_list) #Identificador
        if identificador < 0:
            return -1
        else:
            distRes.id = identificador
    #Nombre del distribuidor
    if alta == False:
        printLog("Nombre anterior:" + distRes.nombre)
    nombre = introducirValor("", "Introduce nombre del distribuidor (debe ser único):")
    if alta == False and nombre == '':
        nombre = distRes.nombre
    elif nombre == "" or len([d for d in distribuidores_list if d.nombre == nombre]) != 0:
        printError("Nombre incorrecto, debe contener algún valor y ser único")
        return -1
    else:
        distRes.nombre = nombre
    #Tiempo de entrega
    if alta == False:
        printLog("Tiempo de entrega anterior:" + str(distRes.tiempoEntrega))
    tiempo = introducirValor("entero", "Introduce tiempo de entrega en días (entero > 0):") #Numero entero
    if alta == False and tiempo == -2:
        tiempo = distRes.tiempo    
    elif tiempo > 0:
        distRes.tiempoEntrega = tiempo
    else:
        printError("Ingresa un tiempo de entrega válido")
        return -1
    #Direccion
    if alta == False:
        printLog("Direccion anterior:" + distRes.direccion)
    direccion = introducirValor("cadena", "Introduce dirección, máximo 100 caracteres:") #Numero entero
    if alta == False and direccion == '':
        direccion = distRes.direccion
    elif direccion != "" and len(direccion) <= 100:
        distRes.direccion = direccion
    else:
        printError("Ingresa una dirección válida")
        return -1
    
    return distRes

def darDeBaja(dist, distribuidores_list):
    #Si tiene equipos en despacho, devolverlos al listado de equipos disponibles:
    despacho = despachos.get(dist.id)
    if despacho is not None:
        for equipo in despacho.equipos:
            equipos_disponibles.append(equipo)
        del despachos[dist.id]
    printLista(equipos_disponibles, "Listado de equipos disponibles actualizado")
    #Eliminar distribuidor
    elimina(dist, distribuidores_list)


    