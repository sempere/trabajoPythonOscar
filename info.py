from utiles import *
from estructuras import *
from testing import *

def info_sistema():
    printLista(componentes_list, "Listado de componentes:")
    printLista(equipos_disponibles, "Listado de equipos disponibles en stock:")
    
    for distId in despachos:
        distribuidor = getElemento(distribuidores_list, distId)
        printLista(despachos[distId], "Listado de equipos despachando por el distribuidor " + distribuidor.nombre)
    printLista(equipos_despachados, "Listado de equipos despachados:")
    
    printLista(distribuidores_list, "Listado de distribuidores:")
    
def ficheros():
    printMenu("Selecciona una opción:")
    printMenu("1. Cargar datos")
    printMenu("2. Guardar datos")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0: return
    elif opcion == 1:    cargar()            
    elif opcion == 2:    guardar()


def cargar():
    inicializa()
    fichero = introducirValor("", "Introduce nombre del fichero:")
    if fichero == -2:
        printError("Nombre incorrecto, debe contener algún valor")
        return 
    try:
        with open(fichero, mode='r', encoding='utf-8') as f:
            lineas = f.readlines()
            modos = ['componentes', 'equipos_disponibles', 'equipos_despachados', 'distribuidores', 'despachos']
            indiceModo = 0
            for linea in lineas:
                if linea==separador():
                    indiceModo += 1
                else:
                    elementos = linea.split(";")
                    if modos[indiceModo] == 'componentes':               
                        componentes_list.append(leerComponente(elementos))
                    elif modos[indiceModo] == 'equipos_disponibles':
                        equipos_disponibles.append(leerEquipo(elementos))
                    elif modos[indiceModo] == 'equipos_despachados':
                        equipos_despachados.append(leerEquipo(elementos))
                    elif modos[indiceModo] == 'distribuidores':
                        distribuidores_list.append(leerDistribuidor(elementos))
                    elif modos[indiceModo] == 'despachos':
                        despachoNuevo = leerDespacho(elementos)
                        despacho = despachos.get(despachoNuevo.distribuidor.id)
                        if despacho is None:
                            despachos[despachoNuevo.distribuidor.id] = []
                        despachos[despachoNuevo.distribuidor.id].append(despachoNuevo)
        printLog("Carga correcta de los datos del fichero: " + fichero)
    except:
        printError("Error en la apertura del fichero con nombre: " + fichero)
def guardar():
    fichero = introducirValor("", "Introduce nombre del fichero:")
    if fichero == "":
        printError("Nombre incorrecto, debe contener algún valor")
        return
    linea = ""
    with open(fichero, mode='w', encoding='utf-8') as f:
        #Listado de componentes
        for componente in componentes_list:
            linea = datosComponente(componente)
            f.write(linea)
        f.write(separador())
        #Listado de equipos disponibles
        for equipo in equipos_disponibles:
            linea = datosEquipo(equipo) + '\n'
            f.write(linea)
        f.write(separador())
        #Listado de equipos despachados
        for equipo in equipos_despachados:
            linea = datosEquipo(equipo) + '\n'
            f.write(linea)
        f.write(separador())
        #Listado de distribuidores
        for dist in distribuidores_list:
            linea = datosDistribuidor(dist)
            f.write(linea)
        f.write(separador())
        #Despachos
        for distId in despachos:
            despachos_list = despachos[distId]
            for despacho in despachos_list:
                linea = datosDespacho(despacho)
                f.write(linea)
        f.write(separador())
        

'''
FUNCIONES AUXILIARES
'''
def datosComponente(componente):
    return componente.id + ";" + componente.tipo + ";" + str(componente.peso) + ";" + str(componente.coste) + ";" + str(componente.cantidad) + '\n'
def leerComponente(elementos):
    return Componente(elementos[0], elementos[1], int(elementos[2]), float(elementos[3]), int(elementos[4]))
def datosEquipo(equipo):
    cadena = str(equipo.id)
    for tipoComp in equipo.componentes:
        cadena += ";" + tipoComp + "-" + equipo.componentes.get(tipoComp).id
    return cadena
def leerEquipo(elementos):
    equipo = Equipo(elementos[0])
    for i in range(1,7):
        tuplaComponente = elementos[i].split("-")
        componente = getElemento(componentes_list, tuplaComponente[1].rstrip())
        equipo.addComponente(tuplaComponente[0], componente)
    return equipo
def datosDistribuidor(dist):
    return str(dist.id) + ";" + dist.nombre + ";" + str(dist.tiempoEntrega) + ";" + dist.direccion + "\n"
def leerDistribuidor(elementos):
    return Distribuidor(elementos[0], elementos[1], int(elementos[2]), elementos[3])
def datosDespacho(despacho):
    cadena = str(despacho.distribuidor.id) + ";"
    cadena += datosEquipo(despacho.equipo) + ";"
    cadena += str(despacho.tiempoRestante) + "\n"
    return cadena
def leerDespacho(elementos):
    despacho = Despacho()
    despacho.distribuidor = getElemento(distribuidores_list, elementos[0])
    equipo = Equipo(elementos[1])
    for i in range(2,8):
        tuplaComponente = elementos[i].split("-")
        componente = getElemento(componentes_list, tuplaComponente[1].rstrip())
        equipo.addComponente(tuplaComponente[0], componente)
    despacho.equipo = equipo
    despacho.tiempoRestante = int(elementos[8])
    return despacho
def separador():
    return "---\n"