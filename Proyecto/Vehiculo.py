import math
import random

# LAMBA
dic_avance = {'camion': lambda x: 2 * x + 1,
              'tractor': lambda x: math.log(x, 2),
              'sedan': lambda x: 3 * x ** 2,
              'bus': lambda x: 5 * x}

class vehiculo(dict):
    def __init__(self, Nombre):
        self.nombre = Nombre

    def agregar_vehiculo(self, tipo, avance, posicion, intento):
        self.update({tipo: {'Avance': avance, 'Posicion': posicion, 'Intento': intento}})

    def rendimiento_avance(self, tipo):
        fuerza = random.randint(1, 9) if tipo == 'tractor' else random.randint(0, 9)
        self[tipo]['Avance'] = self[tipo]['Avance'] + math.floor(dic_avance[tipo](fuerza))
        self.update()

    def intento_vehiculo(self, tipo):
        self[tipo]['Intento'] = self[tipo]['Intento'] + 1
        self.update()

    def posicion(self):
        #posiciones = sorted(self.items(), key=lambda kv: (kv[1]['Avance'],-kv[1]['Intento']), reverse=True)
        posiciones = sorted(self.items(), key=lambda kv: (-kv[1]['Intento'],kv[1]['Avance']), reverse=True)
        for a in posiciones:
            self[a[0]]['Posicion'] = posiciones.index(a) + 1
        self.update()