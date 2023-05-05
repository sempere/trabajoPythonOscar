# Modulos.....
import sys
import colorama
from collections import namedtuple
from colorama import Fore
colorama.init()


def introducirValor(tipo, mensaje): #Numero
    print(Fore.CYAN + mensaje)
    numero = input()
    try:
        numero = str(numero)
        if numero == "":
            return -2
    except:
        pass
    if tipo == "real":
        try:
            numero = float(numero)
        except:
            numero = -1
    if tipo == "entero":
        try:
            numero = int(numero)
        except:
            numero = -1 
    return numero           
def pedirOpcion(numOpciones, opcion=-1, msgError="Ingresa una opción válida"):
    if opcion == -1:
        opcion = -1
        try:
            opcion = int(input())
        except:
            opcion = -1
        if opcion in list(range(numOpciones)):
            return opcion
        else:
            printError(msgError)  
    return opcion  
          
def printError(msg):
    printMsg(msg + "\n", 'red')
def printLog(msg):
    printMsg(msg + "\n", 'white')
def printMenu(msg):
    printMsg(msg, 'blue')

def printMsg(msg, color):
    if color == 'red': print(Fore.RED + msg)
    elif color == 'cyan': print(Fore.CYAN + msg)
    elif color == 'green': print(Fore.GREEN + msg)
    elif color == 'yellow': print(Fore.YELLOW + msg)
    elif color == 'magenta': print(Fore.MAGENTA + msg)
    elif color == 'blue': print(Fore.BLUE + msg)
    elif color == 'white': print(Fore.WHITE + msg)
    else : print(Fore.WHITE + msg)

def printLista(lista, msg=""):
    #print("[" + ",".join(map(str, lista)) + "]")
    if msg != "": print(Fore.WHITE + msg)
    if len(lista) == 0:
        print(Fore.GREEN + "No hay elementos")
    else:
        print(Fore.GREEN)
        print(*lista, sep='\n')
    print("")
  
#Funcion que pide un id al usuario por teclado, y sirve tanto para modificar componentes/equipos/dist
#como para dar de alta un elemento  
def pedirId(comprobacion=True, debeExistir=True, lista=[]): #Identificador
    print(Fore.CYAN + "Introduce identificador, (alfanumérico, mínimo 3 caracteres):")
    try:
        identificador = str(input())
        if identificador == '':
            return -2
    except:
        identificador = -1       
    if comprobacion:
        if len(identificador) <= 0:
            printError("El identificador debe tener mínimo 3 caracteres.")
            return -1
        elif existe_id(lista, identificador) != debeExistir:
            if debeExistir: printError("El identificador no existe.")
            else: printError("El identificador no es único, ya existe otro.")
            return -1
        else:
            return identificador
    else:
        return identificador
        
#Funcion que comprueba si el id existe ya en la lista de componentes
def existe_id(lista, id):
    return len([e for e in lista if e.id == id]) != 0
#Funcion que devuelve un elemento en base a su id
def getElemento(lista, id):
    aux = -1
    for elemento in lista:
        if elemento.id == id:
            return elemento
    return aux 
#Funcion que elimina un elemento en base a su ID
def elimina(elemento, lista):
    c = 0
    for e in lista:
        if e.id == elemento.id:
            del lista[c]
        c = c + 1


def preguntaYN(msg=""): #Añadir otro elemento
    if msg != "": print(msg)
    try:
        opcion = str(input())
    except:
        opcion = "z"
        return False
    if opcion == "n":
        return False
    if opcion == "y":
        return True
    else:              
        printError("Valor invalido, volviendo a menu.")
        return False