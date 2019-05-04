#Ejemplos de funciones
#funcion sume dos #
def mi_suma(a,b):
    return a+b

c= mi_suma(1,5)
#c= mi_suma(a=1,b=5)
#Error c= mi_suma(b=5) pide el otro parametro missing

#Función sin parámetros
def f():
    a=9
    b=0
    print ('hola',a,b)

f() #resultado none

pass


#Ejercio#1
def mi_print(h):

    for i in range(1,h+1):
        print('*'*i)

mi_print(3)


#Ejercicio#2
agenda = {
    'Juan Perez': {'telefono':831013040,
                   'correo':'jperez@gmail.com'},
    'Carlos Rojas':{'telefono':87001030,
                    'correo': 'crojas@hotmail.com'},
    'Ana Marin':{'telefono':9100013,
                 'correo':'ana@gmail.com'}}


def add_agenda(a,b):
    return agenda.update({a:b})

add_agenda('Marilyn Brenes', {'telefono':1111,'correo':'mari@brenes'})
add_agenda('John Brenes', {'telefono':222,'correo':'john@brenes'})
pass


#Resuelto por el profe
def agregar_agenda(nombre, telefono, correo):
    return agenda.update({nombre: {'telefono':telefono,
                                  'correo':correo}})

agregar_agenda('Jean Brenes',1111,'jean@brenes')

pass