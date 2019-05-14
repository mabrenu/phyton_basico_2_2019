#Tarea 5. Programación orientado a Objetos: Nieto y abuelos

# Misc classes
class misc:
    def __repr__(self):
        # return the clase name
        return self.__class__.__name__

    def __str__(self):
        # return the clase name
        return self.__class__.__name__
#La defición de lo que es un animal con sus funciones básicas, al menos muestra lo que intenta hacer

class Animal(misc):
    def __init__(self, especie):
        self.especie = especie

    def reproducirse(self):
        print(f'El {self} está reproduciendose')

    def comer(self):
        print(f'El {self} está comiendo')

    def crecer(self):
        print(f'El {self} está creciendo')

    def nacer(self):
        print(f'El {self} está naciendo')

    def morir(self):
        print(f'El {self} está muriendo')
#El mono puede basarse en la estructura y definiciones de lo que es un Animal

class Mono(Animal):
    def __init__(self):
        super().__init__(especie='Mono')
        self.cola = True

    def jugar(self):
        print(f'El {self.especie} está jugando')

    def mueve_la_cola(self):
        print(f'El {self.especie} mueve la cola')
#El humano puede definirse basado en un mono. Incluyendo eliminando la cola. La especie es humano.

class Humano(Mono):
    def __init__(self):
        self.especie = 'Humano'
        self.cola = False

    def mueve_la_cola(self):
        if not self.cola:
            print(f'El {self.especie} no tiene cola')
        else:
            print(f'El {self.especie} tiene cola')
yo = Humano()
yo
Humano
print(yo)
Humano
yo.nacer()
yo.mueve_la_cola()
yo.morir()

Tarea
#Basado en el ejemplo anterior, crear un Nieto Humano, basado en las habilidades aprendidas por el abuelo humano y transmitidas al padre Humano.
#Abuelo -> padre -> Nieto


class Abuelo(Humano):
    def __init__(self):
        self.especie = 'Humano'
        self.cola = False

    def mueve_la_cola(self):
        if not self.cola:
            print(f'El {self.especie} no tiene cola')
        else:
            print(f'El {self.especie} tiene cola')
yo = Humano()
yo
Humano
print(yo)
Humano
yo.nacer()
yo.mueve_la_cola()
yo.morir()



#El abuelo trabaja. El padre es contador y el nieto es analista de negocios
#El nieto tiene que ir a trabajar, sabe de contabilidad es un analista de negocios