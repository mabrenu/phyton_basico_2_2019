x= lambda a : a+1
x(10)
pass

#cear funcion lambda sin parametros
(lambda : print('hola'))()

#crear función lambda sin parámetros
(lambda : 1+1)()

#Ejercicio 1
#calculadora
suma = lambda x,y : x+ y
resta = lambda x,y : x- y
multiplicacion = lambda x,y : x* y
division= lambda x,y : x/y
import math
potencia = lambda x,y : math.pow(x,y)
raiz = lambda  x,y : math.pow(x,1/y)


x = 3
y= 2

#lista_funciones =[suma, resta, multiplicacion, division, potencia, raiz]
#for mi_funciones in lista_funciones:
 #   print('Resultado=', mi_funciones(x,y))


#Ejercicio#2

dic_funciones ={'suma': lambda  x,y :x+y,
                'resta': resta,
                'multiplicacion':multiplicacion,
                'division': division,
                'potencia': potencia,
                'raiz': raiz}

for func in dic_funciones.keys():
    print('Resultado=', dic_funciones[func](x,y))

#for func in dic_funciones.values():
 #   print('Resultado=',func(x,y))
