#creaccion de diccionarios
#sintasis
#opcion 1
mi_dict = {
    'llave1' : 'valor1',
    'llave2' : 'valor2'
}
#opcion 2
otro_dic = dict(llave1 = 'valor1' ,
     llave2='valor2')


#Ejercicio 1
#Usando tuplas
mis_contactos = {('Juan','Perez'): [831013040,'jperez@gmail.com'],
                 ('Carlos',' Rojas'):[87001030,'crojas@hotmail.com'],
                 ('Ana','Marin'):[9100013,'ana@gmail.com']}



#problema para encontrar el usuario, hay que abrir todos los contactos para saber quien es el contacto buscado
mi_contacto = {
    'Contacto1' : ['Juan Perez',831013040,'jperez@gmail.com'],
    'Contacto2' : ['Carlos Rojas',87001030,'crojas@hotmail.com'],
    'Contacto3' :  ['Ana Marin', 9100013,'ana@gmail.com']}


#Ejemplo Resuelto por el profesor
agenda = {
    'Juan Perez': [831013040,'jperez@gmail.com'],
    'Carlos Rojas':[87001030,'crojas@hotmail.com'],
    'Ana Marin':[9100013,'ana@gmail.com']}

agenda = {
    'Juan Perez': {'telefono':831013040,
                   'correo':'jperez@gmail.com'},
    'Carlos Rojas':{'telefono':87001030,
                    'correo': 'crojas@hotmail.com'},
    'Ana Marin':{'telefono':9100013,
                 'correo':'ana@gmail.com'}}

agenda = {
    'Juan Perez': {'telefono':831013040,
                   'correo':'jperez@gmail.com'},
    'Carlos Rojas':{'telefono':87001030,
                    'correo': 'crojas@hotmail.com'},
    'Ana Marin':{'telefono':9100013,
                 'correo':'ana@gmail.com'}}


#Ejercicio#2
print('La cantidad de contactos es:',len(agenda))

#Ejercicio#3
print('Nombre de las llaves',list(agenda.keys()))

#Ejercicio#4
#keys, items: lista de tupla de keys y valores, values.
#x,y


agenda = {
    'Juan Perez': {'telefono':831013040,
                   'correo':'jperez@gmail.com'},
    'Carlos Rojas':{'telefono':87001030,
                    'correo': 'crojas@hotmail.com'},
    'Ana Marin':{'telefono':9100013,
                 'correo':'ana@gmail.com'}}

for x,y in agenda.items():
    print('Nombre:',x, 'Telefono:',y['telefono'],'','Email:',y['correo'])


#Ejercicio resulto por el profe
#keys()
for persona in agenda.keys():
    print('Nombre',persona,'Telefono',agenda[persona]['telefono'],'Email',agenda[persona]['correo'])
#values()

#Ejercicio#5

agenda = {
    'Juan Perez': {'telefono':831013040,
                   'correo':'jperez@gmail.com'},
    'Carlos Rojas':{'telefono':87001030,
                    'correo': 'crojas@hotmail.com'},
    'Ana Marin':{'telefono':9100013,
                 'correo':'ana@gmail.com'}}

agenda['Juan Perez']['telefono'] = [12356,52365]

#Ejercicio#6
#opcion#1
sofia ={'telefono':333333,'correo':'sofi@sofi'}
agenda['Sofia Castro'] = sofia

#opcion#2
agenda.update({'Sofia Alfaro': sofia})

