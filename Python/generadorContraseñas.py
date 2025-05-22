""" Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos) """

import random
import string

def generar_contrasena(longitud=12, mayusculas=True, numeros=True, simbolos=True):
    """Genera una contraseña aleatoria con los parámetros especificados."""
    
    # Definimos los caracteres que se pueden usar
    caracteres = string.ascii_lowercase  # Letras minúsculas
    if mayusculas:
        caracteres += string.ascii_uppercase  # Letras mayúsculas
    if numeros:
        caracteres += string.digits  # Números
    if simbolos:
        caracteres += string.punctuation  # Símbolos

    # Verificamos que la longitud esté dentro del rango permitido
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")

    # Generamos la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contrasena

# Ejemplo de uso
if __name__ == "__main__":
    longitud = int(input("Ingrese la longitud de la contraseña (8-16): "))
    mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

    contrasena = generar_contrasena(longitud, mayusculas, numeros, simbolos)
    print(f"Contraseña generada: {contrasena}")