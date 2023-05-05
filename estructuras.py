# Estructuras
componentes_list = []
equipos_disponibles = []
equipos_despachados = []
despachos = dict()
distribuidores_list = []


tiposComponentes = ["Fuente", "PB", "TG", "CPU", "RAM", "Disco"]

def inicializa():
    # Estructuras
    componentes_list.clear()
    equipos_disponibles.clear()
    equipos_despachados .clear()
    distribuidores_list.clear()
    despachos.clear()

#Definicion de la clase componente
class Componente:
    def __init__(self, id=-1, tipo='', peso=1, coste=1, cantidad=1):
        self.id = id
        self.tipo = tipo
        self.peso = peso
        self.coste = coste
        self.cantidad = cantidad        
    def decStock(self):
        self.cantidad -= 1
    def incStock(self):
        self.cantidad += 1
    def __str__(self):
        cadena="Componente id: " + self.id+",Tipo: "+self.tipo+",Peso: "+str(self.peso) + ",Coste: " + str(self.coste) + ",Cantidad: " + str(self.cantidad) + ")"
        return cadena
    
#Definicion de la clase equipo
class Equipo:
    def __init__(self, id=-1):
        self.id = id
        self.componentes = {}
    def addComponente(self, tipo, componenteNuevo):
        componenteAnterior = self.componentes.get(tipo)
        if componenteAnterior is None:
            self.componentes[tipo] = componenteNuevo;
            componenteNuevo.decStock()
        elif componenteAnterior.id != componenteNuevo.id:
            componenteAnterior.incStock()
            self.componentes[tipo] = componenteNuevo;
            componenteNuevo.decStock()  
    def addComponentes(self, dict):
        for key in dict:
            self.addComponente(key, dict[key]) 
    def eliminaComponentes(self):
        for c in self.componentes:
            self.componentes[c].incStock()
    def getComponente(self, tipo):
        return self.componentes[tipo]
    def __str__(self):
        cadena="Equipo id: " + self.id + "\n"
        cadena += "\tComponentes: ("
        for tipo in self.componentes:
            cadena += self.componentes[tipo].__str__()
            cadena += ","
        cadena += ")\n"
        return cadena
        
#Definicion de la clase componente
class Distribuidor:
    def __init__(self, id=-1, nombre='', tiempoEntrega=1, direccion=""):
        self.id = id
        self.nombre = nombre
        self.tiempoEntrega = tiempoEntrega
        self.direccion = direccion
        
    def __str__(self):
        cadena="Distribuidor id: " + self.id+",Nombre: "+self.nombre+",Tiempo de entrega: "+str(self.tiempoEntrega) + ",Direccion: " + self.direccion + ")"
        return cadena
    
class Despacho:
    def __init__(self, distribuidor=Distribuidor(), equipo=(), tiempoRestante=0):
        self.distribuidor = distribuidor
        self.equipo = equipo
        self.tiempoRestante = tiempoRestante
    def decTiempo(self, tiempo):
        self.tiempoRestante -= tiempo
        return self.tiempoRestante 
    def __str__(self):
        cadena="Despachando equipo:\n"
        cadena += "\t" + self.equipo.__str__() +"\nTiempo restante en días: "+str(self.tiempoRestante) + ""
        return cadena