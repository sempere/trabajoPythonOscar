from estructuras import *

#Funciones de prueba, inicializando datos para testing
componentes_list.append(Componente('comp1', 'Fuente', 50, 10.5, 10))
componentes_list.append(Componente('comp2', 'PB', 50, 10.5, 10))
componentes_list.append(Componente('comp3', 'TG', 50, 10.5, 10))
componentes_list.append(Componente('comp4', 'CPU', 50, 10.5, 10))
componentes_list.append(Componente('comp5', 'RAM', 50, 10.5, 10))
componentes_list.append(Componente('comp6', 'Disco', 50, 10.5, 10))

componentes_list.append(Componente('comp10', 'Fuente', 10, 10.5, 10))
componentes_list.append(Componente('comp20', 'PB', 10, 10.5, 10))
componentes_list.append(Componente('comp30', 'TG', 10, 10.5, 10))
componentes_list.append(Componente('comp40', 'CPU', 10, 10.5, 10))
componentes_list.append(Componente('comp50', 'RAM', 10, 10.5, 10))
componentes_list.append(Componente('comp60', 'Disco', 10, 10.5, 10))

#Funciones de prueba, inicializando datos para testing
equipo = Equipo(id='equipo1')
equipo.addComponente('Fuente', componentes_list[0])
equipo.addComponente('PB', componentes_list[1])
equipo.addComponente('TG', componentes_list[2])
equipo.addComponente('CPU', componentes_list[3])
equipo.addComponente('RAM', componentes_list[4])
equipo.addComponente('Disco', componentes_list[5])
equipos_disponibles.append(equipo)

equipo2 = Equipo(id='equipo2')
equipo2.addComponente('Fuente', componentes_list[0])
equipo2.addComponente('PB', componentes_list[1])
equipo2.addComponente('TG', componentes_list[2])
equipo2.addComponente('CPU', componentes_list[3])
equipo2.addComponente('RAM', componentes_list[4])
equipo2.addComponente('Disco', componentes_list[5])
equipos_disponibles.append(equipo2)

equipo3 = Equipo(id='equipo3')
equipo3.addComponente('Fuente', componentes_list[0])
equipo3.addComponente('PB', componentes_list[1])
equipo3.addComponente('TG', componentes_list[2])
equipo3.addComponente('CPU', componentes_list[3])
equipo3.addComponente('RAM', componentes_list[4])
equipo3.addComponente('Disco', componentes_list[11])
equipos_disponibles.append(equipo3)

#Prueba de distribuidores
dist = Distribuidor(id='dist1', nombre='InforRapid', tiempoEntrega=10, direccion='Consell de Cent 123, Local 4, 08015, Barcelona, Barcelona')
distribuidores_list.append(dist)
dist1 = Distribuidor(id='dist2', nombre='MediaMarkt', tiempoEntrega=4, direccion='Calle Ricard Vicent n9 El Puig Valencia 46540')
distribuidores_list.append(dist1)