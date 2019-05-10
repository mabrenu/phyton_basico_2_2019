#Promedio de los valores de la lista
mis_valores = [5, 6, 10, 13, 3, 4]
promedio = 0
for i in mis_valores:
	promedio +=  i

print('El promedio de la lista es:', promedio / len(mis_valores) )


#Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas
personas = [
[177,145,167,190,140,150,180,130], # grupo 1
[165,176,145,189,170,189,159,190], # grupo 2
[145,136,178,200,123,145,145,134], # grupo 3
[201,110,187,175,156,165,156,135] # grupo 4
]

grande=0
for p in personas:
	if max(p) > grande:
		grande = max(p)
		list = p
print('Lista con el valor de mayor altura es: ',list)