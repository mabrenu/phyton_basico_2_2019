#esto es un ejemplo de creacion de listas
#Practica #1 Incorporar listas dentro de una lista general
mis_frutas = [ 'fresas', 'manzana', 'mango', 'pera', 'naranja', 'piña']


verduras =['tomates', 'papas', 'cebollas', 'ajos']
frutas = ['piña','naranja', 'sandia']
carnes = ['mortadela','pollo', 'costilla de cerdo']
limpieza = ['jabon', 'cloro', 'shampoo']

listacompras= [verduras, frutas,carnes,limpieza]

print ('La consolidacion de listas es:',listacompras)
#Práctica #2 Conteo de todos los elementos de la lista general

conteo = 0
for categoria in listacompras:
    conteo += len(categoria)

print ('La cantidad es de elementos en mi listacompras',conteo)
