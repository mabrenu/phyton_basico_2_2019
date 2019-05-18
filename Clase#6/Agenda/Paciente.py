agenda = {}

class Paciente:

    def __init__(self,identificacion, datosGenerales = {} ):
        self.id = identificacion
        self.datos = datosGenerales

    def agregarPaciente(self):
        agenda.update({'Identificacion':self.id, 'Paciente': self.datos})

    def eliminarPaciente(self, id):
       del agenda[id]


hola = Paciente('12304523', {'jola': 1230})
hola.agregarPaciente(hola)
adios = Paciente('1', {'jola': 2242})
adios.agregarPaciente()
adios.eliminarPaciente('12304523')
pass
print('esta',agenda)