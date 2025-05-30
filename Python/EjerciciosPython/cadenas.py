#EJERCICO 1
""" Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido. """

# nombre = input("¿Cuál es tu nombre? ")
# numero = int(input("Introduce un número: "))

# print((nombre + "\n") * numero)

#EJERCICIO 2

# nombre = input("¿Cuál es tu nombre completo? ")

# print(nombre.lower())  # Convierte a minúsculas
# print(nombre.upper()) # Convierte a mayúsculas
# print(nombre.title()) # Convierte la primera letra de cada palabra en mayúscula

#EJERCICIO 3
""" Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre """

# nombre = input("¿Cuál es tu nombre? ")
# nombre = nombre.upper()  # Convierte a mayúsculas
# letras = len(nombre)

# print(f"{nombre} tiene {letras} letras")

#EJERCICIO 4
# telefono = input("Introduce tu número de teléfono con el formato +xx-xxxxxxxxx-xx: ") #+34-913724710-56
# telefono = telefono[4:-3] #Extraer los dígitos del 4 al 13
# print(f"El número de teléfono es: {telefono}")

#EJERCICIO 5

# frase = input("Introduce una frase: ")
# frase = frase[::-1]  # Invierte la cadena
# print(f"La frase invertida es: {frase}")

#EJERCICIO 6

# frase = input("Introduce una frase: ")
# vocal = input("Introduce una vocal: ")

# print(frase.replace(vocal, vocal.upper()))  # Reemplaza la vocal por su versión en mayuscula

#EJERCICIO 7
""" Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es. """

# correo = input("Introduce tu correo electrónico: ")

# print(correo[:correo.find("@")] + "@ceu.es") # Extrae la parte del correo antes del símbolo @

#EJERCICIO 8
""" Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido. """

# precio = (input("Introduce el precio del producto: "))
# punto = precio.find(".") # Encuentra la posición del punto decimal

# print(f"El precio del producto es {precio[:punto]} euros y {precio[punto + 1:]} centimos")

#EJERCICIO 9
""" Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter. """

# fechaNacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

# print("Dia:", fechaNacimiento[:2])
# print("Mes:", fechaNacimiento[3:5])
# print("Año:", fechaNacimiento[6:])

#EJERCICIO 10
""" Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta. """

# compra = input("Introduce los productos que has comprado:")
# print("He comprado estos productos:", compra.replace("," , "\n") )  # Imprime los productos antes de la coma

#EJERCICIO 11
""" Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales. """

# nombreProducto = input("Introduce el nombre del producto: ")
# precioProducto = float(input("Introduce el precio del producto: "))
# unidadesProducto = int(input("Introduce el número de unidades del producto: "))

# print("{nombreProducto}:{unidadesProducto:3d} unidades x{precioProducto:9.2f} euros ={costeTotal:11.2f} euros".format(
#     nombreProducto=nombreProducto,
#     unidadesProducto=unidadesProducto,
#     precioProducto=precioProducto,
#     costeTotal=unidadesProducto * precioProducto
# ))
