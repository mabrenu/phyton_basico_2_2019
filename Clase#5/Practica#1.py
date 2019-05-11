#Practica 1
#lista = [1,2,7,1,9,2]
#num=[(lambda x:i>x)(i)for i in lista]
#print(num)

class First:
    def __init__(self):
        print('Constructor ejecutado')
a = First()
print(type(a))


class Duck:
    def quak(self):
        print('Quaaaack!')

    def walk(self):
        print('Walks like a duck')

#Nace un pato llamado donald
donald = Duck()
#Dpmañd dice Quack y camina
donald.quak()
donald.walk()

print(type(donald))


#-----------Ejemplo#2
class Duck:
    def __init__(self, nombre):
        self.duck_nombre = nombre

    def quak(self):
            print('Quaaaack!')

    def walk(self):
        print('Walks like a duck')

#Nace un pato llamado donald
donald = Duck('donald')
#Dpmañd dice Quack y camina
donald.quak()
donald.walk()
print('¿Cuál es tu nombre?', donald.duck_nombre)

#----------Ejemplo#3
class Animal:
    def __init__(self,e,a):
        self.especie = e
        self.edad = a

    def correr(self):
        print('Soy un {}. ' #autocompleta con el atributo
              'Estoy corriendo'.format(self.especie))

    def crecer(self,edad=0):
        if(self.edad + edad) > 14:
            self.vivo = False
        else:
            self.edad += edad
            self.vivo = True

perro= Animal('perro',3)
print("Hola soy un {} " "tengo {} años.".format(perro.especie,
                              perro.edad))

perro.crecer(10)
print("Hola soy un {} " "tengo {} años.".format(perro.especie,
                                                perro.edad))

if perro.vivo:
    print("Hola soy un {} " "tengo {} años.".format(perro.especie,
                                  perro.edad))
else:
    print('...Me mori...RIP')





#Ejercicio#1,2
class Bebe:
    def __init__(self,nombre):
        self.bebe_nombre= nombre
        self.edad=0
    def respirar(self):
        print('El bebé respira')
    def comer(self):
        print('El bebé comer')
    def llorar(self):
        print('El bebé llorar')
    def dormir(self):
        print('El bebé dormir')
    def crecer(self,edad=1):
        self.edad += edad
        print('El bebé {}' ' tiene {} años.'.format(self.bebe_nombre,self.edad ))


ninno= Bebe('Spiderman')
ninno.respirar()
ninno.comer()
ninno.llorar()
ninno.dormir()
print('Bebé como te llamas: Me llamo', ninno.bebe_nombre)
ninno.crecer(10)
ninno.crecer()


