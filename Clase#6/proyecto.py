
#esto es un proyecto que usa otros modulos
from Modulo1 import suma_resta
#from Modulo1 import.*
#from Modulo1 import nombre_de_variables

resultado = suma_resta(a=10,b=3,c=2)
#resultado = sum(10,3,2)

print(resultado)

#los import pueden estar en cualquier lugar

from Modulo2 import mi_lista
from Modulo2 import mi_diccionario

# from Modulo2 import mi_lista,mi_diccionario

print('Ejemplo')
from mi_Folder.Modulo3 import Pato
donald = Pato()
p = donald.camina()

