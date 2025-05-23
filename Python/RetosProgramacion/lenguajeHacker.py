""" Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker"(conocido realmente como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

def lenguajeHacker(palabra):
    letras = {
        'a': '4',
        'b': '8',
        'c': '[',
        'd': ')',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': ',_|',
        'k': '>|',
        'l': '1',
        'm': '^^',
        'n': '^/',
        'o': '0',
        'p': '|*',
        'q': '(,)',
        'r': '|2',
        's': '5',
        't': '7',
        'u': '|_|',
        'v': '|/',
        'w': '\\/\\/',
        'x': '><',
        'y': 'j',
        'z': '2',
    }
    palabras = palabra.lower()
    text = ""
    for word in palabras:
        if word in letras.keys():
            text += letras[word]
        else:
            text += word
    return text
        

while True:
    palabra_orig = input("Escribe el texto a transformar: ")
    if palabra_orig.lower() == "exit":
        print("Saliendo del programa...")
        break
    palabra_cambiada = lenguajeHacker(palabra_orig)
    print(f"La nueva palabra es: {palabra_cambiada}")
    