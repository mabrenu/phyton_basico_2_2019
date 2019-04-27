

#Práctica #3 Agregar 'Chile y Mango'

verduras =['tomates', 'papas', 'cebollas', 'ajos']
frutas = ['piña','naranja', 'sandia']
carnes = ['mortadela','pollo', 'costilla de cerdo']
limpieza = ['jabon', 'cloro', 'shampoo']

listacompras= [verduras, frutas,carnes,limpieza]
print('Lista Original', listacompras)

verduras.append('Chile')
frutas.append('Mango')
print('Append', listacompras)

#Práctica #4 Eliminar lista verduras
#limpiar elementos de la lista
listacompras.remove(verduras)
#Verduras.clear() - la lista queda vacia
#del Verduras
#verduras.clear()

print('Remove',listacompras)

#Modificación practica #2, conteo de elementos mediante aplacar listas contenidas en una sola
mi_lista=[]
for categoria in listacompras:
    mi_lista.extend(categoria)

print('mi_lista lista acoplada',mi_lista)
print ('La cantidad es',len(mi_lista))

