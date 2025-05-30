#EJERCICIO 1
""" Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no. """
# edad = int(input("Introduce tu edad: "))

# if edad > 18 :
#     print("Eres mayor de edad")
# else : 
#     print("Lo siento, aun no eres un hombre jajajajjjja")

# EJERCICIO 2

# contraseña = "saul1234"
# password = input("Introduce tu contraseña: ")

# if contraseña == password:
#     print("Contraseña correcta")
# else :
#     print("La contraña introducida es incorrecta")

# EJERCICIO 3
""" Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error. """

# print("Dime dos numeros para realizar una division....")
# n1 = int(input("Numero 1: "))
# n2 = int(input("Numero 2: "))

# if n2 == 0 :
#     print("El divisor no puede ser 0")
# else: 
#     division = n1 / n2
#     print(f"La division entre {n1} y {n2} es de: {division}")

#EJERCICO 4
""" Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde. """

# nombre = input("Cual es tu nombre?")
# sexo = input("Cual es tu sexo? (Hombre/Mujer)")

# if ("mujer" in sexo and "a" >= nombre[0].lower() < "m") or ("hombre" in sexo and "n" < nombre[0].lower()):
#     print(f"{nombre} perteneces al grupo A")
# else:
#     print(f"{nombre} perteneces al grupo B")

#EJERCICO 5

# renta = int(input("¿Cual es tu renta anual? "))

# if renta < 10000:
#     print("Te corresponde un 5% de tipo impositivo")
#     print("Por tanto tienes que pagar: ", renta*5 /100 , "euros")
# elif 10000 <= renta <= 20000:
#     print("Te corresponde un 15% de tipo impositivo")
#     print("Por tanto tienes que pagar: ", renta*15 /100 + "euros")  
# elif 20000 < renta <= 35000:
#     print("Te corresponde un 20% de tipo impositivo")
#     print("Por tanto tienes que pagar: ", renta*20 /100 + "euros")
# elif 35000 < renta <= 60000:
#     print("Te corresponde un 30% de tipo impositivo")
#     print("Por tanto tienes que pagar: ", renta*30 /100 + "euros")
# else :
#     print("Te corresponde un 45% de tipo impositivo")
#     print("Por tanto tienes que pagar: ", renta*45 /100 + "euros")

#EJERCICIO 6

# puntuacion = float(input("Dime tu puntuacion: "))

# if 0 == puntuacion:
#     nivel = "Inaceptable"
# elif 0.4 == puntuacion:
#     nivel = "Aceptable"
# elif 0.6 <= puntuacion:
#     nivel ="Meritorio"
# else:
#     nivel =""
# if nivel == "":
#     print("El rango indicado no se evalua")
# else:
#     cantidad = 2400 * puntuacion
#     print(f"Como tu nivel es {nivel} has conseguido {cantidad} euros")


#EJERCICIO 7

# edad = int(input("Dime tu edad: "))

# if edad < 4:
#     print("Entras gratis ya que eres un niño")
# elif 4 <= edad <= 18 :
#     print("Debes pagar por entrar 5 euros")
# elif edad > 18:
#     print("Debes pagar por entrar 10 euros")


#EJERCICIO 8

ing_veganos = ["pimiento", "tofu"] #Ingredientes vegetarianos
ing_no_veganos =["peperoni", "jamon", "salmon"] #Ingredientes no vegetarianos
ingredientes = ["tomate", "mozzarella"] #INGREDIENTES que estan en todas las pizzas

elecc_pizza = input("¿Te apetece una pizza vegetariana? (SI/NO) ")

if "si" in elecc_pizza:
    tipo_pizza = "vegetariana"
    print("Solo puedes elegir un ingrediente adicional de los siguientes ", ing_veganos)
    ingrediente_vegano = input("Dime tu eleccion: ")

    if "pimiento" in ingrediente_vegano : 
        ingredientes.append(ing_veganos[0])
    elif "tofu" in ingrediente_vegano :
        ingredientes.append(ing_veganos[1])
    else:
        print("El ingrediente introducido no esta en la lista")
else:
    tipo_pizza = "no vegetariana"
    print("Solo puedes elegir un ingrediente adicional de los siguientes ", ing_no_veganos)
    ingrediente_no_vegano = input("Dime tu eleccion: ")

    if "peperoni" in ingrediente_no_vegano :
        ingredientes.append(ing_no_veganos[0])
    elif "jamon" in ingrediente_no_vegano :
        ingredientes.append(ing_no_veganos[1])
    elif "salmon" in ingrediente_no_vegano:
        ingredientes.append(ingrediente_no_vegano[2])
    else: 
        print("El ingrediente introducido no esta en la lista")

print(f"La pizza es {tipo_pizza} y tiene los siguiente ingredientes: {ingredientes}")





