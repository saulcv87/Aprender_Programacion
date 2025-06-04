#EJERCICIO 1
""" Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir. """

# lista = ["Mates", "Historia", "Lengua", "Fisica", "Quimica"]

# notas = []
# for i in lista:
#     nota = float(input("¿Qué nota has sacado en " + i + "? "))
#     notas.append(nota)

# for i in range(len(lista)-1, -1,-1) : 
#     if notas[i] >= 5.0 :
#         lista.pop(i)

# print("Debes repetir estas asignaturas: " + str(lista))


#EJERCICIO 2
# lista = []
# inverso = []

# for i in range(1,11,1) : 
#     lista.append(i)

# for i in range(len(lista), 0, -1) : 
#     inverso.append(i)

# print(inverso)


#EJERCICO 3

""" Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante. """

# abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(len(abecedario)-1, 0, -1) :
#     if i % 3 == 0 :
#         abecedario.pop(i)

# print(abecedario)


#EJERCICIO 4

precios = [50,75,46,22,80,65,8]

min = max = precios[0] #el primer numero siempre es el minimo y maximo al principio de una lista
for i in precios:
    if i > max :
        max = i
    if i < min :
        min = i
print("El maximo es",max)
print("El minimo es",min)