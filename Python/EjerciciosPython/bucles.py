#EJERCICIO 1

# palabra = input("Dime una palabra... ")

# for i in range(10):
#     print(palabra)

#EJERCICO 2

# edad = int(input("Dime tu edad...."))

# for i in range (1,edad + 1,1):
#     print("Has cumplido " + str(i) + " años")

#EJERCICO 3

# num = int(input("Dime un numero......."))
# res = ""
# for i in range(num):
#     res +="*"
#     print(res)

#EJERCICO 4

# num= int(input("Dime un numero....."))

# for i in range(1,num + 1,2): 
#     for j in range(i,0,-2):
#         print(j, end=" ")
#     print("")

#EJERCICO 5
""" Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. """

# contraseña = "saul1234"
# password = ""

# while password != contraseña  :
#     password = input("Introduce tu contraseña: ")

#     if password != contraseña :
#         print("Contraseña Incorrecta. Por favor intentelo de nuevo")
#     else :
#         print("Contraseña Correcta")


#EJERCICIO 6

""" Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última. """

# palabra = input("Introduce una palabra: ")

# # for i in reversed(palabra) :  #usando la funcion reversed
# #     print(i) 

# for i in range(len(palabra)-1, -1,-1) : 
#     print(palabra[i])


#EJERCICO 7

""" Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase. """

# frase = input("Dime lo que quieras: ")
# letra = input("Dime una letra para comprobar cuantas veces se repite: ")
# count = 0

# for i in frase :
#     if i == letra : 
#         count += 1

# print(f"La letra '{letra}' se repite {count} veces")


#EJERCICIO 8

palabra = ""
while palabra != "salir":
    palabra = input("Di lo que quieras: ")
    if palabra == "salir":
        break
    print(palabra)