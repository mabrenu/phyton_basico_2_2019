from Vehiculo import vehiculo

auto = vehiculo("Carrera No lo use.. Maltratelo!!")
list_competidores = []

class ciclo(vehiculo, dict):
    def __init__(self,num_ciclo):
        self.Numero_ciclo = num_ciclo

    def agregar_competidores(self):
        camion = {'tipo': 'camion', 'avance': 0, 'posicion': 0, 'intento': 0}
        tractor = {'tipo': 'tractor', 'avance': 0, 'posicion': 0, 'intento': 0}
        sedan = {'tipo': 'sedan', 'avance': 0, 'posicion': 0, 'intento': 0}
        bus = {'tipo': 'bus', 'avance': 0, 'posicion': 0, 'intento': 0}

        # Agregando competidores
        auto.agregar_vehiculo(**camion)
        auto.agregar_vehiculo(**tractor)
        auto.agregar_vehiculo(**sedan)
        auto.agregar_vehiculo(**bus)

        list_competidores.append('camion')
        list_competidores.append('tractor')
        list_competidores.append('sedan')
        list_competidores.append('bus')

    def inicializar_ciclo(self):
        self.agregar_competidores()
        self.Numero_ciclo = +1

    def nuevo_ciclo(self, num_ciclo):
        for item in list_competidores:
            auto.rendimiento_avance(item)
            auto.intento_vehiculo(item)
            auto.posicion()
        print(auto)
        self.update({num_ciclo:auto})

    def eliminar_competidores(self):
        for k in auto.keys():
            if auto[k]['Avance'] > 1000 and k in list_competidores:
                list_competidores.remove(k)

    def iniciar_ciclo(self):
        print('imprimir ',len(list_competidores))

        while len(list_competidores) > 2:
            self.Numero_ciclo = len(self) + 1
            print('******* INICIO CICLO', self.Numero_ciclo,'*******' )
            self.nuevo_ciclo(self.Numero_ciclo)
            self.eliminar_competidores()

    def resultado_final(self):
        resultado = list(self.items())
        print('La carrera tuvo', self.Numero_ciclo,'ciclos. \n El resultado de la carrera es: ',resultado[-1])

    def imprimir(self):
        print('LISTA FINAL',self)
        #import pandas as pd
        #pd.DataFrame(self)