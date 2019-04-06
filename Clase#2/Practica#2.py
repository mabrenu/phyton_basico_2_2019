"""
Crear un código que calcule las soluciones de la ecuación cuadrática
de la fórmula  aX2 + bx +c=0
"""


import math
#math.sqrt() raiz cuadrada
#elevado 2**2
a = float(input('Favor ingresar a'))
b = float(input(''
                'Favor ingresar b'))
c = float(input('Favor ingresar c'))

discriminante =b**2 - 4*a*c
if discriminante <0:
    raiz=math.sqrt(-discriminante) * complex(0,1) #meter el número complejo i
else:
    raiz=math.sqrt(discriminante)

resultado = (-b+raiz)/ (2*a)

resultado2 = (-b-raiz)/ (2*a)
print('El resultado de las ecuaciones son:',resultado, resultado2)