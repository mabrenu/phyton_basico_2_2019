# lambda funcion para aplanar la lista de listas
flatten = lambda l: [item for sublist in l for item in sublist]
flattenDic = lambda l: [repr(sublist) + '\n' for sublist in l.items()]


def returnNotMatches(a, b):
    a = set(a)
    b = set(b)
    return [list(b - a), list(a - b)]

def intersection(a, b):
    a = set(a)
    b = set(b)
    return list(b & a)


class Clinica(dict):
    def __init__(self, nombre):
        self.nombre = nombre

    def agregarPaciente(self,identificación, Nombre, Apellido, teléfono, dirección,
                        lista_enfermedades,lista_medicamentos):
        self.update({
            identificación :{
            'Nombre':Nombre,'Apellido':Apellido,'teléfono':teléfono,
            'dirección':dirección,
            'lista_de_enfermedades_tratadas':lista_enfermedades,
            'lista_de_medicamentos_que_toma':lista_medicamentos}})
        print('Paciente agregado', repr(self[identificación]))


    def eliminarPaciente(self,identificacion):
        print('Borrando Paciente', repr(self[identificacion]))
        if identificacion in self:
            del self[identificacion]

    def agregarMedicamento(self, identificacion,medicamento):
        self[identificacion]['lista_de_medicamentos_que_toma'].append(medicamento)

    def agregarenfermedad(self, identificacion,enfermedad):
        self[identificacion]['lista_de_enfermedades_tratadas'].append(enfermedad)

    def enfermedades_tratadas(self):
        return flatten([self[paciente_id]['lista_de_enfermedades_tratadas'] for paciente_id in self.keys()])

    def medicamentos_recetados(self):
        return flatten([self[paciente_id]['lista_de_medicamentos_que_toma'] for paciente_id in self.keys()])

    def comparar_pacientes(self, paciente1_id, paciente2_id):
        #Creando funcion reporte. notese que el formato es similar
        def reporte(Mensaje, funcion_a_ejecutar, detalle):
            print(Mensaje,
                  'Paciente:' ,paciente1_id,
                  'Paciente:', paciente2_id,
                  funcion_a_ejecutar(
                      self[paciente1_id][detalle],
                      self[paciente2_id][detalle])
                  )
        reporte('Medicamentos en común', intersection, 'lista_de_medicamentos_que_toma')
        reporte('Medicamentos diferentes', returnNotMatches, 'lista_de_medicamentos_que_toma')
        reporte('Enfermedades en común', intersection, 'lista_de_enfermedades_tratadas')
        reporte('Enfermedades diferentes', returnNotMatches, 'lista_de_enfermedades_tratadas')

    def salvar_ListaPacientes(self):
        import pickle
        with open('Agenda Clinica.pickle', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def inicilizarlista(self):
        import pickle
        with open('Agenda Clinica.pickle', 'rb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            a = pickle.load(f)
            return a

    def reporte_pacientes(self):
        import datetime
        print('\n---------------------Buen Día--------------------------------------\n---------------------Lista de Pacientes----------------------------\n',
              datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        for key, val in self.items():
            print('Identificación:', key, "=>", val)

        print('---------------------Fin Reporte-----------------------------------\n')
