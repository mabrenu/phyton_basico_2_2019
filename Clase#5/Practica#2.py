#Calculadora
class CalculadoraBasica:
    def capturar_valores(self, a,b):
        self.a=a
        self.b=b
    #método de suma

    def sum(self):
        return self.a + self.b

    def multiplicar(self):
        return self.a * self.b


    #permite tener control de la ejecución de
    #todo el file, puedo exe métodos de otros lados, solo se ejecute ciertas cosas..ejecute solo una parte
if __name__ == "__main__":
    miCalculadora= CalculadoraBasica()
    resultado =0
    print('Bienvenido a la calculadora básica')
    operacion =  input('Ingrese la función realizar \n')

    miCalculadora.capturar