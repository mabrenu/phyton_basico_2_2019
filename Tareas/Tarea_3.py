# Para definir la agenda del hospital
agenda_hospital = []
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')
# agregamos una persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)

# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)

# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]
# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)
print(agenda_hospital)

# notemos que la impresión en pantalla está un poco sucia... lo arreglamos
for paciente in agenda_hospital:
    print(paciente)

############DESARROLLO TAREA #3
#PRIMERA pregunta
    print('Respuesta#1 La cantidad de pacientes es:', len(agenda_hospital))

#SEGUNDA pregunta
conteopacientes = 0
for paci in agenda_hospital:
    if 'dolor' in paci:
        conteopacientes+=1
print('Respuesta#2 La cantidad de pacientes con dolor son:' , conteopacientes)

#TERCERA pregunta
agenda_hospital.sort(key=lambda x: x[3])
print(agenda_hospital)

#CUARTA pregunta
mayor = 0
menor = 0
for a in agenda_hospital:
    if a[3] >= 18:
        mayor+=1
    else:
        menor+=1
print('La cantidad de pacientes menores de edad:', menor, 'Los pacientes mayores de edad:', mayor)

#QUINTA pregunta
sort_dolor= sorted(agenda_hospital, key=lambda x: x[5],reverse=True)
sort_age= sorted(sort_dolor, key=lambda x: x[3])
print('La lista ordenada por prioridad gravedad y edad:',sort_age)

#SEXTA pregunta
#Suponga que los que tienen dolor mueren :( Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.
print(agenda_hospital)

posicion = 0
while posicion < len(agenda_hospital):
    if 'dolor' in agenda_hospital[posicion]:
        agenda_hospital.pop(posicion)
    else:
        posicion = posicion + 1

agenda_hospital.sort(key=lambda x: x[3])
print(agenda_hospital)