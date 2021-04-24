import ficheros

nombre_fichero = 'prueba.txt'

fichero = ficheros.Fichero(nombre_fichero)

fichero.write('Este es el texto de la primera linea. \n')

fichero.append('Este es el texto de la segunda linea. \n')

print(fichero.read())