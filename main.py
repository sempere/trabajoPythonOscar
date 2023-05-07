

from componentes import *
from equipos import *
from distribuidores import *
from despachar import *
from info import *

# Menu Principal.....
while True:
    printMenu("Selecciona una opción:")
    printMenu("1. Componentes")
    printMenu("2. Equipos")
    printMenu("3. Distribuidores")
    printMenu("4. Despachar")
    printMenu("5. Días")
    printMenu("6. Info sistema")
    printMenu("7. Ficheros")
    printMenu("0. Salir")
   
    try:
        opcion = int(input())
    except:
        opcion = -1
    if opcion in list(range(8)):
        if opcion == 0: break
        if opcion == 1: componentes()
        if opcion == 2: equipos()
        if opcion == 3: distribuidores()
        if opcion == 4: despachar()
        if opcion == 5: dias()
        if opcion == 6: info_sistema()
        if opcion == 7: ficheros()
    else:
        printError("Ingresa un número válido")
