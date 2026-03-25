from hangman import Hangman
import random
import uuid
from datetime import datetime

def main():
    print("Bienvenidos al juego del Ahorcado")

    juego = Hangman()
    juego.load("data/words.csv")

    # Mostrar resumen
    juego.resumen_palabras()

    # Validación
    if juego.get_number_of_words() == 30:
        print("\nPalabras listas, ¡adelante!")
    else:
        print("\nVaya, parece que no encontramos todas las palabras necesarias, no podemos dar comienzo al juego.")
        return

    # Pedir nombre
    usuario = input("Introduce tu nombre: ")
    print(f"Hola {usuario}, comienza la partida!")

    # Datos de partida
    game_id = str(uuid.uuid4())
    start_date = datetime.now()
    puntuacion = 0

    # Dificultad
    print("\nSelecciona dificultad:")
    print("1. Facil (9 intentos)")
    print("2. Normal (7 intentos)")
    print("3. Dificil (5 intentos)")

    opcion = input("Elige opción: ")

    if opcion == "1":
        max_intentos = 9
        pistas_restantes = 999
    elif opcion == "2":
        max_intentos = 7
        pistas_restantes = 2
    else:
        max_intentos = 5
        pistas_restantes = 0

    # Palabras usadas
    palabras_usadas = []
    rondas = 3

    for ronda in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda} ---")

        while True:
            palabra = juego.get_random_word()
            if palabra not in palabras_usadas:
                palabras_usadas.append(palabra)
                break

        print("Se ha seleccionado una palabra al azar")

        juego.mostrar_palabra_oculta(palabra)

        letras_acertadas = []
        letras_falladas = []
        intentos = 0

        while True:
            letra = input("Introduce una letra o 'pista': ").lower().strip()

            # PISTA
            if letra == "pista":
                if pistas_restantes > 0:
                    pistas_restantes -= 1

                    letras_no = []
                    for l in palabra:
                        if l not in letras_acertadas:
                            letras_no.append(l)

                    if len(letras_no) > 0:
                        pista = random.choice(letras_no)
                        print("Pista:", pista)

                    print("Pistas restantes:", pistas_restantes)
                else:
                    print("No tienes pistas")
                continue

            if len(letra) != 1:
                print("Introduce solo una letra")
                continue

            if letra in letras_acertadas or letra in letras_falladas:
                print("Ya has usado esa letra")
                continue

            acierto = juego.comprobar_letra(palabra, letra)

            if acierto:
                letras_acertadas.append(letra)
            else:
                intentos += 1
                letras_falladas.append(letra)

                print(f"Intentos fallidos: {intentos}/{max_intentos}")
                print(f"Intentos restantes: {max_intentos - intentos}")

                juego.dibujar_ahorcado(intentos, max_intentos)

            juego.mostrar_progreso(palabra, letras_acertadas)
            print("Letras falladas:", " ".join(letras_falladas))

            # Victoria
            ganado = True
            for l in palabra:
                if l not in letras_acertadas:
                    ganado = False
                    break

            if ganado:
                print("¡Has ganado esta ronda!")
                puntuacion += 1
            else:
                if intentos >= max_intentos:
                    print("Has perdido esta ronda. La palabra era:", palabra)

            # Guardar ronda
            round_id = str(uuid.uuid4())
            with open("data/rounds_in_games.csv", "a", encoding="utf-8") as f:
                f.write(f"{game_id},{palabra},{usuario},{round_id},{intentos},{ganado}\n")

            if ganado or intentos >= max_intentos:
                break

    # Fin de partida
    end_date = datetime.now()

    print(f"\nPartida finalizada. Tu puntuación es: {puntuacion}/3. Gracias por jugar, {usuario}.")

    # Guardar partida
    with open("data/games.csv", "a", encoding="utf-8") as f:
        f.write(f"{game_id},{usuario},{start_date},{end_date},{puntuacion}\n")


if __name__ == "__main__":
    main()