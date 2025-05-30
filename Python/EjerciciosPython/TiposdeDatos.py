""" Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido. """

#nombre = input("¿Cuál es tu nombre? ")
#print(f"Hola {nombre}, bienvenido al curso de Python.")

#EJERCICIO 2
# """ suma = 3 + 2
# multiplicacion = 2 * 5
# division = suma / multiplicacion
# potencia = division ** 2
# print(f"El resultado de la operacion aritmetica es: {potencia}") """

#EJERCICIO 3
""" Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde. """
# horas = input("¿Cuántas horas trabajaste? ")
# coste = input("¿Cuál es el coste por hora? ")

# sueldo = float(horas) * float(coste)
# print(f"El sueldo es: {sueldo} euros")

#EJERCICIO 4
""" Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
primeros enteros positivos puede ser calculada de la siguiente forma: """

# numero = int(input("Introduce un número: "))
# suma = numero * (numero + 1)/ 2 
# print(f"La suma de los números del 1 al {numero} es: {suma}")

#EJERCICIO 5
""" Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales. """

# peso = float(input("Introduce tu peso en kg: "))
# altura = float(input("Introduce tu altura en metros: "))

# imc = peso / (altura ** 2)
# print(f"Tu IMC es: {imc:.2f}")

#EJERCICIO 6
""" Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente. """

# numero1 = int(input("Introduce el primer número: "))
# numero2 = int(input("Introduce el segundo número: "))
# division = numero1 / numero2
# resto = numero1 % numero2
# print(f"La división de {numero1} entre {numero2} da un cociente {int(division)} y un resto {resto} ")

#EJERCICIO 7
""" Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado. """

# payasos = int(input("¿Cuántos payasos vendiste? "))
# muñecas = int(input("¿Cuántas muñecas vendiste? "))

# peso_payaso = 112
# peso_muñeca = 75

# peso_total = payasos * peso_payaso + muñecas * peso_muñeca

# print(f"El peso total del paquete es de: {peso_total}")

#EJERCICIO 8
""" Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total. """

# pan_precio = 3.49
# pan_descuento = 0.40 # 60% de descuento

# pan_no_dia_descuento = round(pan_precio * pan_descuento, 2)

# pan_no_dia = int(input("Barras vendidas que nos son del dia: "))
# print(f"El precio de una barra de pan del dia es de {pan_precio} y si no es del dia tiene un descuento del 60%, que se le quedaria en {pan_no_dia_descuento}")

# precio_descuento = round(pan_no_dia_descuento * pan_no_dia,2)

# print(f"Ganancias total de panes que no son del dia: {precio_descuento} euros")