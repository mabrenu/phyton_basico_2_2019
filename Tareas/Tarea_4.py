#Tarea 4. lamba y diccionario de funciones
#cantidad en miles en la cuenta del banco,n crédito en miles de colones y la tercer columna en miles de colones en deuda.

hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]
#la transpuesta(cambiar las columnas por las filas)

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]
b = transpuesta(hoja_calculo)

# dividir todos los números entre 10
b[1] = list(map(lambda x: x/10, b[1]))
print(b)

#Parte 1
#Contruya un diccionario de funciones matematicas (utilizando funciones lambda) Promedio,+,*

dic_funciones ={
                'suma': lambda x: sum(x),
                'multiplicacion': lambda x: x[0]*x[1]*x[2],
                'promedio': lambda x: (sum(x)/float(len(x))),
                'impuesto': lambda x: x*1.2
               }

#Parte 2
print('Promedio Débito de todas las personas',":",str(dic_funciones['promedio'](b[1])))
print('Suma de las deudas todas las personas',":",str(dic_funciones['suma'](b[3])))
print('Multiplicación de todos los créditos',":",str(dic_funciones['multiplicacion'](b[2])))


#Parte 3
#Actualice (en la tabla general)los valores de los créditos aplicando un impuesto del 20% (esto es multiplicar por 1.2)
#a toda la fila de créditos usando el diccionario de funciones.

for a in hoja_calculo:
   a[1]=dic_funciones['impuesto'](a[1])

print('Aumento de impuesto en créditos',":",hoja_calculo)

