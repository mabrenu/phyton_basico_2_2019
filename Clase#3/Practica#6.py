#Práctica Crear una tupla

t= ('mango','uvas','manzana','pera')
print('Tupla original',t)

#Práctica2 Agregar a piña
#p=('piña',)
p= tuple(['piña'])
a= t + p
print('Tupla original + piña', a)

#Práctica 3
print(t[0:-1])
print(t[::2]) #Salto de dos en dos
print(t[::-2]) #Salto en Reversa
#for element in range(0, len(a)):
 #   if element%2!=0:
  #      print(element, a[element])
