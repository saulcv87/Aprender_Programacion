# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */

s = input("Introduce todas las palabras que quieras: ")
palabra = s.split()  #Divide la cadena en palabras

def contar_palabras(s) :
    conteo_palabras = {}
    palabra = ""

    for caracter in s.lower() : 
        if caracter.isalnum() : 
            palabra += caracter
        else : 
            if palabra : 
                conteo_palabras[palabra] = conteo_palabras.get(palabra,0) + 1
                palabra = ""

    if palabra : 
        conteo_palabras[palabra] = conteo_palabras.get(palabra,0) + 1
    
    return conteo_palabras


resultado = contar_palabras(s)

for palabra, cantidad in resultado.items() :
    print(f"{palabra}: {cantidad}")
