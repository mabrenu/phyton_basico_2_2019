#PARTE 1
intentos= int(input('Dígame cuántas palabras tiene la lista:'))
if intentos > 0:
    posicion = 1
    lista_palabras =[]
    while posicion <= intentos:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras.append(palabra)
        posicion = posicion + 1
    print('La lista creada es:', lista_palabras)
else:
    print('¡Imposible!')


#PARTE 2
intentos= int(input('Dígame cuántas palabras tiene la lista:'))
if intentos > 0:
    posicion = 1
    lista_palabras =[]
    while posicion <= intentos:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras.append(palabra)
        posicion = posicion + 1
    print('La lista creada es:', lista_palabras)
else:
    print('¡Imposible!')

buscar = input('Dígame la palabra a buscar:')
conteo = lista_palabras.count(buscar)
print('La palabra', buscar, 'aparece ' + buscar + ' veces' if conteo > 0 else 'no aparece', 'en la lista.')


#PARTE 3
intentos= int(input('Dígame cuántas palabras tiene la lista:'))
if intentos > 0:
    posicion = 1
    lista_palabras =[]
    while posicion <= intentos:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras.append(palabra)
        posicion = posicion + 1
    print('La lista creada es:', lista_palabras)
else:
    print('¡Imposible!')

buscar = input('Sustituir la palabra:')
sustituir = input('por la palabra:')
indice = lista_palabras.index(buscar)
print(indice)

lista_palabras[indice] = sustituir
print('La lista es ahora:', lista_palabras)


#PARTE 4
intentos= int(input('Dígame cuántas palabras tiene la lista:'))
if intentos > 0:
    posicion = 1
    lista_palabras =[]
    while posicion <= intentos:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras.append(palabra)
        posicion = posicion + 1
    print('La lista creada es:', lista_palabras)
else:
    print('¡Imposible!')

eliminar = input('Palabra a eliminar:')
lista_palabras.remove(eliminar)
print('La lista es ahora:', lista_palabras)


#PARTE 5
intentos= int(input('Dígame cuántas palabras tiene la lista:'))
if intentos > 0:
    posicion = 1
    lista_palabras =[]
    while posicion <= intentos:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras.append(palabra)
        posicion = posicion + 1
    print('La lista creada es:', lista_palabras)
else:
    print('¡Imposible!')


eliminar= int(input('Dígame cuántas palabras tiene la lista de palabras a eliminar:'))
    posicion = 1
    lista_eliminar =[]
    while posicion <= eliminar:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_eliminar.append(palabra)
        posicion = posicion + 1
    print('La lista de palabras a eliminar es:', lista_eliminar)

lista_palabras = [n for n in lista_palabras if n not in lista_eliminar]
print('La lista es ahora:', lista_palabras)


#PARTE 6
intentos= int(input('Dígame cuántas palabras tiene la lista:'))
if intentos > 0:
    posicion = 1
    lista_palabras =[]
    while posicion <= intentos:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras.append(palabra)
        posicion = posicion + 1
else:
    print('¡Imposible!')

print('La lista creada es:', lista_palabras)
print('La lista inversa es:', lista_palabras[::-1])


#PARTE 7
intentos= int(input('Dígame cuántas palabras tiene la lista:'))
if intentos > 0:
    posicion = 1
    lista_palabras =[]
    while posicion <= intentos:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras.append(palabra)
        posicion = posicion + 1
else:
    print('¡Imposible!')

print('La lista creada es:', lista_palabras)
print('La lista sin repeticiones:', list(set(lista_palabras)))


#PARTE 8
primera= int(input('Dígame cuántas palabras tiene la primera lista:'))
if primera > 0:
    posicion = 1
    lista_palabras =[]
    while posicion <= intentos:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras.append(palabra)
        posicion = posicion + 1
    print('La primera lista es:', lista_palabras)
else:
    print('¡Imposible!')


segunda= int(input('Dígame cuántas palabras tiene la segunda lista:'))
    posicion = 1
    lista_palabras2 =[]
    while posicion <= segunda:
        palabra = input('Dígame la palabra ' + str(posicion) + ':')
        lista_palabras2.append(palabra)
        posicion = posicion + 1
    print('La segunda lista es:', lista_palabras2)

lista_iguales = [n for n in lista_palabras if n in lista_palabras2]
lista1 = [n for n in lista_palabras if n not in lista_palabras2]
lista2 = [n for n in lista_palabras2 if n not in lista_palabras]

print('Palabras que aparecen en las dos listas:', set(lista_iguales))
print('Palabras que sólo aparecen en la primera lista:', set(lista1))
print('Palabras que sólo aparecen en la segunda lista:', set(lista2))
print('Todas las palabras:', set(lista_palabras + lista_palabras2))

