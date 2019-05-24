from Agenda import Clinica

class Proyecto(Clinica):

    clinica = Clinica('Clinica los Ángeles')
    clinica = clinica.inicilizarlista()
    clinica.reporte_pacientes()

    #--------------------------------------------------Nuevos pacientes de hoy
    rocio = {'identificación':1,'Nombre':'Rocio','Apellido':'Mora','teléfono':2222221,
    'dirección':'San Jose 3 st, 5 Av','lista_enfermedades' : ['dolor de cabeza'],
    'lista_medicamentos': ['aspirina', 'panadol']}

    juanita = {'identificación':2,'Nombre':'Juanita','Apellido':'Fernandez','teléfono':2222223,
    'dirección':'Heredia 1 st, 3 Av','lista_enfermedades' : ['dolor de espalda'],
    'lista_medicamentos': ['voltaren', 'panadol']}

    fausto = {'identificación':3,'Nombre':'Maia','Apellido':'Picado','teléfono':2222225,
    'dirección':'Cartago 5 st, 9 Av','lista_enfermedades' : ['Fibroma', 'dolor de cabeza'],
    'lista_medicamentos': ['voltaren', 'panadol']}

    #Agregando pacientes
    clinica.agregarPaciente(**rocio)
    clinica.agregarPaciente(**juanita)
    clinica.agregarPaciente(**fausto)

    clinica.salvar_ListaPacientes()
    clinica.reporte_pacientes()

    #Eliminar paciente
    clinica.eliminarPaciente(1)
    clinica.salvar_ListaPacientes()
    clinica.reporte_pacientes()