from hangman import Hangman
import random  # Necesario para pistas

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

    # Selección de dificultad
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

    # Número de rondas
    rondas = 3

    for ronda in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda} ---")

        # Seleccionar palabra sin repetir
        while True:
            palabra = juego.get_random_word()
            if palabra not in palabras_usadas:
                palabras_usadas.append(palabra)
                break

        print("Se ha seleccionado una palabra al azar")

        # Mostrar palabra inicial
        juego.mostrar_palabra_oculta(palabra)

        # Lista de letras acertadas
        letras_acertadas = []

        # Letras falladas
        letras_falladas = []

        # Contador de intentos
        intentos = 0

        while True:
            # Opción de pista
            letra = input("Introduce una letra o 'pista': ").lower().strip()

            # Sistema de pistas
            if letra == "pista":
                if pistas_restantes > 0:
                    pistas_restantes -= 1

                    letras_no_descubiertas = []
                    for l in palabra:
                        if l not in letras_acertadas:
                            letras_no_descubiertas.append(l)

                    if len(letras_no_descubiertas) > 0:
                        pista = random.choice(letras_no_descubiertas)
                        print("Pista:", pista)

                    print("Pistas restantes:", pistas_restantes)
                else:
                    print("No tienes pistas")
                continue

            # Validar que solo se introduce una letra
            if len(letra) != 1:
                print("Introduce solo una letra")
                continue

            # Evitar repetir también letras falladas
            if letra in letras_acertadas or letra in letras_falladas:
                print("Ya has usado esa letra")
                continue

            # Comprobar letra
            acierto = juego.comprobar_letra(palabra, letra)

            if acierto:
                letras_acertadas.append(letra)
            else:
                intentos += 1
                letras_falladas.append(letra)

                print(f"Intentos fallidos: {intentos}/{max_intentos}")

                # Mostrar intentos restantes
                print(f"Intentos restantes: {max_intentos - intentos}")

                # Pasar max_intentos al dibujo
                juego.dibujar_ahorcado(intentos, max_intentos)

            # Mostrar progreso actualizado
            juego.mostrar_progreso(palabra, letras_acertadas)

            # Mostrar letras falladas
            print("Letras falladas:", " ".join(letras_falladas))

            # Comprobar si se ha ganado
            ganado = True
            for l in palabra:
                if l not in letras_acertadas:
                    ganado = False
                    break

            if ganado:
                print("¡Has ganado esta ronda!")
                break

            # Comprobar si se ha perdido
            if intentos >= max_intentos:
                print("Has perdido esta ronda. La palabra era:", palabra)
                break


if __name__ == "__main__":
    main()