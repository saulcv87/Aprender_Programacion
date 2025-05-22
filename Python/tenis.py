""" Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.  """

def partido_tenis(puntos):
    # Definimos las puntuaciones
    puntuaciones = ["Love", 15, 30, 40, "Deuce", "Ventaja"]
    # Inicializamos los puntos de los jugadores
    p1 = 0
    p2 = 0

    # Iteramos sobre la secuencia de puntos
    for punto in puntos:
        if punto == "P1":
            p1 += 1
        elif punto == "P2":
            p2 += 1

        # Mostramos el estado actual del juego
        if p1 < 4 and p2 < 4 and (p1 != 3 or p2 != 3):
            print(f"{puntuaciones[p1]} - {puntuaciones[p2]}")
        elif p1 == 3 and p2 == 3:
            print("Deuce")
        elif p1 == 4 and p2 == 3:
            print("Ventaja P1")
        elif p2 == 4 and p1 == 3:
            print("Ventaja P2")
        elif p1 >= 4 and (p1 - p2) >= 2:
            print("Ha ganado el P1")
            return
        elif p2 >= 4 and (p2 - p1) >= 2:
            print("Ha ganado el P2")
            return
        
# Ejemplo de uso    
puntos = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
partido_tenis(puntos)

