#pruebas con numeros
#no es necesario declarar una variable, no hay que ponerle precisión, ni tipo
a= 100000
pass
#typado dinámico, cambio de integer a float


#Practica hacer un código que calcule el área de un rectángulo
#Area= largo X ancho
largo = 10
ancho = 5
area = largo * ancho
print ('El área del rectángulo es', area )


#commando para preguntarle al usuario input
largo= input('Favor ingresar el largo')
print('El valor de largo es' ,largo, 'el tipo de largo es', type(largo))
#el resultado es un string debo convertirlo en entero

#Caso#1
largo = float(input('Favor ingresar el largo'))

#Caso#2
largo = input('Favor ingresar el largo')
largo = float(largo)

print('El valor de largo es' ,largo, 'el tipo de largo es', type(largo))


#Modificar el ejercicio para pedir al usuario los valores
largo = float(input('Favor ingresar el largo'))
ancho = float(input('Favor ingresar el ancho'))
area = largo * ancho
print('El área del rectángulo es', area )




