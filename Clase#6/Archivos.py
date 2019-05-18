f=open('data.txt')
contenido = f.read()
f.close()
contenido


#from os import path
#ruta_path = path.join('directorio','data.txt')

#Escritura
archivo = open('data.txt','w')
archivo.write('primera linea\n')
archivo.write('segunda linea\n')
archivo.write('tercer linea\n')
archivo.close

#cerrar el archivo automaticamente
with open('data.txt','w') as f:
    f.write('Hello\n')

#Escritura de varias lineas
with open('data.txt','w') as f:
    f.writelines(['Primera linea\n','segunda linea\n', 'tercera linea\n'])
#-->>>hace un append

#Lectura
with open('data.txt','r') as f:
    text = f.read()

#todas las lineas al mismo tiempo
#f.readlines