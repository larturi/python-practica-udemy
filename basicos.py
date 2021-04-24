# import os
# clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
# clear()

# numero1 = 5
# type(numero1)

# numero2 = 6.5
# type(numero2)

# numero3 = 7
# type(numero3)

# suma = numero1 + numero2 + numero3
# print(suma)
# type(suma)

# ------------------
# cadena = "Leandro"
# cadena.upper()

# print(cadena)

# nombre = "Leandro"
# saludo = print(f"Hola {nombre}")

# cadena = "Esto es un texto de ejemplo"
# mostrar = cadena[11:16]
# print(mostrar)

# ------------------
# print("Introduce el primer numero: ")
# dato1 = input()
# print("Introduce el segundo numero: ")
# dato2 = input()

# numero1 = int(dato1)
# numero2 = int(dato2)

# suma = numero1 + numero2
# strSuma = str(suma)
# resultado = print(f"La suma es {strSuma}")

# frutas = ['pera', 'manzana', 'uva', 'banana']
# fruta1 = 'melon'
# fruta2 = 'pera'
# resultado1 = fruta1 in frutas
# resultado2 = fruta2 in frutas
# print(resultado1)
# print(resultado2)

# ------------------
# frutas = {"manzana": "apple", "naranja": "orange", "banana": "bannana", "limon": "lemon"}
# print(frutas["naranja"])
# frutas["piña"] = "pineapple"

# for clave, valor in frutas.items():
#     print(clave + " en ingles es: " + valor)

# ------------------
# nota = 9.5
# trabajo_realizado = True

# if (nota >= 4 and trabajo_realizado == True):
#   nota_final = "Aprobado"
# else:
#   nota_final = "Desaprobado"

# print(nota_final)

# ------------------
# inicio = 1
# valor = 6

# while (inicio < 6):
#   print("Esta es la fila " + str(inicio))
#   inicio += 1

# ------------------
# class Coche:
#     def __init__(self, marca, color, combustible, cilindrada):
#         self.marca = marca
#         self.color = color
#         self.combustible = combustible
#         self.cilindrada = cilindrada

#     def mostrar_caracteristicas(self):
#         print("Este coche es de la marca {}, de color {}, de {} y una cilindrada de {}".format(self.marca, self.color, self.combustible, self.cilindrada))

# coche1 = Coche("Tesla", "Gris", "Electrico", "8")

# coche1.mostrar_caracteristicas()

# ------------------
# media = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3) / 3
# print(media(4, 6, 8))


import camelcase

camel = camelcase.CamelCase()

texto = "mi nombre es leandro"

print(camel.hump(texto))