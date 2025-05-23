#   Crea un programa que invierta el orden de una cadena de texto
#   sin usar funciones propias del lenguaje que lo hagan de forma automática.
#   - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

s = 'Hola mundo'
print(s)

for i in s[::-1] : 
  print(i, end= "")
print("\n")
