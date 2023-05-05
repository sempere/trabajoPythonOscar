class Componente:
  def __init__(self, id, tipo, peso, coste, cantidad):
    self.id = id
    self.tipo = tipo
    self.peso = peso
    self.coste = coste
    self.cantidad = cantidad

  def setCantidad(self, cantidad):
    self.cantidad = cantidad