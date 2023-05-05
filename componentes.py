from utiles import *

from testing import *



#Funcion principal, llamada desde el menú principal cuando 
def componentes():
    printMenu("Componentes seleccionado")
    printMenu("Selecciona una opción:")
    printMenu("1. Alta")
    printMenu("2. Modificación")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0: return
    elif opcion == 1:    alta(componentes_list)            
    elif opcion == 2:    menuModificacion(componentes_list)
     
def alta(componentes_list):
    componente = especificarValoresComponente(componentes_list)
    if  componente == -1:
        return
    
    componentes_list.append(componente)
    
    if preguntaYN("¿Desea introducir otro componente? y/n:") == False: #Añadir otro componente
        return 0
    
def menuModificacion(componentes_list):
    printMenu("Selecciona una opción:")
    printMenu("1. Modificar componente a partir del identificador")
    printMenu("2. Listar componentes")
    printMenu("0. Regresar")
    opcion = pedirOpcion(3)
    
    if opcion == 0: return
    if opcion == 1: modificacion(componentes_list)
    if opcion == 2: 
        printLista(componentes_list, "Listado de componentes:")
        modificacion(componentes_list)
    
def modificacion(componentes_list):   
    componenteAux = ()
    identificador = pedirId(False)
    for componente in componentes_list:
        if componente.id == identificador:
            componenteAux = componente
            break
    if componenteAux == ():
        printError("El identificador introducido no existe")
        return
         
    printMenu("Selecciona una opción:")
    printMenu("1. Cambio de stock")
    printMenu("2. Cambio informacion")
    printMenu("3. Dar de baja")
    printMenu("0. Regresar")
    opcion = pedirOpcion(4)
    
    if opcion == 0: return
    if opcion == 1: 
        cambio_stock(componenteAux)
    if opcion == 2: 
        cambio_info(componenteAux)
    if opcion == 3:
        if preguntaYN("¿Está seguro de que desea eliminar el componente? y/n:") == True:
            componentes_list = elimina(componenteAux, componentes_list)
    
def cambio_stock(componenteAux):
    printLog("Cantidad anterior:" + str(componenteAux.cantidad))
    cantidad = introducirValor("entero", "Introduce la cantidad nueva (pulse INTRO para dejar la cantidad anterior):")
    if cantidad != -2:
        componenteAux.cantidad = cantidad
def cambio_info(componenteAux):
    componente = especificarValoresComponente([], componenteAux, False)
    if componente == -1:
        return
    componenteAux = componente
#---------------------------------------------------
#Funciones genéricas
#---------------------------------------------------
def especificarValoresComponente(componentes_list, componente=(), alta=True):
    if alta:
        componenteRes = Componente()
    else:
        componenteRes = componente
    identificador = -1
    if alta:
        print(Fore.CYAN + "Inicio alta")          
        identificador = pedirId(comprobacion=True, debeExistir=False, lista=componentes_list) #Identificador
        if identificador < 0:
            return -1
        else:
            componenteRes.id = identificador
                                
    #Tipo de componente
    if alta == True:
        print(Fore.CYAN + "Introduce tipo de componente")        
        for i, elemento in enumerate(tiposComponentes):
            print(str(i) +". "+ elemento)
        try:
            opcion = input()
            if int(opcion) in list(range(len(tiposComponentes)+1)):
                componenteRes.tipo = tiposComponentes[int(opcion)]
            else:              
                printError("Ingresa un tipo válido1")
                return -1
        except:
            printError("Ingresa un tipo válido2")
            return -1
        
    if alta == False:
        printLog("Peso anterior:" + str(componente.peso))
    numero = introducirValor("entero", "Introduce peso en gramos:") #Numero entero
    if alta == False and numero == -2:
        componenteRes.peso = componente.peso
    elif numero > 0:
        componenteRes.peso = numero
    else:
        printError("Ingresa un número válido")
        return -1
    if alta == False:
        printLog("Coste anterior: " +  str(componente.coste))        
    numero = introducirValor("real", "Introduce coste en euros:") #Numero real
    if alta == False and numero == -2:
        componenteRes.coste = componente.coste
    elif numero > 0:
        componenteRes.coste = numero
    else:
        printError("Ingresa un número válido")
        return -1
    if alta == False:
        printLog("Cantidad de stock anterior: " + str(componente.cantidad))
    numero = introducirValor("entero", "Introduce cantidad:") #Numero entero
    if alta == False and numero == -2:
        componenteRes.cantidad = componente.cantidad
    elif numero > 0:
        componenteRes.cantidad = numero
    else:
        printError("Ingresa un número válido")
        return -1
    return componenteRes

